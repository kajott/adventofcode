# 2020, Day 6: Custom Customs


## Solution Notes

One of the cases where you can see exactly what part 2 is going to be while working on part 1.

Again, parsing is the most involved aspect of the task, everything else is just set unions and intersections. A nice optimization for part 1 is that it's not even required to split the answers into individual persons -- the union can simply be done across all letters in a group, only discarding the newline characters.

* Part 1, Python: 77 bytes, <100 ms
* Part 2, Python: 133 bytes, <100 ms
