# [2024, Day 3: Mull It Over](https://adventofcode.com/2024/day/3)

The input consists of (typically) 20 kB of gibberish containing fragments of apparent computer code, 3-digit numbers and random symbols inbetween.

**Part 1** asks to find instances of `mul(A,B)` "instructions", with `A` and `B` being numbers.

**Part 2** is the same, but it specifies that matches between `don't()` and `do()` shall be ignored.


## Solution Notes

This is the perfect use case for regular expressions; I bet that every other approach is going to be more complicated. The easiest way to implement part 2 is using regular expressions (again) to substitute the `don't()`...`do()` segments by an empty string before putting it into the same evaluation as used in part 1. There are a few pitfalls though: First, matching the span between `don't()` and `do()` must be non-greedy, otherwise it will remove too much; second, the input contains a few newline characters, so matching must cross over these as well; and finally, the input may end with a `don't()` block that must also be removed.

* Part 1, Python: 105 bytes, <100 ms
* Part 2, Python: 149 bytes, <100 ms
