# [2020, Day 7: Handy Haversacks](https://adventofcode.com/2020/day/7)

The input consists of (typically) 600 descriptions which kind of "bags", identified by two-word color names, contain how many bags of other colors. There are be 0 to 4 other bag colors listed per bag, and 1 to 5 instances of each other-colored bag.

**Part 1** asks for how many different colors of bags contain a bag with one specific color.

**Part 2** asks for the total number of bags that a bag with that specific color contains.


## Solution Notes

Relatively simple topological reduction operations: Part 1 requires a set; part 2 requires a sum. Parsing and building data structures is again the main task here. For part 1, it makes sense to construct a reverse mapping from contained bags to containing bags, contrary to how the input rules are formulated.

* Part 1, Python: 202 bytes, <100 ms
* Part 2, Python: 212 bytes, <100 ms
