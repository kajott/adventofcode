# [2021, Day 13: Transparent Origami](https://adventofcode.com/2021/day/13)

The input consists of (typically) 900 3-digit 2D coordinates, and a list of (typically) 12 instructions to "fold" along either the X or Y axis at some position.

Dots are to be entered into a grid at the specified coordinates, followed by executing the folding operations. Each fold merges all dots right of or below the crease to the left or above. There can be multiple dots at a position after folding.

**Part 1** asks for the number of dots after executing the first fold.

**Part 2** asks for the letters that become visible after executing all folds.


## Solution Notes

Nothing special here; just implement as specified and it's done.

* Part 1, Python: 237 bytes, <100 ms
* Part 2, Python: 286 bytes, <100 ms
