# [2022, Day 19: Not Enough Minerals](https://adventofcode.com/2022/day/19)

The input consists of (typically) 30 "blueprints". Each blueprint describes the resource costs for four types of "robots": *Ore* robots cost some ore, *clay* robots cost some ore, *obsidian* robots cost some ore and some clay, *geode* robots cost some ore and some obsidian.

Each robot produces one item of its resource type per time unit. A scenario starts with 1 ore robot and nothing else. At each time step, existing resources can be used to build another robot of some type, which will then start producing its type of resources in the following time step. Only one robot can be built per time step. There can be any number of robots.

**Part 1** asks for the highest number of geodes that's possible to produce with each blueprint in 24 timesteps.

**Part 2** asks for the highest number of geodes that's possible to produce with the first three blueprints in **32** timesteps.


## Solution Notes

This is another graph search puzzle with very peculiar rules. I initially tried to solve this with DFS and memoization, but it's too slow on its own. Eventually, I switched over to BFS, which is not inherently faster, but allows for a few nice optimizations. And this is essentially what this puzzle is all about: Finding shortcuts to prune the search tree. The ones I used in the end are these:
- It's not needed to have a node for every minute of the simulation. Instead, it's possible to choose which robot to build next and advance the time by as many minutes as it takes to gather all the required resources with the current production capabilities.
- The only thing that consumes resources is building more robots, but only one robot can be built per time unit. So it doesn't make sense to have more mining robots for a specific resource than what's needed to built the most resource-consuming other robot. The mined material would just be wasted.
- Even under ideal circumstances, only one additional geode robot can be built per time unit, so for each examined state, there's an upper bound of geodes that can possibly be mined at the end of the simulation. If that number isn't higher than the current global maximum, it doesn't make sense to explore this state further.

With these implemented, I get to a large, but (just barely) acceptably fast solution. Parts 1 and 2 only differ in how the evualuation is performed, hence the code is very similar.

During golfing, a few sacrifices had to be made; the non-golf version is around 1.5x to 2x faster as a result. Out of curiosity, I also tried my hand at a C++ version (albeit using DFS, for simplicity reasons), and that's "only" 5x faster than the non-golf BFS version and requires 80 instead of 300 MB of RAM.

* Part 1, Python: 510 bytes, ~7 s
* Part 2, Python: 511 bytes, ~30 s
* Parts 1+2, C++ (non-golf): ~3.5 s
