# [2019, Day 9: Sensor Boost](https://adventofcode.com/2019/day/9)

This puzzle extends the Intcode virtual machine that has been introduced in [days 2](../02) [and 5](../05), and which is going to be used a lot during AoC 2019.

Intcode operates on memory containing signed integers of only vaguely specified word size; 52 bits seem to be sufficient in practice though. The memory contains both the program code and data. There are no registers, except the instruction pointer (`pc`) and "relative base" (`sp`).

Instruction operands can use the following modes:
- mode `0` = "position mode": `op(x) := mem[x]`
- mode `1` = "immediate mode": `op(x) := x`
- mode `2` = "relative mode": `op(x) := mem[sp+x]`

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
- `9,a` = adjust relative base: `sp = sp + a`
- `99` = stop execution

The input for this task consists of an Intcode core dump of (typically) 970 words.

**Parts 1 and 2** ask for the output of the program when inputting `1` and `2`, respectively.


## Solution Notes

With this, the Intcode machine gets a proper stack, and the program of part 2 makes already good use of it.

The golf implementations are almost identical, only the input parameter changes.

* Part 1, Python: 418 bytes, <100 ms
* Part 2, Python: 418 bytes, ~2.5 s
