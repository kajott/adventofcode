# [2020, Day 6: Custom Customs](https://adventofcode.com/2020/day/6)

The input consists of (typically) 500 groups of 1 to 5 strings of 1 to 24 random letters each.

**Part 1** asks, for each group, how many different letters appear across all strings of the group.

**Part 2** asks, for each group, how many letters appear in every string of the group.


## Solution Notes

One of the cases where you can see exactly what part 2 is going to be while working on part 1.

Again, parsing is the most involved aspect of the task, everything else is just set unions and intersections. A nice optimization for part 1 is that it's not even required to split the answers into individual persons -- the union can simply be done across all letters in a group, only discarding the newline characters.

* Part 1, Python: 77 bytes, <100 ms
* Part 2, Python: 133 bytes, <100 ms
