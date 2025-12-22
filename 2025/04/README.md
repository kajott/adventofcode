# [2025, Day 4: Printing Department](https://adventofcode.com/2025/day/4)

The input contains a (typically) 140x140 grid, densely populated with objects.

Objects can be removed if they have less than 4 neighboring objects in their 8 neighbor cells.

**Part 1** asks how many of the objects can be removed this way.

**Part 2** asks how many of the objects can be removed in total if the removal process is performed repeatedly until no more objects are eligible for removal.


## Solution Notes

A nice and simple task, very conveniently solvable with sets of complex numbers.
Part 2 is basically just running part 1 in a loop.

* Part 1, Python: 168 bytes, <100 ms
* Part 2, Python: 203 bytes, ~700 ms
