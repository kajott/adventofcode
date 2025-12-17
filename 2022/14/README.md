# 2022, Day 14: Regolith Reservoir


## Solution Notes

As the task description hints at, this is indeed a variant of [2018/17](../../2018/17), but fortunately a simplified one that can be solved without too much hassle.

I implemented the golf solutions with both complex numbers and tuples, and even though the input parser requires tuples and thus can't use the full potential of complex numbers, they're still a net win of a few bytes.

For part 2, a radically different approach can be used. Since the simulation is run until *every* grain of sand is resting, it is sufficient to just count the all the locations that the sand *can* reach. This, in turn, is quite simple: For each row of the map, the set of locations where sand can ultimately rest are the same as the set from the row above, _plus_ the same set moved one X step to the left, _plus_ one X step to the right, _minus_ (of course) the locations where there's rock. This way, the solution can be found with a single sweep across the map, in a negligible amount of time, and with even less code than part 1.

* Part 1, Python (complex numbers): 332 bytes, <100 ms
* Part 2, Python (complex numbers): 351 bytes, ~2 s
* Part 1, Python (coordinate tuples): 334 bytes, <100 ms
* Part 2, Python (coordinate tuples): 357 bytes, ~1.5 s
* Part 2, Python (sweep approach): 314 bytes, <100 ms
