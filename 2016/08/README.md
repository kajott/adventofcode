# [2016, Day 8: Two-Factor Authentication](https://adventofcode.com/2016/day/8)


## Solution Notes

One might be tempted to only count the `rect` instructions for part 1, but since some of the pixels may already be active when the command is issued, a full implementation of all commands is required for part 1 too. At that point, it doesn't make any sense to separate the parts at all, as part 2's result is a necessary byproduct of part 1.

To save space, I implemented column rotations by transposing the screen, applying a row rotation (which is nicely done with Python's list slicing syntax) and transposing back.

* Parts 1+2, Python: 321 bytes, <100 ms
