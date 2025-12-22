# [2020, Day 23: Crab Cups](https://adventofcode.com/2020/day/23)

The input describes the initial order of 9 numbered objects ("cups") in a circular arrangement. The first of these objects is denoted as being "current".

In each time step, the three objects following (but not including) the current object are removed from the list and reinserted after the object with the current object's number minus 1. If the target object is in the set of removed objects, the target object number is decreased further until it points to an object that's still in the list. Decreasing wraps around.
Finally, the current object marker is moved to the next element in the list.

**Part 1** asks to simulate 100 time steps.

**Part 1** asks to simulate 10 million time steps.


## Solution Notes

Part 1 is very straightforward, but part 2 blows apart completely. Forget about vectors (a.k.a. Python lists). Forget about actual linked lists in C, even! The only structure that makes runtime performance somewhat manageable is a mapping from a cup number to the next one in clockwise order. With that in place, the puzzle becomes relatively easy to solve -- but it's a highly non-obvious solution, making this one of the more infuriating puzzles.

The Python version is pretty slow, even with all tricks in place. C is 25 times faster, and compilation time doesn't even matter much.

* Part 1, Python: 197 bytes, <100 ms
* Part 2, Python: 244 bytes, ~15 s
* Part 2, C: 387 bytes, ~600 ms
