# [2021, Day 10: Syntax Scoring](https://adventofcode.com/2021/day/10)

The input consists of (typically) 110 lines of 90-110 random brackets of various types (`(`/`)`, `[`/`]`, `{`/`}`, `<`/`>`). The brackets never match properly, there are always glitches: The line may be truncated, and/or closing brackets may not match the correct opening brace type.

**Part 1** asks to find the first invalid closing bracket, if any, in each line.

**Part 2** asks to complete the incomplete lines.


## Solution Notes

For part 1, the stack operations are simply simulated and as soon as a "pop" occurs with a mismatched tag, the alarm is rung.

Part 2 needs to keep the stack checking code intact, if only to exclude the irrelevant lines; some additional annoying (and not even complex) coding is then required to implement the base-5 scoring and compute the median.

* Part 1, Python: 208 bytes, <100 ms
* Part 2, Python: 251 bytes, <100 ms
