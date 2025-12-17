# 2020, Day 23: Crab Cups


## Solution Notes

Part 1 is very straightforward, but part 2 blows apart completely. Forget about vectors (a.k.a. Python lists). Forget about actual linked lists in C, even! The only structure that makes runtime performance somewhat manageable is a mapping from a cup number to the next one in clockwise order. With that in place, the puzzle becomes relatively easy to solve -- but it's a highly non-obvious solution, making this one of the more infuriating puzzles.

The Python version is pretty slow, even with all tricks in place. C is 25 times faster, and compilation time doesn't even matter much.

* Part 1, Python: 197 bytes, <100 ms
* Part 2, Python: 244 bytes, ~15 s
* Part 2, C: 387 bytes, ~600 ms
