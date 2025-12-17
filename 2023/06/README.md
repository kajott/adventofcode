# [2023, Day 6: Wait For It](https://adventofcode.com/2023/day/6)


## Solution Notes

A very easy puzzle. The problem size in part 2 is fortunately small enough that brute force is a [perfectly cromulent](https://www.merriam-webster.com/wordplay/what-does-cromulent-mean) approach to solving it, and it doesn't exceed the range and precision of 64-bit floating-point values either, so solving the underlying quadratic equation is also not a problem. I tried both solutions, and it's the classic code size vs. run time tradeoff: Brute force takes 5 seconds, but it's also 6 bytes shorter.

* Part 1, Python: 116 bytes, <100 ms
* Part 2, Python (brute force): 99 bytes, ~5 s
* Part 2, Python (quadratic equation solving): 105 bytes, <100 ms
