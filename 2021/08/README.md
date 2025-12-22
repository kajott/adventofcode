# [2021, Day 8: Seven Segment Search](https://adventofcode.com/2021/day/8)

The input consists of (typically) 200 lines, each consisting of 10 "signal patterns" and 4 "output digits", each consisting of 2 to 7 letters between `a` and `g`, in random order.

The "signal patterns" correspond to the seven segments of a classical digital numeric display, except that the segment assignments are randomized per input line. The "output digits" denote which segments light up to form a 4-digit number.

**Part 1** asks how often the digits 1, 4, 7 and 8 are appearing in the output.

**Part 2** asks to fully decode the four displayed digits for each line.


## Solution Notes

Part 1 is a trivial training task, nothing to see there.

Part 2 is a different beast altogether. Programming-wise, it isn't too bad (golf-specific issues notwithstanding); the complicated part is coming up with a recipe on how to deduce the numbers from the observed patterns. There are certainly several ways to approach this, and I'm not sure whether mine is the optimal one, but here it is (spoilers ahead!):

- Numbers #1, #7, #4 and #8 can be trivially deduced by the pattern length (2, 3, 4, and 8, respectively), as already explained in the task description.
- Of the three patterns with length 5, number #3 is the only one that is a true superset of #1.
- Of the other two patterns of length 5, number #5 contains segment B (which is present in #4, but not #3), while number #2 doesn't.
- The three length-6 patterns are all missing exactly one of the segments: #6 is missing C (which is present in #3, but not #5), #9 is missing E (which is present in #2, but not #3), and #0 is missing D (which doesn't need to be determined, because #0 is the only remaining number at that point).

Turning all of this into a compact implementation wasn't trivial. It all revolves around global variables for the current set of patterns and the current pattern-to-number map, and a function that takes the target number, pattern length and a condition function as parameters; it locates the one pattern that has the correct length and fulfills the condition, enters it into the map, and returns the pattern as a set. Using these return values and set arithmetics, the necessary deduction operations can be done easily. It's still an awful lot of `lambda`s, and one _very_ long line, but it's not the most complicated thing either.

* Part 1, Python: 118 bytes, <100 ms
* Part 2, Python: 455 bytes, <100 ms
