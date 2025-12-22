# [2022, Day 10: Cathode-Ray Tube](https://adventofcode.com/2022/day/10)

The input consists of a sequence of (typically) 150 instructions for a virtual machine with only one register and two instructions: NOP, and add immediate. The immediates are signed 1-to-2-digit numbers. NOP takes 1 cycle, addition takes 2 cycles.

**Part 1** asks for the value of the register at certain cycles during one run of the program.

For part 2, a CRT that draws one pixel per cycle and 40 pixels per line is added to the machine. The register describes the position of a 3 pixels wide sprite that is to be drawn. If the CRT scans over one of the positions covered by the sprite, a dot is drawn.

**Part 2** asks for the letters that appear on the screen after one run of the program.


## Solution Notes

Implementing this task is not a problem at all, but figuring out the phases of the exact sampling points is. I (and, presumably, a lot of other people solving this problem) didn't even bother to fully understand the descriptions how it's supposed to be done, but simply tweaked phases until it was right.

* Part 1, Python: 127 bytes, <100 ms
* Part 2, Python: 164 bytes, <100 ms
