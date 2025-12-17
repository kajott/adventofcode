# 2016, Day 10: Balance Bots


## Solution Notes

The puzzle description is quite vague, but fortunately, there are no nasty pitfalls -- the puzzle just works as one would expect.

My implementation uses a shared "namespace" for bots and outputs; the latter simply have negative indices, which puts them at the end of the Python list I use to keep track of which bot currently has which chips.

* Part 1, Python: 320 bytes, <100 ms
* Part 2, Python: 336 bytes, <100 ms
