# 2015, Day 19: Medicine for Rudolph


## Solution Notes

The second part has the potential to be a major headache, and indeed a standard BFS approach blows up quite spectacularly. So imagine my surprise when I found out that even the dumbest DFS implementation works just fine! I actually added a greedy optimization later on to be a bit on the safe side in case my input was too optimistic, but there seems to be only a single input to begin with: I found the exact same input file in other people's repositories ...

* Part 1, Python: 275 bytes, <100 ms
* Part 2, Python (dumb DFS): 240 bytes, <100 ms
* Part 2, Python (greedy DFS): 281 bytes, <100 ms
