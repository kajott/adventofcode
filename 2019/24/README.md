# [2019, Day 24: Planet of Discord](https://adventofcode.com/2019/day/24)


## Solution Notes

Part 1 is just a garden variety cellular automaton simulation.

Part 2 adds an interesting extra twist. There are certainly more ways to solve it, but I chose to build a full "adjacency matrix" that specifies the neighbor fields for each of the 25 grid cells. The golfed code that computes this is the worst, unmaintainable mess I've ever written: it's a single 276-character line, exploiting operator precedence to the max to save on parentheses. I tried to replace this with a "compiled" version of the matrix, but that's even larger ...

* Part 1, Python: 269 bytes, <100 ms
* Part 2, Python: 551 bytes, ~600 ms
