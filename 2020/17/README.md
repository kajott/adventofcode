# [2020, Day 17: Conway Cubes](https://adventofcode.com/2020/day/17)


## Solution Notes

This is a perfectly normal cellular automaton implementation -- except that it's in more than two dimensions. Choosing the proper data structure is important here; I opted for sets, which let me solve part 1 quite efficiently, and was trivially extensible for part 2. Runtime performance in part 2 could be better, but it's perfectly within acceptable limits.

* Part 1, Python: 328 bytes, <100 ms
* Part 2, Python: 357 bytes, ~1.5 s
