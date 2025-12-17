# 2018, Day 23: Experimental Emergency Teleportation


## Solution Notes

Part 2 took me countless attempts to get right. I tried octree subdivision first, to no avail. Then I tried a octahedron refinement algorithm. And a random refinement algorithm. Nothing worked. Even after I realized that my import code mixed the X,Y,Z,R parameters up and fixed that, only the random algorithm produced the correct result after a minute ... sometimes. Then I added an exhaustive search as a refinement on top of the random algorithm, and that finally gave me the correct result with good reproduceability. To my great surprise, it even does that when I start the full search with a more-or-less random point (like the center of gravity of all input points), even though it finds a different region with a less-than-maximal number of nearby bots, but identical distance to the origin. Yet that's enough to solve the puzzle, so that is what I used for the final golf implementation, also in part because that's by far the simplest code.

TL;DR: I didn't solve this puzzle properly, I just found a shortcut that works by accident. Rest assured that I **do** feel dirty, but looking at the Reddit threads about this puzzle, at least I'm in good company.

* Part 1, Python: 150 bytes, <100 ms
* Part 2, Python: 356 bytes, ~500 ms
