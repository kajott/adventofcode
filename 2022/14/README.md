# [2022, Day 14: Regolith Reservoir](https://adventofcode.com/2022/day/14)

The input consists of (typically) 140 polygons of 2 to 27 2-to-3-digit 2D coordinates. All lines in the polygons are either horizontal or vertical. Together, they define fixed obstacles in a 2D map.

The task is about simulating falling sand. Sand moves downwards if it can, down-right if it can't, down-left if even that path is blocked, and comes to rest if can go nowhere else.

**Part 1** asks how many units of sand come to rest before the first unit of sand starts running off the bottom of the map.

**Part 2** introduces a floor at a fixed height and asks how many units of sand come to rest until a certain point in the map is occupied by resting sand.


## Solution Notes

As the task description hints at, this is indeed a variant of [2018/17](../../2018/17), but fortunately a simplified one that can be solved without too much hassle.

I implemented the golf solutions with both complex numbers and tuples, and even though the input parser requires tuples and thus can't use the full potential of complex numbers, they're still a net win of a few bytes.

For part 2, a radically different approach can be used. Since the simulation is run until *every* grain of sand is resting, it is sufficient to just count the all the locations that the sand *can* reach. This, in turn, is quite simple: For each row of the map, the set of locations where sand can ultimately rest are the same as the set from the row above, _plus_ the same set moved one X step to the left, _plus_ one X step to the right, _minus_ (of course) the locations where there's rock. This way, the solution can be found with a single sweep across the map, in a negligible amount of time, and with even less code than part 1.

* Part 1, Python (complex numbers): 332 bytes, <100 ms
* Part 2, Python (complex numbers): 351 bytes, ~2 s
* Part 1, Python (coordinate tuples): 334 bytes, <100 ms
* Part 2, Python (coordinate tuples): 357 bytes, ~1.5 s
* Part 2, Python (sweep approach): 314 bytes, <100 ms
