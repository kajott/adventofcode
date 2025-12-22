# [2020, Day 8: Handheld Halting](https://adventofcode.com/2020/day/8)

The input consists of (typically) 600 instructions for a virtual machine with a single register and three different instructions: NOP, increment register by signed immediate, and unconditional relative jump with signed offset. NOPs have an immediate parameter too, but this is ignored. The register's value starts at zero.

**Part 1** asks for the value of the register before the first loop, i.e. before any instruction is executed a second time.

**Part 2** reveals that the program is not supposed to loop, but should run to the end instead, and that one of the NOPs should be a jump or vice-versa. The task is to determine the value of the register after executing the fixed program.


## Solution Notes

An almost trivial interpreter. Since there's no conditional jumps, part 2 is easily solvable by brute-force modifying every instruction in turn and running the program.

* Part 1, Python: 157 bytes, <100 ms
* Part 2, Python: 258 bytes, <100 ms
