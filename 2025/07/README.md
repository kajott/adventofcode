# [2025, Day 7: Laboratories](https://adventofcode.com/2025/day/7)


## Solution Notes

Part 1 is an easy starter. I initially used my trusty map of complex-number-indexed characters as a central data structure, and this worked fine, but it was slow and cumbersome. Since the ray only ever propagates downwards, all the extra geometry features provided by complex numbers aren't used and a simple iteration over the lines of the input file will do just fine (and is an order of a magnitude quicker even).

Many participants solved part 2 using DFS with memoization, but this approach seems overkill to me. I'd rather just iterate over the lines as in part 1 and keep track of how many possible scenarios would lead to a ray being present in each position. Initially, I did this with a dictionary, but later on it turned out that using a simple list is even shorter, despite having to deal with several boundary conditions.

* Part 1, Python: 145 bytes, <100 ms
* Part 2, Python (dictionary): 162 bytes, <100 ms
* Part 2, Python (list): 155 bytes, <100 ms
