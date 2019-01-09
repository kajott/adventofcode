#if 0
cc -Wall -Wno-unused-result -g -O9 -march=native $0 || exit 1
exec ./a.out $*
#endif

#include <stdint.h>
#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>
#include <assert.h>

// state encoding: 2 bits per object (including elevators),
// packed from LSB to MSB, containing the positions of each object in order:
// (MSB) elevator, gen N, chip N, ..., gen 1, chip 1, gen 0, chip 0 (LSB)
// floor numbers are inverted: floor 0 is the target floor

// note that the parser is *not* fault-tolerant at all

#if 0
    #define Dprintf printf
    #define Ddump_state dump_state
#else
    #define Dprintf(...) do{}while(0)
    #define Ddump_state(...) do{}while(0)
#endif

#ifndef EXTRA_OBJECTS
#define EXTRA_OBJECTS 0  // 0 for part 1, 4 for part 2
#endif

#define MAX_DEPTH 0

#define FLOOR_BITS   2
#define MAX_OBJECTS (10 + EXTRA_OBJECTS)
#define NUM_FLOORS (1 << FLOOR_BITS)
#define FLOOR_MASK (NUM_FLOORS - 1)

#define MAX_ELEMENT_NAME_LENGTH 32

#define MAX_QUEUE_SIZE (8 * 1024 * 1024)  // must be a power of two

#define STATE_BITS ((MAX_OBJECTS + 1) * FLOOR_BITS)

#if STATE_BITS <= 16
    typedef uint16_t state_t;
#elif STATE_BITS <= 32
    typedef uint32_t state_t;
#else
    typedef uint64_t state_t;
#endif

unsigned object_count = 0;  // not including the elevator

#define GET_POS(state, obj) (((state) >> ((obj) * FLOOR_BITS)) & FLOOR_MASK)
#define SET_POS(state, obj, pos) do { state = (state & ~(FLOOR_MASK << ((obj) * FLOOR_BITS))) | ((pos) << ((obj) * FLOOR_BITS)); } while (0)

state_t queue[MAX_QUEUE_SIZE];
uintptr_t queue_rpos, queue_wpos;
inline void add_to_queue(state_t state) {
    queue[queue_wpos] = state;
    queue_wpos = (queue_wpos + 1) & (MAX_QUEUE_SIZE - 1);
    assert(queue_wpos != queue_rpos);
}

uint8_t visited[1 << (STATE_BITS - 3)];
#define CHECK_VISITED(state) (visited[(state >> 3)] & (1 << (state & 7)))
#define MARK_VISITED(state) do { visited[(state >> 3)] |= (1 << (state & 7)); } while (0)

void dump_state(state_t state, bool eof) {
    printf("[0x%08X]", state);
    for (unsigned floor = 0;  floor < NUM_FLOORS;  ++floor) {
        if (floor) printf(" |");
        if (GET_POS(state, object_count) == floor) printf(" E");
        for (unsigned oid = 0;  oid < object_count;  ++oid) {
            if (GET_POS(state, oid) == floor) printf(" %c%d", "MG"[oid & 1], (oid >> 1) + 1);
        }
    }
    if (eof) printf("\n");
}


// parse a line and return a bitmask; may update object_count as a side effect!
state_t parse_line(char* line, const char *marker) {
    static char names[MAX_OBJECTS / 2][MAX_ELEMENT_NAME_LENGTH];
    char *pos, *name;
    state_t state = 0;
    while ((pos = strstr(line, marker))) {
        *pos = '\0';
        for (name = pos;  !isspace(name[-1]);  --name);
        unsigned oid;
        for (oid = 0;  names[oid][0] && strcmp(names[oid], name);  ++oid)
            assert(oid < MAX_OBJECTS);
        strcpy(names[oid], name);
        *pos = '~';
        oid <<= 1;  // there are two objects per element!
        state |= 1 << (oid * FLOOR_BITS);
        if (oid >= object_count) { object_count = oid + 2; }
    }
    return state;
}




int main(int argc, char *argv[]) {
    // parse input
    FILE *f = fopen((argc > 1) ? argv[1] : "input.txt", "r");
    state_t initial_state = 0;
    for (int floor = NUM_FLOORS - 1;  floor >= 0;  --floor) {
        char line[512];
        fgets(line, 512, f);
        initial_state |= parse_line(line, "-compatible microchip") * floor;
        initial_state |= parse_line(line, " generator") * (floor << FLOOR_BITS);
    }
    fclose(f);
    for (unsigned extra = 0;  extra < EXTRA_OBJECTS;  ++extra) {
        SET_POS(initial_state, object_count, NUM_FLOORS - 1);
        object_count++;
    }
    SET_POS(initial_state, object_count, NUM_FLOORS - 1);

    printf("sizeof(queue) = %d MiB\n", (int)(sizeof(queue) >> 20));
    printf("sizeof(visited) = %d MiB\n", (int)(sizeof(visited) >> 20));
    printf("%d objects in total.\n", object_count);
    Dprintf("initial state: ");
    Ddump_state(initial_state, true);
    queue[0] = initial_state;
    queue[1] = 0;
    queue_wpos = 2;
    MARK_VISITED(initial_state);

    unsigned depth = 0;

    while (queue_rpos != queue_wpos) {
        // fetch new state to analyze
        state_t state = queue[queue_rpos];
        queue_rpos = (queue_rpos + 1) & (MAX_QUEUE_SIZE - 1);

        // end-of-depth sentinel found?
        if (!state) {
            depth++;
            printf("depth %d: %d moves\n", depth, (int)((queue_wpos - queue_rpos) & (MAX_QUEUE_SIZE - 1)));
#if MAX_DEPTH
            if (depth >= MAX_DEPTH) break;
#endif
            // add a new sentinel
            add_to_queue(0);
            continue;
        }

        Dprintf("  * %d ", depth); Ddump_state(state, true);

        // generate child states
        unsigned pos = state >> (object_count * FLOOR_BITS);
        state_t check1 = state;
        for (unsigned obj1 = 0;  obj1 < object_count;  ++obj1, check1 >>= FLOOR_BITS) {
            if ((check1 & FLOOR_MASK) != pos) continue;
            state_t check2 = state >> (obj1 * FLOOR_BITS);
            for (unsigned obj2 = obj1;  obj2 < object_count;  ++obj2, check2 >>= FLOOR_BITS) {
                if ((check2 & FLOOR_MASK) != pos) continue;
                for (unsigned newpos = pos ? (pos - 1) : (pos + 1);  (newpos <= (pos + 1)) && (newpos < NUM_FLOORS);  newpos += 2) {
                    // compute new state
                    state_t newstate = state;
                    SET_POS(newstate, obj1, newpos);
                    SET_POS(newstate, obj2, newpos);
                    SET_POS(newstate, object_count, newpos);
                    Dprintf("      > "); Ddump_state(newstate, false);

                    // check for win situation
                    if (!newstate) {
                        Dprintf(" (DONE)\n");
                        printf("solution found at depth:\n%d\n", depth + 1);
                        return 0;
                    }

                    // check for already visited
                    if (CHECK_VISITED(newstate)) {
                        Dprintf(" (cycle)\n");
                        continue;
                    }

                    // check for invalid move
                    state_t objlist = 0;
                    for (state_t bit = 1, checkX = newstate;  bit < (1 << object_count);  bit <<= 1, checkX >>= 2) {
                        if ((checkX & FLOOR_MASK) == newpos) { objlist |= bit; }
                    }
                    state_t gens = (objlist & 0xAAAAAAAA) >> 1;
                    state_t chips = objlist & 0x55555555;
                    if (gens && (chips & ~gens)) {
                        Dprintf(" (invalid)\n");
                        continue;
                    }

                    // add state to queue
                    Dprintf(" (OK)\n");
                    add_to_queue(newstate);
                    MARK_VISITED(newstate);

                    // end of child state check loop
                }
            }
        }
    }
    printf("no solution found.\n");
    return 1;
}
