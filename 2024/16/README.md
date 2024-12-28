# 2024, Day 16: Reindeer Maze

It's time again for the [Reindeer Olympics](../../2015/14)! This year, the big event is the _Reindeer Maze_, where the Reindeer compete for the _lowest score_.

You and The Historians arrive to search for the Chief right as the event is about to start. It wouldn't hurt to watch a little, right?

## Part 1

The Reindeer start on the Start Tile (marked `S`) facing _East_ and need to reach the End Tile (marked `E`). They can move forward one tile at a time (increasing their score by `1` point), but never into a wall (`#`). They can also rotate clockwise or counterclockwise 90 degrees at a time (increasing their score by `1000` points).

To figure out the best place to sit, you start by grabbing a map (your puzzle input) from a nearby kiosk. For example:

    ###############
    #.......#....E#
    #.#.###.#.###.#
    #.....#.#...#.#
    #.###.#####.#.#
    #.#.#.......#.#
    #.#.#####.###.#
    #...........#.#
    ###.#.#####.#.#
    #...#.....#.#.#
    #.#.#.###.#.#.#
    #.....#...#.#.#
    #.###.#.#.#.#.#
    #S..#.....#...#
    ###############

There are many paths through this maze, but taking any of the best paths would incur a score of only _`7036`_. This can be achieved by taking a total of `36` steps forward and turning 90 degrees a total of `7` times:

    
    ###############
    #.......#....E#
    #.#.###.#.###^#
    #.....#.#...#^#
    #.###.#####.#^#
    #.#.#.......#^#
    #.#.#####.###^#
    #..>>>>>>>>v#^#
    ###^#.#####v#^#
    #>>^#.....#v#^#
    #^#.#.###.#v#^#
    #^....#...#v#^#
    #^###.#.#.#v#^#
    #S..#.....#>>^#
    ###############

Here's a second example:

    #################
    #...#...#...#..E#
    #.#.#.#.#.#.#.#.#
    #.#.#.#...#...#.#
    #.#.#.#.###.#.#.#
    #...#.#.#.....#.#
    #.#.#.#.#.#####.#
    #.#...#.#.#.....#
    #.#.#####.#.###.#
    #.#.#.......#...#
    #.#.###.#####.###
    #.#.#...#.....#.#
    #.#.#.#####.###.#
    #.#.#.........#.#
    #.#.#.#########.#
    #S#.............#
    #################

In this maze, the best paths cost _`11048`_ points; following one such path would look like this:

    #################
    #...#...#...#..E#
    #.#.#.#.#.#.#.#^#
    #.#.#.#...#...#^#
    #.#.#.#.###.#.#^#
    #>>v#.#.#.....#^#
    #^#v#.#.#.#####^#
    #^#v..#.#.#>>>>^#
    #^#v#####.#^###.#
    #^#v#..>>>>^#...#
    #^#v###^#####.###
    #^#v#>>^#.....#.#
    #^#v#^#####.###.#
    #^#v#^........#.#
    #^#v#^#########.#
    #S#>>^..........#
    #################

Note that the path shown above includes one 90 degree turn as the very first move, rotating the Reindeer from facing East to facing North.

Analyze your map carefully. _What is the lowest score a Reindeer could possibly get?_

Your puzzle answer was `72428`.

## Part 2

Now that you know what the best paths look like, you can figure out the best spot to sit.

Every non-wall tile (`S`, `.`, or `E`) is equipped with places to sit along the edges of the tile. While determining which of these tiles would be the best spot to sit depends on a whole bunch of factors (how comfortable the seats are, how far away the bathrooms are, whether there's a pillar blocking your view, etc.), the most important factor is _whether the tile is on one of the best paths through the maze_. If you sit somewhere else, you'd miss all the action!

So, you'll need to determine which tiles are part of _any_ best path through the maze, including the `S` and `E` tiles.

In the first example, there are _`45`_ tiles (marked `O`) that are part of at least one of the various best paths through the maze:

    ###############
    #.......#....O#
    #.#.###.#.###O#
    #.....#.#...#O#
    #.###.#####.#O#
    #.#.#.......#O#
    #.#.#####.###O#
    #..OOOOOOOOO#O#
    ###O#O#####O#O#
    #OOO#O....#O#O#
    #O#O#O###.#O#O#
    #OOOOO#...#O#O#
    #O###.#.#.#O#O#
    #O..#.....#OOO#
    ###############

In the second example, there are _`64`_ tiles that are part of at least one of the best paths:

    #################
    #...#...#...#..O#
    #.#.#.#.#.#.#.#O#
    #.#.#.#...#...#O#
    #.#.#.#.###.#.#O#
    #OOO#.#.#.....#O#
    #O#O#.#.#.#####O#
    #O#O..#.#.#OOOOO#
    #O#O#####.#O###O#
    #O#O#..OOOOO#OOO#
    #O#O###O#####O###
    #O#O#OOO#..OOO#.#
    #O#O#O#####O###.#
    #O#O#OOOOOOO..#.#
    #O#O#O#########.#
    #O#OOO..........#
    #################

Analyze your map further. _How many tiles are part of at least one of the best paths through the maze?_

Your puzzle answer was `456`.

## Solution Notes

This is a nice twist for an otherwise unassuming pathfinding puzzle, but at the same time, it's extremely brutal. Coming up with a solution that works for the examples in part 1 is easy, but one that scales for the 20k-cell maze of the actual input is already challenging, and finding all the bugs and corner cases that are _not_ exercised in the examples can be a downright horror trip. In my case, it turns out that the order in which nodes are visited does matter: using a `set` for the unvisited states _sometimes_ doesn't work, it has to be a list. For part 2, it's crucial to have the "visited state" map not just keyed by the position, but the position _and direction_, otherwise the algorithm wouldn't find all optimal paths, only some.

The only nice thing here is that it's trivial to write a combined solution: Since part 1's result is a byproduct of computing part 2, it's more or less only a matter of an additional `print()` to output both.

* Part 1, Python: 276 bytes, ~2 s
* Part 2, Python: 347 bytes, ~3.5 s
* Parts 1+2, Python: 359 bytes, ~3.5 s
