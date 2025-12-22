# [2023, Day 13: Point of Incidence](https://adventofcode.com/2023/day/13)

The input consists of (typically) 100 2D grids of varying sizes between 7 and 17 rows and columns, densely populated with objects.

**Part 1** asks to find a horizontal or vertical symmetry axis in all of the grids.

**Part 2** asks the same, but considering an "off by one" error where an object has to be inserted or removed at exactly one place before checking for symmetry.


## Solution Notes

Usually, my go-to data structure for puzzles with 2D fields is sets of complex numbers, but these are of limited to no usefulness here. In fact, the simplest conceivable representation is the most convenient for the task at hand: A simple list of strings (or two-level nested lists of characters, which is almost the same in most languages anyway). This makes the vertical reflection check almost trivial, since entire strings / character lists can be compared against each other. For the horizontal direction, the same algorithm can be used on transposed input.

Part 2 is merely a slight change to the comparison function: Instead of checking for identity, check for exactly one error. It's a little less convenient to write, but no big deal either.

* Part 1, Python: 211 bytes, <100 ms
* Part 2, Python: 260 bytes, <100 ms
