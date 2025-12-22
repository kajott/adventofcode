# [2022, Day 25: Full of Hot Air](https://adventofcode.com/2022/day/25)

The input consists of (typically) 135 numbers of 2 to 19 digits in balanced quinary, i.e. each digit can have the values -2 / -1 / 0 / +1 / +2.

The tasks asks for adding all the numbers and outputting them in balanced quinary again.


## Solution Notes

A very simple, yet interesting task; for people who never heard of balanced quinary or at least [balanced ternary](https://en.wikipedia.org/wiki/Balanced_ternary), this might have been a head-scratcher.

There are two fundamental ways to implement the task: Either "import" numbers, add them together and "export" to balanced quinary again, or perform the addition directly in the balanced quinary system. I implemented both and was very surprised to find out that the round-trip through binary is significantly more space-efficient than the direct method.

* Part 1, Python (with conversions): 169 bytes, <100 ms
* Part 1, Python (direct addition): 199 bytes, <100 ms
