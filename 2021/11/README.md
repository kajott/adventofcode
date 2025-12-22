# [2021, Day 11: Dumbo Octopus](https://adventofcode.com/2021/day/11)

The input consists of a 10x10 grid of digits.

In each time step, each cell increases by 1. If a cell goes above 9, it "flashes" and increases the surrounding eight cells, possibly causing these to flash too. Finally, all cells that flashed are reset to zero.

**Part 1** asks for the total amount of flashes after 100 time steps.

**Part 2** asks for the first time step where all cells flash.


## Solution Notes

This puzzle is very similar to a cellular automaton simulation, except that the specific rules about what happens during a flash are a bit unconventional. My implementation uses a 2D array with a "guard band" that is generally ignored during the simulation.

The only difference between parts 1 and 2 is the abort criterion and what needs to be output at the end; the core simulation loop is identical.

* Part 1, Python: 321 bytes, <100 ms
* Part 2, Python: 321 bytes, <100 ms
