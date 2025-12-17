# 2024, Day 10: Hoof It


## Solution Notes

This is textbook example for a search algorithm, and specifically DFS due to its simplicity and because no path length optimization is required that would call for BFS. The "height must always increase by one" constraint also means that backwards steps are forbidden, eliminating the need to keep track of already visited positions. It's also once again a puzzle where part 2 is actually simpler than part 1, because it doesn't require counting _unique_ ending locations, but _any_ successful path through the map.

* Part 1, Python: 219 bytes, <100 ms
* Part 2, Python: 202 bytes, <100 ms
