# [2022, Day 16: Proboscidea Volcanium](https://adventofcode.com/2022/day/16)


## Solution Notes

This is a tough one. It's essentially a graph searching puzzle where every possible move is a node, and can be tackled with Dijkstra's algorithm or DFS with memoization as usual; however, there are quite a few tiny details to get exactly right, lest the whole thing blows up in terms of computation power and memory usage.

For example, I included the projected flow rate into my DFS state - a bad idea. Later on, I temporarily switched to Dijkstra (because I thought that DFS is unviable due to my earlier failure with it), which worked beautifully for part 1, but for part 2, it generated wrong results on the example data and ran forever on the actual input. The reason: I included the time in my scoring function, whereas it should be part of the state instead. Computation still took 10 minutes though, and I didn't bother to clean up and golf that code as a result.

After getting a few hints from other contestants, I switched back to DFS with the "proper" set of states, and this does the trick indeed - it's relatively slow, but it's quite lean and it works.

For part 2, there is a pretty neat trick that helps to drastically reduce the complexity (in terms of code size, not necessarily runtime complexity): Instead of simulating both players at the same time, they can be serialized. Once player 1's time runs out, player 2 gets another 26 minutes of time to close the remaining valves. This enables a relatively compact DFS+memoization-based implementation.

It's still very slow though; a useful optimization is to run a BFS first to compute a distance matrix between all valves, like in [2019/18](../../2019/18). The main DFS can then use this data to perform movement and valve opening as one atomic operation, thus severely cutting down the number of graph nodes to search.

* Part 1, Python (DFS only): 340 bytes, ~2.5 s
* Part 2, Python (DFS only): 395 bytes, ~1.5 min
* Part 2, Python (BFS+DFS): 507 bytes, ~20 s
