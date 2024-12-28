# 2024, Day 9: Disk Fragmenter

Another push of the button leaves you in the familiar hallways of some friendly [amphipods](../../2021/23)! Good thing you each somehow got your own personal mini submarine. The Historians jet away in search of the Chief, mostly by driving directly into walls.

While The Historians quickly figure out how to pilot these things, you notice an amphipod in the corner struggling with his computer. He's trying to make more contiguous free space by compacting all of the files, but his program isn't working; you offer to help.

## Part 1

He shows you the _disk map_ (your puzzle input) he's already generated. For example:

    2333133121414131402

The disk map uses a dense format to represent the layout of _files_ and _free space_ on the disk. The digits alternate between indicating the length of a file and the length of free space.

So, a disk map like `12345` would represent a one-block file, two blocks of free space, a three-block file, four blocks of free space, and then a five-block file. A disk map like `90909` would represent three nine-block files in a row (with no free space between them).

Each file on disk also has an _ID number_ based on the order of the files as they appear _before_ they are rearranged, starting with ID `0`. So, the disk map `12345` has three files: a one-block file with ID `0`, a three-block file with ID `1`, and a five-block file with ID `2`. Using one character for each block where digits are the file ID and `.` is free space, the disk map `12345` represents these individual blocks:

    0..111....22222

The first example above, `2333133121414131402`, represents these individual blocks:

    00...111...2...333.44.5555.6666.777.888899

The amphipod would like to _move file blocks one at a time_ from the end of the disk to the leftmost free space block (until there are no gaps remaining between file blocks). For the disk map `12345`, the process looks like this:

    0..111....22222
    02.111....2222.
    022111....222..
    0221112...22...
    02211122..2....
    022111222......

The first example requires a few more steps:

    00...111...2...333.44.5555.6666.777.888899
    009..111...2...333.44.5555.6666.777.88889.
    0099.111...2...333.44.5555.6666.777.8888..
    00998111...2...333.44.5555.6666.777.888...
    009981118..2...333.44.5555.6666.777.88....
    0099811188.2...333.44.5555.6666.777.8.....
    009981118882...333.44.5555.6666.777.......
    0099811188827..333.44.5555.6666.77........
    00998111888277.333.44.5555.6666.7.........
    009981118882777333.44.5555.6666...........
    009981118882777333644.5555.666............
    00998111888277733364465555.66.............
    0099811188827773336446555566..............

The final step of this file-compacting process is to update the _filesystem checksum_. To calculate the checksum, add up the result of multiplying each of these blocks' position with the file ID number it contains. The leftmost block is in position `0`. If a block contains free space, skip it instead.

Continuing the first example, the first few blocks' position multiplied by its file ID number are `0 * 0 = 0`, `1 * 0 = 0`, `2 * 9 = 18`, `3 * 9 = 27`, `4 * 8 = 32`, and so on. In this example, the checksum is the sum of these, _`1928`_.

Compact the amphipod's hard drive using the process he requested. _What is the resulting filesystem checksum?_ (Be careful copy/pasting the input for this puzzle; it is a single, very long line.)

Your puzzle answer was `6399153661894`.

## Part 2

Upon completion, two things immediately become clear. First, the disk definitely has a lot more contiguous free space, just like the amphipod hoped. Second, the computer is running much more slowly! Maybe introducing all of that [file system fragmentation](https://en.wikipedia.org/wiki/File_system_fragmentation) was a bad idea?

The eager amphipod already has a new plan: rather than move individual blocks, he'd like to try compacting the files on his disk by moving _whole files_ instead.

This time, attempt to move whole files to the leftmost span of free space blocks that could fit the file. Attempt to move each file exactly once in order of _decreasing file ID number_ starting with the file with the highest file ID number. If there is no span of free space to the left of a file that is large enough to fit the file, the file does not move.

The first example from above now proceeds differently:

    00...111...2...333.44.5555.6666.777.888899
    0099.111...2...333.44.5555.6666.777.8888..
    0099.1117772...333.44.5555.6666.....8888..
    0099.111777244.333....5555.6666.....8888..
    00992111777.44.333....5555.6666.....8888..

The process of updating the filesystem checksum is the same; now, this example's checksum would be _`2858`_.

Start over, now compacting the amphipod's hard drive using this new method instead. _What is the resulting filesystem checksum?_

Your puzzle answer was `6421724645083`.

## Solution Notes

This puzzle is mostly interesting in the sense that the two parts call for completely different data structures to get the most effective solution. For part 1, a simple map of each block on the disk, just like the ASCII printouts in the puzzle description, does the job perfectly. For part 2, two separate lists of extents for the files and the empty spaces are basically a requirement. Even with that, the solution can be quite slow, as the empty space list needs to be searched a lot. A substantially faster, albeit larger (but still somewhat golfable) solution is to further segregate the empty space list into bins for each block size. When looking for a place to move a file into, only the first positions for each of the 10 empty space bins need to be examined, instead of several thousands from a raw list. However, the remaining free space after a move operation must be inserted at the proper place in the target bin's list so that it stays sorted; this is where Python's `heapq` module shows that it _does_ in fact have a use outside of Dijkstra's algorithm ;)

* Part 1, Python: 195 bytes, <100 ms
* Part 2, Python (minimum size): 246 bytes, ~15 s
* Part 2, Python (speed-optimized): 335 bytes, <100 ms
