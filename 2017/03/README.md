# [2017, Day 3: Spiral Memory](https://adventofcode.com/2017/day/3)


## Solution Notes

The hardest part of these puzzles is wrapping your head around the spiral data organization. I solved part 1 in an (I think) rather clever way that doesn't compute the target cell's coordinates explicitly; while this results in a very compact implementation, it's not reusable for part 2, where an explicit spiral walk is really required. The field size is surprisingly small though: For my input, an 8x8 field would already be sufficient, though my implementation uses a field that's roughly twice as big, in case anybody uses it for larger input numbers.

* Part 1, Python: 68 bytes, <100 ms
* Part 2, Python: 202 bytes, <100 ms
