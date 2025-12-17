# [2021, Day 21: Dirac Dice](https://adventofcode.com/2021/day/21)


## Solution Notes

Part 1 is just a small and easy starter dish.

Part 2, however, is essentially impossible to solve with any straightforward algorithm. You just have to **know** that you're supposed to encode the game state as a 5D vector (with score and position of both players, and the current player ID) and implement a function that recursively explores the derivative game states, with caching for already visited states, returning a 2-tuple of winning universes for both players. This is _incredibly_ hard to come up with.

* Part 1, Python: 194 bytes, <100 ms
* Part 2, Python: 346 bytes, ~250 ms
