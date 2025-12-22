# [2023, Day 14: Parabolic Reflector Dish](https://adventofcode.com/2023/day/14)

The input consists of a (typically) 100x100 grid, populated with two types of objects, movable and stationary.

**Part 1** asks for the positions of the movable objects after they have been moves as far upwards as possible, until they hit the edge or a stationary object.

**Part 2** asks for the positions of the movable objects after a billion "cycles", each consisting of moving the objects all the way up, then left, then down, then right.


## Solution Notes

A very interesting puzzle, because there are so many ways to implement it, with no clearly superior option.

My first approach was to read the map into a dictionary that only contains the obstacles (with every out-of-map position counting as an obstacle too), and a list or set that contains the positions of the rocks. I chose coordinate tuples first, because direct access to specific axes is required, which is always a bit cumbersome with complex numbers. The core function then simply moves each rock until it hits an obstacle or another "resting" rock. The order is important here: For a northward motion, rocks need to be processed in a north-to-south order, otherwise they might erroneously see other unprocessed rocks as obstacles.

Part 2 means storing the rock coordinates after each cycle in a suitable data structure, and once a constellation has been found again, the period can be extrapolated to a billion cycles using modulo arithmetic.

My first try at golfing the solutions took exactly that approach too. I started with part 2 and derived part 1 from that later on, stripping everything that's not needed. This even includes the sorting step, because the rock list is already pre-sorted in the proper order for northbound motion after importing the input data.

After finishing this, I wondered whether dismissing complex numbers was the right choice, and ported the solutions to use this representation. Surprisingly, even the frequent accesses to `.real` and `.imag` don't outweigh the savings of not having to manipulate two coordinate axes separately. It's only in part 1 where this approach shows its limits, because there, only one axis needs to be worked with, and the tuple approach is still a tiiiny bit shorter there.

Finally, a friend told me, half-jokingly, that a purely string-based approach that repeatedly replaces e.g. `O.` by `.O` for eastbound motion, combined with rotation of the entire map, would also work. We quickly agreed that this would certainly be slower than what I came up with before, but I wanted to know by how much, so I got to work writing another, this time completely different, implementation. To our great surprise, this approach turns out to work **extremely** well: It's twice as fast as the others, and it's even considerably shorter, at least for part 2! In part 1, the dual rotations hurt code size enough that it's not competitive with the other approaches, but it isn't far off either.

* Part 1, Python (coordinate tuples): 184 bytes, <100 ms
* Part 2, Python (coordinate tuples): 382 bytes, ~1 s
* Part 1, Python (complex numbers): 185 bytes, <100 ms
* Part 2, Python (complex numbers): 374 bytes, ~1.5 s
* Part 1, Python (string processing): 201 bytes, <100 ms
* Part 2, Python (string processing): 296 bytes, ~500 ms
