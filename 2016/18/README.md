# 2016, Day 18: Like a Rogue


## Solution Notes

A simple 1D cellular automaton (rule 90 or 165, depending on definition) with trivial boundary conditions that can be easily implemented in Python by adding a single "safe" block at the end of the row. (The boundary on the left side establishes itself as a result of Python's negative index semantics.) The iteration count in part 2 is low enough to make it solvable without cycle detection (though the result looks suspiciously like there *is* a cycle somewhere that could be exploited).

* Part 1, Python: 146 bytes, <100 ms
* Part 2, Python: 150 bytes, ~7 s
