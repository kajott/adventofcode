# 2023, Day 18: Lavaduct Lagoon

Thanks to your efforts, the machine parts factory is one of the first factories up and running since the lavafall came back. However, to catch up with the large backlog of parts requests, the factory will also need a _large supply of lava_ for a while; the Elves have already started creating a large lagoon nearby for this purpose.

## Part 1

However, they aren't sure the lagoon will be big enough; they've asked you to take a look at the _dig plan_ (your puzzle input). For example:

    R 6 (#70c710)
    D 5 (#0dc571)
    L 2 (#5713f0)
    D 2 (#d2c081)
    R 2 (#59c680)
    D 2 (#411b91)
    L 5 (#8ceee2)
    U 2 (#caa173)
    L 1 (#1b58a2)
    U 2 (#caa171)
    R 2 (#7807d2)
    U 3 (#a77fa3)
    L 2 (#015232)
    U 2 (#7a21e3)
    

The digger starts in a 1 meter cube hole in the ground. They then dig the specified number of meters _up_ (`U`), _down_ (`D`), _left_ (`L`), or _right_ (`R`), clearing full 1 meter cubes as they go. The directions are given as seen from above, so if "up" were north, then "right" would be east, and so on. Each trench is also listed with _the color that the edge of the trench should be painted_ as an [RGB hexadecimal color code](https://en.wikipedia.org/wiki/RGB_color_model#Numeric_representations).

When viewed from above, the above example dig plan would result in the following loop of _trench_ (`#`) having been dug out from otherwise _ground-level terrain_ (`.`):

    #######
    #.....#
    ###...#
    ..#...#
    ..#...#
    ###.###
    #...#..
    ##..###
    .#....#
    .######
    

At this point, the trench could contain 38 cubic meters of lava. However, this is just the edge of the lagoon; the next step is to _dig out the interior_ so that it is one meter deep as well:

    #######
    #######
    #######
    ..#####
    ..#####
    #######
    #####..
    #######
    .######
    .######
    

Now, the lagoon can contain a much more respectable _`62`_ cubic meters of lava. While the interior is dug out, the edges are also painted according to the color codes in the dig plan.

The Elves are concerned the lagoon won't be large enough; if they follow their dig plan, _how many cubic meters of lava could it hold?_

Your puzzle answer was `42317`.

## Part 2

The Elves were right to be concerned; the planned lagoon would be _much too small_.

After a few minutes, someone realizes what happened; someone _swapped the color and instruction parameters_ when producing the dig plan. They don't have time to fix the bug; one of them asks if you can _extract the correct instructions_ from the hexadecimal codes.

Each hexadecimal code is _six hexadecimal digits_ long. The first five hexadecimal digits encode the _distance in meters_ as a five-digit hexadecimal number. The last hexadecimal digit encodes the _direction to dig_: `0` means `R`, `1` means `D`, `2` means `L`, and `3` means `U`.

So, in the above example, the hexadecimal codes can be converted into the true instructions:

*   `#70c710` = `R 461937`
*   `#0dc571` = `D 56407`
*   `#5713f0` = `R 356671`
*   `#d2c081` = `D 863240`
*   `#59c680` = `R 367720`
*   `#411b91` = `D 266681`
*   `#8ceee2` = `L 577262`
*   `#caa173` = `U 829975`
*   `#1b58a2` = `L 112010`
*   `#caa171` = `D 829975`
*   `#7807d2` = `L 491645`
*   `#a77fa3` = `U 686074`
*   `#015232` = `L 5411`
*   `#7a21e3` = `U 500254`

Digging out this loop and its interior produces a lagoon that can hold an impressive _`952408144115`_ cubic meters of lava.

Convert the hexadecimal color codes into the correct instructions; if the Elves follow this new dig plan, _how many cubic meters of lava could the lagoon hold?_

Your puzzle answer was `83605563360288`.

## Solution Notes

Part 1 can be solved using the same approach I took initially for [2023/10](../10): Use *three* sets of complex numbers, one for the main path and two for the left and right neighbor fields in order of traversal. Those are then used as seeds for a BFS-based flood fill algorithm; one of the seeds will spill outside the map, and the other eventually fills the entire loop. The sizes of the resulting sets is the answer. Easy.

For very obvious reasons, this doesn't work for part 2, at least not without modifications. After toying around a lot with scanline-based approaches which ultimately all failed, I went another route: Coordinate compression. All possible X and Y coordinates are collected and then mapped to smaller ones in increments of 2. The spaces inbetween are columns and rows of some inflated size that reflects the distance between the adjacent original coordinates. In other words, the huge grid is reduced to a much smaller grid with uneven weights, but that only matters for the final area computation; everything else can be done just as in part 1, except with tuples instead of complex numbers due to frequent component access.

A few hours later, I learned about another approach: using a combination of the [shoelace formula](https://en.wikipedia.org/wiki/Shoelace_formula) and [Pick's law](https://en.wikipedia.org/wiki/Pick%27s_theorem), it's possible to compute the resulting area directly from the polygon's vertex coordinates using almost trivial math. This approach is so ridiculously simple that the entire solution now fits into three lines, and it doesn't even flinch when confronted with part 2's huge coordinates. The solutions for parts 1 and 2 only differ in the parser, and part 1 even ends up being two bytes _larger_ than part 2 because the directions need to be looked up in a dictionary instead of being computable with a few simple formulas.

* Part 1, Python (BFS filling): 340 bytes, ~150 ms
* Part 2, Python (BFS filling + coordinate compression): 699 bytes, ~400 ms
* Part 1, Python (shoelace/Pick): 176 bytes, <100 ms
* Part 2, Python (shoelace/Pick): 174 bytes, <100 ms
