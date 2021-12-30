# 2021, Day 9: Smoke Basin

These caves seem to be [lava tubes](https://en.wikipedia.org/wiki/Lava_tube). Parts are even still volcanically active; small hydrothermal vents release smoke into the caves that slowly settles like rain.

If you can model how the smoke flows through the caves, you might be able to avoid it and be that much safer.

## Part 1

The submarine generates a heightmap of the floor of the nearby caves for you (your puzzle input).

Smoke flows to the lowest point of the area it's in. For example, consider the following heightmap:

    2199943210
    3987894921
    9856789892
    8767896789
    9899965678
    

Each number corresponds to the height of a particular location, where `9` is the highest and `0` is the lowest a location can be.

Your first goal is to find the _low points_ - the locations that are lower than any of its adjacent locations. Most locations have four adjacent locations (up, down, left, and right); locations on the edge or corner of the map have three or two adjacent locations, respectively. (Diagonal locations do not count as adjacent.)

In the above example, there are _four_ low points, all highlighted: two are in the first row (a `1` and a `0`), one is in the third row (a `5`), and one is in the bottom row (also a `5`). All other locations on the heightmap have some lower adjacent location, and so are not low points.

The _risk level_ of a low point is _1 plus its height_. In the above example, the risk levels of the low points are `2`, `1`, `6`, and `6`. The sum of the risk levels of all low points in the heightmap is therefore _`15`_.

Find all of the low points on your heightmap. _What is the sum of the risk levels of all low points on your heightmap?_

Your puzzle answer was `577`.

## Part 2

Next, you need to find the largest basins so you know what areas are most important to avoid.

A _basin_ is all locations that eventually flow downward to a single low point. Therefore, every low point has a basin, although some basins are very small. Locations of height `9` do not count as being in any basin, and all other locations will always be part of exactly one basin.

The _size_ of a basin is the number of locations within the basin, including the low point. The example above has four basins.

The top-left basin, size `3`. <br>
The top-right basin, size `9`. <br>
The middle basin, size `14`. <br>
The bottom-right basin, size `9`.

Find the three largest basins and multiply their sizes together. In the above example, this is `9 * 14 * 9 = `_`1134`_.

_What do you get if you multiply together the sizes of the three largest basins?_

Your puzzle answer was `1069200`.


## Solution Notes

For part 1, the task description already contains the implementation approach. For code golf, the usual "dictionary with complex numbers as keys" trick does the job admirably.

Part 2 adds an additional flood fill step to the mix, which I implemented by means of breadth-first search. After implementing that, I noticed that the BFS doesn't need to start at a low point; the whole idea of the flood fill is that the whole basin is filled, so the start location doesn't matter. Thus, instead of identifying low points first, a simple list of all open deeper-than-9 points in the map can be used.

* Part 1, Python: 185 bytes, <100 ms
* Part 2, Python (using low point seeds): 328 bytes, <100 ms
* Part 2, Python (using arbitrary seeds): 311 bytes, ~100 ms
