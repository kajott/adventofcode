# 2023, Day 23: A Long Walk

The Elves resume water filtering operations! Clean water starts flowing over the edge of Island Island.

They offer to help _you_ go over the edge of Island Island, too! Just hold on tight to one end of this impossibly long rope and they'll lower you down a safe distance from the massive waterfall you just created.

As you finally reach Snow Island, you see that the water isn't really reaching the ground: it's being _absorbed by the air_ itself. It looks like you'll finally have a little downtime while the moisture builds up to snow-producing levels. Snow Island is pretty scenic, even without any snow; why not take a walk?

## Part 1

There's a map of nearby hiking trails (your puzzle input) that indicates _paths_ (`.`), _forest_ (`#`), and steep _slopes_ (`^`, `>`, `v`, and `<`).

For example:

    #.#####################
    #.......#########...###
    #######.#########.#.###
    ###.....#.>.>.###.#.###
    ###v#####.#v#.###.#.###
    ###.>...#.#.#.....#...#
    ###v###.#.#.#########.#
    ###...#.#.#.......#...#
    #####.#.#.#######.#.###
    #.....#.#.#.......#...#
    #.#####.#.#.#########v#
    #.#...#...#...###...>.#
    #.#.#v#######v###.###v#
    #...#.>.#...>.>.#.###.#
    #####v#.#.###v#.#.###.#
    #.....#...#...#.#.#...#
    #.#########.###.#.#.###
    #...###...#...#...#.###
    ###.###.#.###v#####v###
    #...#...#.#.>.>.#.>.###
    #.###.###.#.###.#.#v###
    #.....###...###...#...#
    #####################.#
    

You're currently on the single path tile in the top row; your goal is to reach the single path tile in the bottom row. Because of all the mist from the waterfall, the slopes are probably quite _icy_; if you step onto a slope tile, your next step must be _downhill_ (in the direction the arrow is pointing). To make sure you have the most scenic hike possible, _never step onto the same tile twice_. What is the longest hike you can take?

In the example above, the longest hike you can take is marked with `O`, and your starting position is marked `S`:

    #S#####################
    #OOOOOOO#########...###
    #######O#########.#.###
    ###OOOOO#OOO>.###.#.###
    ###O#####O#O#.###.#.###
    ###OOOOO#O#O#.....#...#
    ###v###O#O#O#########.#
    ###...#O#O#OOOOOOO#...#
    #####.#O#O#######O#.###
    #.....#O#O#OOOOOOO#...#
    #.#####O#O#O#########v#
    #.#...#OOO#OOO###OOOOO#
    #.#.#v#######O###O###O#
    #...#.>.#...>OOO#O###O#
    #####v#.#.###v#O#O###O#
    #.....#...#...#O#O#OOO#
    #.#########.###O#O#O###
    #...###...#...#OOO#O###
    ###.###.#.###v#####O###
    #...#...#.#.>.>.#.>O###
    #.###.###.#.###.#.#O###
    #.....###...###...#OOO#
    #####################O#
    

This hike contains _`94`_ steps. (The other possible hikes you could have taken were `90`, `86`, `82`, `82`, and `74` steps long.)

Find the longest hike you can take through the hiking trails listed on your map. _How many steps long is the longest hike?_

Your puzzle answer was `2050`.

## Part 2

As you reach the trailhead, you realize that the ground isn't as slippery as you expected; you'll have _no problem_ climbing up the steep slopes.

Now, treat all _slopes_ as if they were normal _paths_ (`.`). You still want to make sure you have the most scenic hike possible, so continue to ensure that you _never step onto the same tile twice_. What is the longest hike you can take?

In the example above, this increases the longest hike to _`154`_ steps:

    #S#####################
    #OOOOOOO#########OOO###
    #######O#########O#O###
    ###OOOOO#.>OOO###O#O###
    ###O#####.#O#O###O#O###
    ###O>...#.#O#OOOOO#OOO#
    ###O###.#.#O#########O#
    ###OOO#.#.#OOOOOOO#OOO#
    #####O#.#.#######O#O###
    #OOOOO#.#.#OOOOOOO#OOO#
    #O#####.#.#O#########O#
    #O#OOO#...#OOO###...>O#
    #O#O#O#######O###.###O#
    #OOO#O>.#...>O>.#.###O#
    #####O#.#.###O#.#.###O#
    #OOOOO#...#OOO#.#.#OOO#
    #O#########O###.#.#O###
    #OOO###OOO#OOO#...#O###
    ###O###O#O###O#####O###
    #OOO#OOO#O#OOO>.#.>O###
    #O###O###O#O###.#.#O###
    #OOOOO###OOO###...#OOO#
    #####################O#
    

Find the longest hike you can take through the surprisingly dry hiking trails listed on your map. _How many steps long is the longest hike?_

Your puzzle answer was `6262`.

## Solution Notes

A very interesting twist on the standard pathfinding algorithms &ndash; but unfortunately, the Longest Path Problem is NP-hard, and it shows.

Due to the direction constraints, part 1 is perfectly manageable with a simple DFS; the only optimization required is that recursion must only happen at actual junctions, otherwise Python's recursion limit will hit.

Running the same DFS directly for part 2 is futile; it *will* eventually terminate, but at least in Python, it's *far* too slow to be acceptable. The problem needs to be simplified first, and this can be done by observing that there is only a relatively low number of junctions in the maze, and the distances between each junction can be pre-computed. The start and goal positions count as junctions too, and thus the resulting distance matrix is a weighted undirected graph:

![graph of my input with the longest path highlighted](graph.svg)

With this simplified representation, the final DFS becomes a little quicker: one minute instead of several hours. This is still too long to be _really_ practical, so I thought of another optimization: Instead of having an actual Python set of visited nodes, a bitfield of visited nodes is also possible. This can be constructed by mapping each junction / graph node to a power of two (which is easy, as there's only 36 nodes). This does indeed make things faster, but only by a factor of two. Python itself seems to be a limitation here, so I escalated one step further and made the Python code generate a small C program that contains the distance matrix in a long `switch`...`case` statement. With this, I get down to sub-second runtimes for everything from Python graph generation and C compilation to execution of the compiled program.

* Part 1, Python (direct maze DFS): 417 bytes, ~400 ms
* Part 2, Python (graph DFS using sets): 425 bytes, ~60 s
* Part 2, Python (graph DFS using bitfields): 503 bytes, ~35 s
* Part 2, Python (generating and running C code): 789 bytes, ~700 ms
