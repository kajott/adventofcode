# [2020, Day 14: Docking Data](https://adventofcode.com/2020/day/14)

The input consists of (typically) 600 instructions. Each instruction either defines a 36-bit ternary mask (containing `1`, `0` or `X` in each position), or a memory write of some 3-to-9-digit number into some 3-to-5-digit address.

The write instructions only affect bits marked as `X` in the mask. Mask bits `0` and `1` are always written to memory as such.

**Part 1** asks for the memory contents after the instructions completed.

**Part 2** asks the same, but the mask is also applied to the write **addresses**, albeit in a different way: a mask bit of `0` doesn't modify the address, a mask bit of `1` forces it to `1`, and a mask bit of `X` causes the address bit to become `X` to. A write to a memory address with `X`es in it will then modify *all* matching addresses.


## Solution Notes

The basic idea for both parts is that the tri-state mask has to be decomposed into an "AND part" and an "OR part". For part 2, there's an additional iteration over all the 2^(number of X'es) combinations.

* Part 1, Python: 179 bytes, <100 ms
* Part 2, Python: 292 bytes, ~150 ms
