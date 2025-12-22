# [2024, Day 9: Disk Fragmenter](https://adventofcode.com/2024/day/9)

The input consists of a (typically) 10,000-digit string that signifies the layout of files on a hypothetical disk volume. Every other digit specifies the size of a file in blocks, and the digits inbetween specify how much space is between the blocks.

**Part 1** asks for the disk layout after moving blocks from the end into the gaps between files, allowing the moved files to be fragmented.

**Part 2** is the same, except that entire files must be moved, not just individual blocks.


## Solution Notes

This puzzle is mostly interesting in the sense that the two parts call for completely different data structures to get the most effective solution. For part 1, a simple map of each block on the disk, just like the ASCII printouts in the puzzle description, does the job perfectly. For part 2, two separate lists of extents for the files and the empty spaces are basically a requirement. Even with that, the solution can be quite slow, as the empty space list needs to be searched a lot. A substantially faster, albeit larger (but still somewhat golfable) solution is to further segregate the empty space list into bins for each block size. When looking for a place to move a file into, only the first positions for each of the 10 empty space bins need to be examined, instead of several thousands from a raw list. However, the remaining free space after a move operation must be inserted at the proper place in the target bin's list so that it stays sorted; this is where Python's `heapq` module shows that it _does_ in fact have a use outside of Dijkstra's algorithm ;)

* Part 1, Python: 195 bytes, <100 ms
* Part 2, Python (minimum size): 246 bytes, ~15 s
* Part 2, Python (speed-optimized): 335 bytes, <100 ms
