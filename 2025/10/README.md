# [2025, Day 10: Factory](https://adventofcode.com/2025/day/10)


## Solution Notes

The two parts are completely different from each other.

Part 1 is an easy starter that calls for a bit of XOR magic, based on the realization that it never makes sense to push any of the buttons twice, as the results would cancel out. Brute-force checking of all combinations is a perfectly viable solution there.

This is not the case for part 2. I tried DFS with memoization, but that lead nowhere. Some people had success with clever searching approaches (I've seen a Dijkstra variant even), but those are excruciatingly slow too. No, there's exactly one proper way to solve this, and it's algebra.

Each line in the input describes a linear system of integers; most are underconstrained, others are overconstrained, and a few are perfectly square. Solving such a system purely in integers is technically an NP-complete problem; it's not surprising that most participants used a ready-made third-party solver like Z3 or SciPy's `optimize` sub-package. Admittedly, I did the same out of frustration, and it's indeed remarkable how compact and fast a solution based on that approach can be.

But it still feels like cheating. So I took another three(!) nights to solve the task "properly": a modified Gauss-Jordan algorithm that works on integers transforms the problem matrix into a (probably scaled) identity matrix with 0 to 3 extra columns tacked on at the right side. To resolve those, a simplex search could be used (which is likely what the solver libraries do), or a well-constrained brute force search. Since it's only up to 3 variables, and the ranges can be limited by computing the maximum amount of "button presses" until any of the "joltages" is exceeded, the resulting performance is absolutely fine.
The code size, however, isn't. It's almost certain that there are algorithmic optimizations with which I could get the size down and probably even break the kilobyte barrier, but since I already invested an inordinate amount of time on this entire endeavour, I didn't poke any further and just edited my non-golf approach down.

* Part 1, Python: 303 bytes, ~400 ms
* Part 2, Python (using SciPy): 240 bytes, ~600 ms
* Part 2, Python (handwritten algebra): 1046 bytes, ~1.5 s
