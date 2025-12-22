# [2019, Day 11: Space Police](https://adventofcode.com/2019/day/11)

This puzzle uses the Intcode virtual machine that has been fully specified in [day 9](../09), and which is going to be used a lot during AoC 2019.

The input for this task consists of an Intcode core dump of (typically) 660 words.

The program controls an agent that operates on an unbounded 2D binary grid initialized to all zeros. It starts at the origin, facing up. The program runs a loop that expects the current grid cell's state (`0`/`1`) as an input, outputs the new state of the grid cell, and outputs a binary turn instruction of 90 degrees, either left (`0`) or right (`1`). After each turn, the agent is supposed to move one cell forward.

**Part 1** asks how many cells the agent visited at least once after the program terminates.

**Part 2** asks for the letters that appear on the grid after running the program with the initial cell (and _only_ that one) initialized to `1` instead.


## Solution Notes

This puzzle puts the Intcode computer into "practical" use, and it's quite a fun thing indeed. The program of part 1 simply performs a few thousand iterations of a [Turmite](https://en.wikipedia.org/wiki/Turmite)-style cellular automaton; part 2 uses a rather complex algorithm to produce a simple 40x6-pixel bitmap.

* Part 1, Python: 499 bytes, ~500 ms
* Part 2, Python: 561 bytes, ~100 ms
