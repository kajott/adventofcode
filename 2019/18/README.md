# [2019, Day 18: Many-Worlds Interpretation](https://adventofcode.com/2019/day/18)

The input describes a (typically) 80x80 maze, visibly subdivided into four quadrants, with a marked starting position in the center. Scattered around the maze are 52 other marked spots, one lowercase and one uppercase for each letter. The uppercase marks can only be passed after the corresponding lowercase mark has been visited at least once.

**Part 1** asks for the shortest path that visits all the lowercase marks.

For **part 2**, the center area of the maze, which contains the starting position, is replaced by a pattern that segregates the quadrants from each other, turning the map into four independent mazes, each with their own starting position. In each time step, only one of the four positions can move, "unlocking" of uppercase marks still works across mazes.

**Part 2** asks for the shortest path that visits all the lowercase marks under these changed conditions.


## Solution Notes

I used a multi-step approach to solve these: First, build a full distance matrix between keys, plus metadata which other keys and doors are encountered along the path(s). Then, use that information to find the shortest way that gets all keys.

The first step is what took longest to get right. A straight BFS is not sufficient because of the doors: I don't just need the key-to-key distances, but also which keys are on the path between any two keys. If there's another door somewhere else in the maze that's not on the path between the two keys, I'm not interested in it, even if it might be located right next to the starting key. This is typically the domain of a DFS, but that's to slow on the (rather large) maze. In the end, I used a BFS variant that stores the "come-from" direction of every explored free field and use that to backtrack from every destination key, collecting doors and extra keys along the way.

The second step is classical DFS, but with a naive implementation, the runtime for more than approx. 10 keys is far too long. Caching already explored states helped to get the runtime down comfortably into the sub-second zone.

Based on that framework, part 2 of the puzzle isn't much of a problem. Step 1 doesn't change at all, and step 2 simply needs to track four current locations instead of just one.

* Part 1, Python: 666 bytes, ~300 ms
* Part 2, Python: 842 bytes, ~700 ms
