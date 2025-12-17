# 2016, Day 25: Clock Signal


## Solution Notes

A frustrating reverse engineering puzzle -- or so I thought. In fact, the real enlightenment came (after fixing a bug in my emulator) when observing the output patterns: It's just a bit-reversed 12-bit binary number repeated over and over again. This number, in turn, is the product of two constants right at the beginning of the code, plus the value of register `a`. In other words, the task is to take a 12-bit number that consists of an alternating bit pattern (i.e. `0xAAA`) and subtract the input's constant from it.

* Part 1, Python: 114 bytes, <100 ms
