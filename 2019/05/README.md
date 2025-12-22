# [2019, Day 5: Sunny with a Chance of Asteroids](https://adventofcode.com/2019/day/5)

This puzzle extends the Intcode virtual machine that has been introduced in [day 2](../02) and which is going to be used a lot during AoC 2019.

Intcode operates on memory containing signed integers of unspecified word size. The memory contains both the program code and data. There are no registers, except the instruction pointer (`pc`).

Instruction operands can use the following modes:
- mode `0` = "position mode": `op(x) := mem[x]`
- mode `1` = "immediate mode": `op(x) := x`

Instruction opcodes are stored in the lower two decimal digits of an instruction word. The 100s digit in the instruction word specifies the mode for the first operand, the 1000s digit in the instruction word specifies the mode for the second operand, etc. The operands themselves are specified as separate words following the instruction word.

The following opcodes are supported:
- `1,a,b,d` = add: `mem[d] = op(a) + op(b)`
- `2,a,b,d` = multiply: `mem[d] = op(a) * op(b)`
- `3,d` = input: `mem[d] = input()`
- `4,a` = output: `output(op(a))`
- `5,a,j` = jump if true: `if op(a) != 0 then pc = op(j)`
- `6,a,j` = jump if false: `if op(a) == 0 then pc = op(j)`
- `7,a,b,d` = less than: `mem[d] = (op(a) < op(b)) ? 1 : 0`
- `8,a,b,d` = equals: `mem[d] = (op(a) == op(b)) ? 1 : 0`
- `99` = stop execution

The input for this task consists of an Intcode core dump of (typically) 680 words.

**Parts 1 and 2** ask for the program's output if some specific value is input. The value differs between the parts.


## Solution Notes

Intcode slowly evolves to a properly usable ISA; whith the comparison and `jz`/`jnz` instructions, it doesn't even rely on self-modifying code to do anything meaningful any longer. The interpreter starts to become unwieldy though, especially in the golf version.

As for the puzzle itself, it's just straightforward emulation, with no surprises whatsoever.

* Part 1, Python: 271 bytes, <100 ms
* Part 2, Python: 342 bytes, <100 ms
