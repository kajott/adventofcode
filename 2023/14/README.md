# 2023, Day 14: Parabolic Reflector Dish

You reach the place where all of the mirrors were pointing: a massive [parabolic reflector dish](https://en.wikipedia.org/wiki/Parabolic_reflector) attached to the side of another large mountain.

The dish is made up of many small mirrors, but while the mirrors themselves are roughly in the shape of a parabolic reflector dish, each individual mirror seems to be pointing in slightly the wrong direction. If the dish is meant to focus light, all it's doing right now is sending it in a vague direction.

This system must be what provides the energy for the lava! If you focus the reflector dish, maybe you can go where it's pointing and use the light to fix the lava production.

Upon closer inspection, the individual mirrors each appear to be connected via an elaborate system of ropes and pulleys to a large metal platform below the dish. The platform is covered in large rocks of various shapes. Depending on their position, the weight of the rocks deforms the platform, and the shape of the platform controls which ropes move and ultimately the focus of the dish.

## Part 1

In short: if you move the rocks, you can focus the dish. The platform even has a control panel on the side that lets you _tilt_ it in one of four directions! The rounded rocks (`O`) will roll when the platform is tilted, while the cube-shaped rocks (`#`) will stay in place. You note the positions of all of the empty spaces (`.`) and rocks (your puzzle input). For example:

    O....#....
    O.OO#....#
    .....##...
    OO.#O....O
    .O.....O#.
    O.#..O.#.#
    ..O..#O..O
    .......O..
    #....###..
    #OO..#....
    

Start by tilting the lever so all of the rocks will slide _north_ as far as they will go:

    OOOO.#.O..
    OO..#....#
    OO..O##..O
    O..#.OO...
    ........#.
    ..#....#.#
    ..O..#.O.O
    ..O.......
    #....###..
    #....#....
    

You notice that the support beams along the north side of the platform are _damaged_; to ensure the platform doesn't collapse, you should calculate the _total load_ on the north support beams.

The amount of load caused by a single rounded rock (`O`) is equal to the number of rows from the rock to the south edge of the platform, including the row the rock is on. (Cube-shaped rocks (`#`) don't contribute to load.) So, the amount of load caused by each rock in each row is as follows:

    OOOO.#.O.. 10
    OO..#....#  9
    OO..O##..O  8
    O..#.OO...  7
    ........#.  6
    ..#....#.#  5
    ..O..#.O.O  4
    ..O.......  3
    #....###..  2
    #....#....  1
    

The total load is the sum of the load caused by all of the _rounded rocks_. In this example, the total load is _`136`_.

Tilt the platform so that the rounded rocks all roll north. Afterward, _what is the total load on the north support beams?_

Your puzzle answer was `108813`.

## Part 2

The parabolic reflector dish deforms, but not in a way that focuses the beam. To do that, you'll need to move the rocks to the edges of the platform. Fortunately, a button on the side of the control panel labeled "_spin cycle_" attempts to do just that!

Each _cycle_ tilts the platform four times so that the rounded rocks roll _north_, then _west_, then _south_, then _east_. After each tilt, the rounded rocks roll as far as they can before the platform tilts in the next direction. After one cycle, the platform will have finished rolling the rounded rocks in those four directions in that order.

Here's what happens in the example above after each of the first few cycles:

    After 1 cycle:
    .....#....
    ....#...O#
    ...OO##...
    .OO#......
    .....OOO#.
    .O#...O#.#
    ....O#....
    ......OOOO
    #...O###..
    #..OO#....
    
    After 2 cycles:
    .....#....
    ....#...O#
    .....##...
    ..O#......
    .....OOO#.
    .O#...O#.#
    ....O#...O
    .......OOO
    #..OO###..
    #.OOO#...O
    
    After 3 cycles:
    .....#....
    ....#...O#
    .....##...
    ..O#......
    .....OOO#.
    .O#...O#.#
    ....O#...O
    .......OOO
    #...O###.O
    #.OOO#...O
    

This process should work if you leave it running long enough, but you're still worried about the north support beams. To make sure they'll survive for a while, you need to calculate the _total load_ on the north support beams after `1000000000` cycles.

In the above example, after `1000000000` cycles, the total load on the north support beams is _`64`_.

Run the spin cycle for `1000000000` cycles. Afterward, _what is the total load on the north support beams?_

Your puzzle answer was `104533`.

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
