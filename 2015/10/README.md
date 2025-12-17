# [2015, Day 10: Elves Look, Elves Say](https://adventofcode.com/2015/day/10)


## Solution Notes

There are two basic ways to implement this: regular expressions (which is compact, but slow) and doing the Run-Length Encoding "by hand" (which is much longer, but also faster). For part 1, I used the former approach, and for part 2, the latter (and even then, it takes *really* long to compute). Both ways work for both parts of the puzzle though; just replace the constant `40` by `50` or vice-versa.

* Part 1, Python: 121 bytes, ~700 ms
* Part 2, Python: 133 bytes, ~6 s
