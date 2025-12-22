# [2021, Day 7: The Treachery of Whales](https://adventofcode.com/2021/day/7)

The input consists of (typically) 1000 2-to-4-digit numbers, specifying the positions of objects ("crabs") in a line.

The goal is to move all these objects to the same position.

**Part 1** asks for the minimum number of moves to reach that goal.

**Part 2** asks for the minimum cost to reach the goal, except with a quadratic cost function.


## Solution Notes

A refreshingly simple and straightforward puzzle, easily solvable by two nested generator expressions.

* Part 1, Python: 104 bytes, ~150 ms
* Part 2, Python: 128 bytes, ~400 ms
