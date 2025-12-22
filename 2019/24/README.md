# [2019, Day 24: Planet of Discord](https://adventofcode.com/2019/day/24)

The input is a 5x5 grid populated with objects.

At each time step, existing objects are removed unless they have exactly one neighbor in the four cardinal directions, and a new object is created in a cell if it has exactly 1 or 2 neighbors.

**Part 1** asks for the first layout that repeats a previously-seen state.

For **part 2**, the the rules of the grid are changed. The center cell now contains another complete 5x5 grid, whose center cell again contains another grid, etc. The main grid itself is also just the center cell of another grid; the grids nest infinitely in both directions. Adjacency rules are unmodified, and all grids except the one with the input are initially empty.

**Part 2** asks for the number of objects in the recursive grid after 200 time steps.


## Solution Notes

Part 1 is just a garden variety cellular automaton simulation.

Part 2 adds an interesting extra twist. There are certainly more ways to solve it, but I chose to build a full "adjacency matrix" that specifies the neighbor fields for each of the 25 grid cells. The golfed code that computes this is the worst, unmaintainable mess I've ever written: it's a single 276-character line, exploiting operator precedence to the max to save on parentheses. I tried to replace this with a "compiled" version of the matrix, but that's even larger ...

* Part 1, Python: 269 bytes, <100 ms
* Part 2, Python: 551 bytes, ~600 ms
