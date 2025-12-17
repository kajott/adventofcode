# [2018, Day 12: Subterranean Sustainability](https://adventofcode.com/2018/day/12)


## Solution Notes

Part 1 is a straightforward cellular automaton simulation. A little care has to be taken about the boundary conditions, but nothing out of the ordinary.

Part 2 is a different beast altogether: The requested number of iterations is so absurdly high that it's unfeasible to simulate it, regardless of which algorithm you use. So there has to be a twist, and it becomes obvious when visualizing the patterns for each generations: It turns out that the rules of the cellular automaton are chosen such that after a few hundred generations, all that remains is a streak of a few populated spots that's constantly moving to the left or right. The solution is then to just extrapolate from that.

* Part 1, Python: 289 bytes, <100 ms
* Part 2, Python: 342 bytes, <100 ms
