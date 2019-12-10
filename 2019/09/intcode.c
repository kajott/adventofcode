#if 0  // self-compiling code
gcc -std=c99 -Wall -Wextra -pedantic -Werror -g -O4 -march=native -fwrapv $0 || exit 1
exec time ./a.out $*
#endif

#include <stdbool.h>
#include <stdint.h>
#include <inttypes.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>
#include <assert.h>

//! default VM memory size (in words)
#define VM_SIZE (640 * 1024)  // 640 kilowords ought to be enough for everybody (tm)

#define ENABLE_CHECKS  1  //!< whether to enable range checks
#define ENABLE_TRACING 1  //!< whether to compile tracing code (if set to 0, tracing is ignored)

#define TRACE_PREFIX_LEN 16  //!< maximum length of machine-specific tracing prefix (in characters)

///////////////////////////////////////////////////////////////////////////////

typedef int64_t ic_word_t;  //!< word data type
#define PRW "%" PRId64      //!< macro to print word values (must match ic_word_t)

//! \private internal state of an Intcode VM
typedef struct _intcode {
    char trace_prefix[TRACE_PREFIX_LEN];  //!< prefix of each line when tracing
    bool tracing;                         //!< trace mode enable/disable bit
    ic_word_t ip;                         //!< instruction pointer
    ic_word_t rb;                         //!< relative base (stack pointer)
    bool in_valid;                        //!< input data valid flag
    ic_word_t in_data;                    //!< input data word
    bool out_valid;                       //!< output data valid flag
    ic_word_t out_data;                   //!< output data word
    ic_word_t mem_size;                   //!< memory size (in words)
    ic_word_t mem[1];                     //!< memory contents
} ic_machine_t;

//! stop condition for ic_run
typedef enum _stop {
    IC_RUNNING = 0,  //!< still running (not stopped)
    IC_STOP_HALT,    //!< hit 'halt' or undefined instruction
    IC_STOP_INPUT,   //!< waiting for input data
    IC_STOP_OUTPUT,  //!< output data has become available
} ic_stop_t;

//! convert a stop condition to a human-readable string
const char *ic_stop_to_str(ic_stop_t stop) {
    switch (stop) {
        case IC_RUNNING:     return "machine is still running"; break;
        case IC_STOP_HALT:   return "machine halted"; break;
        case IC_STOP_INPUT:  return "input value requested"; break;
        case IC_STOP_OUTPUT: return "output value ready"; break;
        default:             return "invalid stop condition"; break;
    }
}

//! create a new Intcode VM
//! \param[in] program       program memory to pre-initialize
//! \param[in] program_size  size of program (in words)
//! \param[in] mem_size      total memory size (in words; 0 = default)
//! \returns new VM instance, or NULL on failure
ic_machine_t* ic_create(const ic_word_t *program, ic_word_t program_size, ic_word_t mem_size) {
    if (mem_size < program_size) {
        mem_size = program_size;
    }
    ic_machine_t* ic = malloc(sizeof(ic_machine_t) + sizeof(ic_word_t) * (mem_size - 1));
    memset(ic, 0, sizeof(ic_machine_t));
    memcpy(ic->mem, program, sizeof(ic_word_t) * program_size);
    if (mem_size > program_size) {
        memset(&ic->mem[program_size], 0, sizeof(ic_word_t) * (mem_size - program_size));
    }
    ic->mem_size = mem_size;
    return ic;
}

//! configure tracing for a VM
//! \param[inout] ic       the VM handle
//! \param[in]    tracing  true to enable tracing, false to disable tracing
//! \param[in]    prefix   prefix to use when tracing;
//!                        up to TRACE_PREFIX_LEN characters;
//!                        NULL = don't modify prefix
inline void ic_set_tracing(ic_machine_t* ic, bool tracing, const char* prefix) {
    if (!ic) { return; }
    ic->tracing = tracing;
    if (prefix) {
        strncpy(ic->trace_prefix, prefix, TRACE_PREFIX_LEN - 1);
        ic->trace_prefix[TRACE_PREFIX_LEN - 1] = '\0';
    }
}

//! input a value into the VM
//! \param[inout] ic    the VM handle
//! \param[in]    data  the value to input
//! \returns true if successful, false if there's still existing input data for the VM
inline bool ic_input(ic_machine_t* ic, ic_word_t data) {
    if (!ic || ic->in_valid) { return false; }
    ic->in_valid = true;
    ic->in_data = data;
    return true;
}

//! check whether a VM has valid output data
inline bool ic_has_output(const ic_machine_t* ic) {
    return !!ic && ic->out_valid;
}

//! get a word of output data from the VM
//! \note This removes the data word from the VM.
inline ic_word_t ic_get_output(ic_machine_t* ic) {
    if (!ic || !ic->out_valid) { return 0; }
    ic->out_valid = false;
    return ic->out_data;
}

//! read VM memory
inline ic_word_t ic_read_mem(ic_machine_t* ic, ic_word_t addr) {
#ifdef ENABLE_CHECKS
    assert(ic);
    if ((addr < 0) || (addr >= ic->mem_size)) {
        fprintf(stderr, "ERROR: out-of-range read acccess to address " PRW "!\n", addr);
        exit(7);
    }
#endif
    return ic->mem[addr];
}

//! write VM memory
inline void ic_write_mem(ic_machine_t* ic, ic_word_t addr, ic_word_t data) {
#ifdef ENABLE_CHECKS
    assert(ic);
    if ((addr < 0) || (addr >= ic->mem_size)) {
        fprintf(stderr, "ERROR: out-of-range write acccess to address " PRW "!\n", addr);
        exit(7);
    }
#endif
    ic->mem[addr] = data;
}

//! \private instruction description table
static const struct ic_op {
    const char* name;  //!< mnemonic name of the instruction
    char size;         //!< size of the instruction (in words)
    char inputs;       //!< number of input arguments that need to be fetched
    #define IC_NUM_OPS 9
} ic_ops[IC_NUM_OPS + 1] = {
                           { "halt",  0, 0 },
    #define IC_OP_ADD   1
                           { "add",   4, 2 },
    #define IC_OP_MUL   2
                           { "mul",   4, 2 },
    #define IC_OP_IN    3
                           { "in",    2, 0 },
    #define IC_OP_OUT   4
                           { "out",   2, 1 },
    #define IC_OP_JNZ   5
                           { "jnz",   3, 2 },
    #define IC_OP_JZ    6
                           { "jz",    3, 2 },
    #define IC_OP_CMPLT 7
                           { "cmplt", 4, 2 },
    #define IC_OP_CMPEQ 8
                           { "cmpeq", 4, 2 },
    #define IC_OP_ARB   9
                           { "arb",   2, 1 },
};

//! run an Intcode VM until the next input, output or halt instruction
//! \param[inout] ic  the VM handle
//! \returns one of the IC_STOP_ codes
ic_stop_t ic_run(ic_machine_t* ic) {
    if (!ic) { return IC_STOP_HALT; }
    ic_stop_t stop = IC_RUNNING;
    do {
        // fetch and decode opcode
        #if ENABLE_TRACING
          if (ic->tracing) {
            fprintf(stderr, "%s%4d: ", ic->trace_prefix, (int)ic->ip);
          }
        #endif
        ic_word_t opcode = ic_read_mem(ic, ic->ip);
        uint8_t raw_op = (uint8_t)(opcode % 100);
        if ((raw_op < 1) || (raw_op > IC_NUM_OPS)) { raw_op = 0; }
        const struct ic_op* op = &ic_ops[raw_op];

        // trace opcode and parameters
        #if ENABLE_TRACING
          if (ic->tracing) {
            fprintf(stderr, "%05d > %-5s", (int)opcode, op->name);
            const char *sep = " ";
            ic_word_t div = 100;
            for (int argc = 1;  argc < op->size;  ++argc) {
                int mode = (opcode / div) % 10;
                ic_word_t argv = ic_read_mem(ic, ic->ip + argc);
                switch (mode) {
                    case 0:  fprintf(stderr, "%s"  PRW,     sep, argv); break;
                    case 1:  fprintf(stderr, "%s#" PRW,     sep, argv); break;
                    case 2:  fprintf(stderr, "%s(" PRW ")", sep, argv); break;
                    default: fprintf(stderr, "%s?" PRW,     sep, argv); break;
                }
                sep = ", ";
                div *= 10;
            }
            fprintf(stderr, "\n");
          }
        #endif

        // load raw arguments and adjust IP
        #define INVALID_VALUE (-123456789012LL)
        ic_word_t a = (op->size > 1) ? ic_read_mem(ic, ic->ip + 1) : INVALID_VALUE;
        ic_word_t b = (op->size > 2) ? ic_read_mem(ic, ic->ip + 2) : INVALID_VALUE;
        ic_word_t c = (op->size > 3) ? ic_read_mem(ic, ic->ip + 3) : INVALID_VALUE;
        ic_word_t old_ip = ic->ip;
        ic->ip += op->size;

        // apply parameter modes
        if (opcode >= 20000) { opcode -= 20000; c += ic->rb; }
        if (opcode >= 10000) { assert(0); }
        if (opcode >=  2000) { opcode -=  2000; b += ic->rb; }
        if (opcode >=  1000) { opcode -=  1000; } else if (op->inputs >= 2) { b = ic_read_mem(ic, b); }
        if (opcode >=   200) { opcode -=   200; a += ic->rb; }
        if (opcode >=   100) { opcode -=   100; } else if (op->inputs >= 1) { a = ic_read_mem(ic, a); }

        // execute
        switch (raw_op) {
            case IC_OP_ADD:
                ic_write_mem(ic, c, a + b);
                break;
            case IC_OP_MUL:
                ic_write_mem(ic, c, a * b);
                break;
            case IC_OP_IN:
                if (ic->in_valid) {
                    ic_write_mem(ic, a, ic->in_data);
                    ic->in_valid = false;
                } else {
                    ic->ip = old_ip;
                    stop = IC_STOP_INPUT;
                }
                break;
            case IC_OP_OUT:
                assert(!ic->out_valid);
                ic->out_data = a;
                ic->out_valid = true;
                stop = IC_STOP_OUTPUT;
                break;
            case IC_OP_JNZ:
                if (a) { ic->ip = b; }
                break;
            case IC_OP_JZ:
                if (!a) { ic->ip = b; }
                break;
            case IC_OP_CMPLT:
                ic_write_mem(ic, c, (a <  b) ? 1 : 0);
                break;
            case IC_OP_CMPEQ:
                ic_write_mem(ic, c, (a == b) ? 1 : 0);
                break;
            case IC_OP_ARB:
                ic->rb += a;
                break;
            default:
                stop = IC_STOP_HALT;
                break;
        }
    } while (stop == IC_RUNNING);
    return stop;
}

///////////////////////////////////////////////////////////////////////////////

ic_word_t* read_file(const char* filename, ic_word_t* p_size) {
    if (p_size) { *p_size = 0; }

    FILE *f = fopen(filename, "rb");
    if (!f) { return NULL; }
    fseek(f, 0, SEEK_END);
    size_t txt_size = ftell(f);
    fseek(f, 0, SEEK_SET);

    char* txt_buf = malloc(txt_size + 1);
    if (!txt_buf) { fclose(f); return NULL; }
    if (fread(txt_buf, txt_size, 1, f) != 1) { fclose(f); return NULL; }
    txt_buf[txt_size] = '\0';

    ic_word_t* out_buf = malloc(sizeof(ic_word_t) * (txt_size / 2));
    ic_word_t out_size = 0;

    char *pos = txt_buf, *end = txt_buf;
    for (;;) {
        assert(out_size < (ic_word_t)(txt_size / 2));
        out_buf[out_size] = (ic_word_t) strtoll(pos, &end, 10);
        if (!end || (end == pos) || (*end && !isspace(*end) && (*end != ','))) { break; }
        out_size++;
        pos = end;
        while (isspace(*pos)) { ++pos; }
        if (*pos != ',') { break; }
        ++pos;
    }
    free(txt_buf);
    if (p_size) { *p_size = out_size; }
    return realloc(out_buf, sizeof(ic_word_t) * out_size);
}

///////////////////////////////////////////////////////////////////////////////


int main(int argc, char* argv[]) {
    bool input_valid = false;
    ic_word_t input_data = 0;
    const char* program_file = "input.txt";
    bool tracing = false;

    for (int argp = 1;  argp < argc;  ++argp) {
        char *arg = argv[argp];
        if (!strcmp(arg, "-h") || !strcmp(arg, "--help")) {
            printf("Usage: intcode.c [-v] [<input.txt>] [<indata>]\n");
            return 0;
        } else if (!strcmp(arg, "-v")) {
            tracing = true;
        } else {
            char *end = arg;
            input_data = (ic_word_t) strtoll(arg, &end, 10);
            if (!*end) {
                input_valid = true;
            } else {
                program_file = arg;
            }
        }
    }
    
    ic_word_t prog_size = 0;
    ic_word_t *program = read_file(program_file, &prog_size);
    assert(program);

    ic_machine_t *ic = ic_create(program, prog_size, VM_SIZE);
    ic_set_tracing(ic, tracing, NULL);
    if (input_valid) { ic_input(ic, input_data); }

    ic_stop_t stop;
    do {
        stop = ic_run(ic);
        if (stop == IC_STOP_INPUT) {
            printf("? "); fflush(stdout);
            char buf[80];
            if (fgets(buf, 80, stdin)) {
                char *end = buf;
                input_data = (ic_word_t) strtoll(buf, &end, 10);
                if (!*end || (*end == '\r') || (*end == '\n')) {
                    ic_input(ic, input_data);
                    stop = IC_RUNNING;
                }
            }
        }
        if (stop == IC_STOP_OUTPUT) {
            printf(PRW "\n", ic_get_output(ic));
            stop = IC_RUNNING;
        }
    } while (stop == IC_RUNNING);
    if (stop != IC_STOP_HALT) {
        fprintf(stderr, "ERROR: unexpected stop condition: %s\n", ic_stop_to_str(stop));
    }

    free(ic);
    return 0;
}
