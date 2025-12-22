# [2021, Day 5: Hydrothermal Venture](https://adventofcode.com/2021/day/5)

The input consists of (typically) 500 pairs of 2-to-3-digit 2D coordinates, describing lines.

**Part 1** asks for the number of places where at least two lines overlap, while ignoring all lines that aren't purely horizontal or vertical.

**Part 2** asks the same, but for *all* lines in the input, which includes lines at 45-degree angles.


## Solution Notes

My initial approach for part 1 was to construct a list of locations that are touched by every line and adding those to a dictionary. (Complex numbers are of no help in that case.) Some care has to be taken to avoid off-by-one errors (missing initial/final points) and be able to work with lines in either direction (up *and* down, left *and* right), but overall it's a fine and efficient approach.

For part 2, however, this doesn't scale so well: Constructing the point lists for diagonals isn't as easy as it was for the horizontal and vertical lines. I tried a much dumber approach instead: Since all coordinates in the input are guaranteed to be valid hor/vert/diag lines, we can just start at the first index and iterate with increasing/decreasing coordinates depending on where the line's end position is located, stopping after(!) the end point has been reached. This is far slower, but still totally acceptable in terms of runtime. In fact, this approach works so well that code size is significantly *lower* than for part 1! Using the iterative approach for part 1 too makes the difference shrink a bit, but still it's one of those puzzles where part 2 is actually the easier thing to do, if done properly.

* Part 1, Python (coordinate list): 295 bytes, <100 ms
* Part 1, Python (using part 2 approach): 275 bytes, ~150 ms
* Part 2, Python: 253 bytes, ~250 ms
