# 2018, Day 16: Chronal Classification

As you see the Elves defend their hot chocolate successfully, you go back to falling through time. This is going to become a problem.

If you're ever going to return to your own time, you need to understand how this device on your wrist works. You have a little while before you reach your next destination, and with a bit of trial and error, you manage to pull up a programming manual on the device's tiny screen.

## Part 1

According to the manual, the device has four [registers](https://en.wikipedia.org/wiki/Hardware_register) (numbered `0` through `3`) that can be manipulated by [instructions](https://en.wikipedia.org/wiki/Instruction_set_architecture#Instructions) containing one of 16 opcodes. The registers start with the value `0`.

Every instruction consists of four values: an _opcode_, two _inputs_ (named `A` and `B`), and an _output_ (named `C`), in that order. The opcode specifies the behavior of the instruction and how the inputs are interpreted. The output, `C`, is always treated as a register.

In the opcode descriptions below, if something says "_value `A`_", it means to take the number given as `A` _literally_. (This is also called an "immediate" value.) If something says "_register `A`_", it means to use the number given as `A` to read from (or write to) the _register with that number_. So, if the opcode `addi` adds register `A` and value `B`, storing the result in register `C`, and the instruction `addi 0 7 3` is encountered, it would add `7` to the value contained by register `0` and store the sum in register `3`, never modifying registers `0`, `1`, or `2` in the process.

Many opcodes are similar except for how they interpret their arguments. The opcodes fall into seven general categories:

Addition:

*   `addr` (add register) stores into register `C` the result of adding register `A` and register `B`.
*   `addi` (add immediate) stores into register `C` the result of adding register `A` and value `B`.

Multiplication:

*   `mulr` (multiply register) stores into register `C` the result of multiplying register `A` and register `B`.
*   `muli` (multiply immediate) stores into register `C` the result of multiplying register `A` and value `B`.

[Bitwise AND](https://en.wikipedia.org/wiki/Bitwise_AND):

*   `banr` (bitwise AND register) stores into register `C` the result of the bitwise AND of register `A` and register `B`.
*   `bani` (bitwise AND immediate) stores into register `C` the result of the bitwise AND of register `A` and value `B`.

[Bitwise OR](https://en.wikipedia.org/wiki/Bitwise_OR):

*   `borr` (bitwise OR register) stores into register `C` the result of the bitwise OR of register `A` and register `B`.
*   `bori` (bitwise OR immediate) stores into register `C` the result of the bitwise OR of register `A` and value `B`.

Assignment:

*   `setr` (set register) copies the contents of register `A` into register `C`. (Input `B` is ignored.)
*   `seti` (set immediate) stores value `A` into register `C`. (Input `B` is ignored.)

Greater-than testing:

*   `gtir` (greater-than immediate/register) sets register `C` to `1` if value `A` is greater than register `B`. Otherwise, register `C` is set to `0`.
*   `gtri` (greater-than register/immediate) sets register `C` to `1` if register `A` is greater than value `B`. Otherwise, register `C` is set to `0`.
*   `gtrr` (greater-than register/register) sets register `C` to `1` if register `A` is greater than register `B`. Otherwise, register `C` is set to `0`.

Equality testing:

*   `eqir` (equal immediate/register) sets register `C` to `1` if value `A` is equal to register `B`. Otherwise, register `C` is set to `0`.
*   `eqri` (equal register/immediate) sets register `C` to `1` if register `A` is equal to value `B`. Otherwise, register `C` is set to `0`.
*   `eqrr` (equal register/register) sets register `C` to `1` if register `A` is equal to register `B`. Otherwise, register `C` is set to `0`.

Unfortunately, while the manual gives the _name_ of each opcode, it doesn't seem to indicate the _number_. However, you can monitor the CPU to see the contents of the registers before and after instructions are executed to try to work them out. Each opcode has a number from `0` through `15`, but the manual doesn't say which is which. For example, suppose you capture the following sample:

    Before: [3, 2, 1, 1]
    9 2 1 2
    After:  [3, 2, 2, 1]
    

This sample shows the effect of the instruction `9 2 1 2` on the registers. Before the instruction is executed, register `0` has value `3`, register `1` has value `2`, and registers `2` and `3` have value `1`. After the instruction is executed, register `2`'s value becomes `2`.

The instruction itself, `9 2 1 2`, means that opcode `9` was executed with `A=2`, `B=1`, and `C=2`. Opcode `9` could be any of the 16 opcodes listed above, but only three of them behave in a way that would cause the result shown in the sample:

*   Opcode `9` could be `mulr`: register `2` (which has a value of `1`) times register `1` (which has a value of `2`) produces `2`, which matches the value stored in the output register, register `2`.
*   Opcode `9` could be `addi`: register `2` (which has a value of `1`) plus value `1` produces `2`, which matches the value stored in the output register, register `2`.
*   Opcode `9` could be `seti`: value `2` matches the value stored in the output register, register `2`; the number given for `B` is irrelevant.

None of the other opcodes produce the result captured in the sample. Because of this, the sample above _behaves like three opcodes_.

You collect many of these samples (the first section of your puzzle input). The manual also includes a small test program (the second section of your puzzle input) - you can _ignore it for now_.

Ignoring the opcode numbers, _how many samples in your puzzle input behave like three or more opcodes?_

Your puzzle answer was `592`.

## Part 2

Using the samples you collected, work out the number of each opcode and execute the test program (the second section of your puzzle input).

_What value is contained in register `0` after executing the test program?_

Your puzzle answer was `557`.


## Solution Notes

The puzzle itself is rather straightforward, but parsing the input and resolving the operations is slightly non-trivial, so I opted for a non-golf implementation first and derived the minimal programs from there. Still, they are relatively large, because the 16 `lambda`s that execute the instructions take up quite some space, especially since the full `lambda` and parameter specification must be repeated ever time.

* Part 1, Python: 633 bytes, <100 ms
* Part 2, Python: 814 bytes, <100 ms
