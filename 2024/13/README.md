# [2024, Day 13: Claw Contraption](https://adventofcode.com/2024/day/13)


## Solution Notes

There are a few red herrings in the task description: The maximum of 100 for A and B, for example, really only serves to minimize the search range for a brute-force solution and is otherwise of no significance. (The real input *does* check that the values can go up to 100 and don't stop at 99 though!) Another potential trap is that the question at the end of part 1 implies that there may be multiple ways to reach the target &ndash; but there aren't, and there can't be, as the entire thing is a linear system with 2 unknowns and 4 constraints, so it has to have a unique (though not necessarily integer) solution.

Part 1 is still solvable by brute-forcing through all 10k A/B combinations within the search range, part 2 obviously isn't. Instead, you really need to solve the linear system, and fail if any of the divisions in that process yield a remainder. That's obviously the much faster method, and it completes the task in no time at all.

* Part 1, Python: 182 bytes, ~1 s
* Part 2, Python: 210 bytes, <100 ms
