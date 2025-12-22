# [2022, Day 1: Calorie Counting](https://adventofcode.com/2022/day/1)

The input consists of (typically) 250 lists of 1 to 15 4-to-5-digit numbers.

**Part 1** asks for the maximum element sum of all lists.

**Part 2** asks for the maximum alement sum of the top-3 lists.


## Solution Notes

A nice and simple starter. The highest hurdle here is splitting the list into several sub-lists.

Just for fun, I also implemented a pure 16-bit DOS version, meant to run on the original IBM 5150 PC (albeit with at least 128k of RAM and DOS 2.0). The result is a 256-byte .COM-format program that reads `input.txt` and solves both parts in no time. On an emulated 5150, I measured around 2 seconds, _including_ the time it takes to load the program and data from floppy disk (which is very likely by far the largest part). <br>
The largest technical struggle in this implementation is the fact that everything requires 32-bit arithmetic, which needs to be performed in two halves on the 16-bit 8086/8088 CPU.

* Part 1, Python: 82 bytes, <100 ms
* Part 2, Python: 95 bytes, <100 ms
* Parts 1+2, x86 DOS Assembly: 256 bytes (assembled), ~2 s
