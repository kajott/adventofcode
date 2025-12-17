# [2021, Day 11: Dumbo Octopus](https://adventofcode.com/2021/day/11)


## Solution Notes

This puzzle is very similar to a cellular automaton simulation, except that the specific rules about what happens during a flash are a bit unconventional. My implementation uses a 2D array with a "guard band" that is generally ignored during the simulation.

The only difference between parts 1 and 2 is the abort criterion and what needs to be output at the end; the core simulation loop is identical.

* Part 1, Python: 321 bytes, <100 ms
* Part 2, Python: 321 bytes, <100 ms
