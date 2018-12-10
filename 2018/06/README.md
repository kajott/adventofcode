# 2018, Day 6: Chronal Coordinates

The device on your wrist beeps several times, and once again you feel like you're falling.

"Situation critical," the device announces. "Destination indeterminate. Chronal interference detected. Please specify new target coordinates."

The device then produces a list of coordinates (your puzzle input). Are they places it thinks are safe or dangerous? It recommends you check manual page 729. The Elves did not give you a manual.

_If they're dangerous,_ maybe you can minimize the danger by finding the coordinate that gives the largest distance from the other points.

## Part 1

Using only the [Manhattan distance](https://en.wikipedia.org/wiki/Taxicab_geometry), determine the _area_ around each coordinate by counting the number of [integer](https://en.wikipedia.org/wiki/Integer) X,Y locations that are _closest_ to that coordinate (and aren't _tied in distance_ to any other coordinate).

Your goal is to find the size of the _largest area_ that isn't infinite. For example, consider the following list of coordinates:

    1, 1
    1, 6
    8, 3
    3, 4
    5, 5
    8, 9
    

If we name these coordinates `A` through `F`, we can draw them on a grid, putting `0,0` at the top left:

    ..........
    .A........
    ..........
    ........C.
    ...D......
    .....E....
    .B........
    ..........
    ..........
    ........F.
    

This view is partial - the actual grid extends infinitely in all directions. Using the Manhattan distance, each location's closest coordinate can be determined, shown here in lowercase:

    aaaaa.cccc
    aAaaa.cccc
    aaaddecccc
    aadddeccCc
    ..dDdeeccc
    bb.deEeecc
    bBb.eeee..
    bbb.eeefff
    bbb.eeffff
    bbb.ffffFf
    

Locations shown as `.` are equally far from two or more coordinates, and so they don't count as being closest to any.

In this example, the areas of coordinates A, B, C, and F are infinite - while not shown here, their areas extend forever outside the visible grid. However, the areas of coordinates D and E are finite: D is closest to 9 locations, and E is closest to 17 (both including the coordinate's location itself). Therefore, in this example, the size of the largest area is _17_.

_What is the size of the largest area_ that isn't infinite?

Your puzzle answer was `5975`.

## Part 2

On the other hand, _if the coordinates are safe_, maybe the best you can do is try to find a _region_ near as many coordinates as possible.

For example, suppose you want the sum of the [Manhattan distance](https://en.wikipedia.org/wiki/Taxicab_geometry) to all of the coordinates to be _less than 32_. For each location, add up the distances to all of the given coordinates; if the total of those distances is less than 32, that location is within the desired region. Using the same coordinates as above, the resulting region looks like this:

    ..........
    .A........
    ..........
    ...###..C.
    ..#D###...
    ..###E#...
    .B.###....
    ..........
    ..........
    ........F.
    

In particular, consider the highlighted location `4,3` located at the top middle of the region. Its calculation is as follows, where `abs()` is the [absolute value](https://en.wikipedia.org/wiki/Absolute_value) function:

*   Distance to coordinate A: `abs(4-1) + abs(3-1) =  5`
*   Distance to coordinate B: `abs(4-1) + abs(3-6) =  6`
*   Distance to coordinate C: `abs(4-8) + abs(3-3) =  4`
*   Distance to coordinate D: `abs(4-3) + abs(3-4) =  2`
*   Distance to coordinate E: `abs(4-5) + abs(3-5) =  3`
*   Distance to coordinate F: `abs(4-8) + abs(3-9) = 10`
*   Total distance: `5 + 6 + 4 + 2 + 3 + 10 = 30`

Because the total distance to all coordinates (`30`) is less than 32, the location is _within_ the region.

This region, which also includes coordinates D and E, has a total size of _16_.

Your actual region will need to be much larger than this example, though, instead including all locations with a total distance of less than _10000_.

_What is the size of the region containing all locations which have a total distance to all given coordinates of less than 10000?_

Your puzzle answer was `38670`.


## Solution Notes

If there is an elegant solution that doesn't require brute-force calculation of the minimum distance for all points on the plane, I didn't find it. The bounding box of all input points was small enough (300x300-ish) to make this just barely feasible though.

I used a neat little (though probably obvious) trick to detect the infinite-area sections: I process an additional extra row or column on each edge of the bounding box, and every unique nearest-point solution in this area is marked as being not eligible for the final result.

This is also one of the puzzles where part 2 is actually easier to implement (and compute) than part 1.

* Part 1, Python: 374 bytes, ~2 s
* Part 2, Python: 265 bytes, ~500 ms
