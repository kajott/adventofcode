# [2020, Day 2: Password Philosophy](https://adventofcode.com/2020/day/2)

The input consists of (typically) 1000 lines cantaining a 1-to-2-digit number range, a single character, and a string of 4 to 20 characters.

**Part 1** asks how many of the lines indeed contain as many instances as indicated of the specified character in the long string. Characters need not be consecutive.

**Part 2** asks how many lines contain the specified character in exactly one of the range's limits, disregarding the characters inbetween.


## Solution Notes

Nothing special really; parsing the input is the most awkward part.

Initially, I interpreted the rules wrongly and searched for N to M _consecutive_ matches.
I almost expected that this would be the answer for part 2, but there was a different (even easier) twist to it.

* Part 1, Python: 137 bytes, <100 ms
* Part 2, Python: 144 bytes, <100 ms
