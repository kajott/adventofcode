# [2024, Day 19: Linen Layout](https://adventofcode.com/2024/day/19)

The input consists of (typically) 400 strings of (typically) 40 to 60 characters, and a list of (typically) 450 shorter substrings of (typically) 2 to 8 characters.

**Part 1** asks how many of the long strings can be built by concatenating any number of the short strings and no other letters.

**Part 2** asks, for each of the longer strings, how many different arrangements of the shorter strings can be used to create each the longer string.


## Solution Notes

Part 1's task can be done directly with regular expressions, so unsurprisingly, the best solution for that is to turn the input pattern list into a regex of form `/(r|wr|b|g|...|br)+$/` and check if that matches.

For part 2, the task of the regular expression matcher needs to be spelled out "by hand" in the form of a rather basic DFS with memoization.

Fun fact: Part 2's solution can be turned into part 1 simply by replacing the `abs()` call with `any()`.

* Part 1, Python: 125 bytes, <100 ms
* Part 2, Python: 206 bytes, ~700 ms
