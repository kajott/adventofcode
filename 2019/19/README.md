# 2019, Day 19: Tractor Beam

Unsure of the state of Santa's ship, you borrowed the tractor beam technology from Triton. Time to test it out.

When you're safely away from anything else, you activate the tractor beam, but nothing happens. It's hard to tell whether it's working if there's nothing to use it on. Fortunately, your ship's drone system can be configured to deploy a drone to specific coordinates and then check whether it's being pulled. There's even an [Intcode](../09) program (your puzzle input) that gives you access to the drone system.

## Part 1

The program uses two input instructions to request the _X and Y position_ to which the drone should be deployed. Negative numbers are invalid and will confuse the drone; all numbers should be _zero or positive_.

Then, the program will output whether the drone is _stationary_ (`0`) or _being pulled by something_ (`1`). For example, the coordinate X=`0`, Y=`0` is directly in front of the tractor beam emitter, so the drone control program will always report `1` at that location.

To better understand the tractor beam, it is important to _get a good picture_ of the beam itself. For example, suppose you scan the 10x10 grid of points closest to the emitter:

           X
      0->      9
     0#.........
     |.#........
     v..##......
      ...###....
      ....###...
    Y .....####.
      ......####
      ......####
      .......###
     9........##
    

In this example, the _number of points affected by the tractor beam_ in the 10x10 area closest to the emitter is _`27`_.

However, you'll need to scan a larger area to _understand the shape_ of the beam. _How many points are affected by the tractor beam in the 50x50 area closest to the emitter?_ (For each of X and Y, this will be `0` through `49`.)

Your puzzle answer was `160`.

## Part 2

You aren't sure how large Santa's ship is. You aren't even sure if you'll need to use this thing on Santa's ship, but it doesn't hurt to be prepared. You figure Santa's ship might fit in a _100x100_ square.

The beam gets wider as it travels away from the emitter; you'll need to be a minimum distance away to fit a square of that size into the beam fully. (Don't rotate the square; it should be aligned to the same axes as the drone grid.)

For example, suppose you have the following tractor beam readings:

    #.......................................
    .#......................................
    ..##....................................
    ...###..................................
    ....###.................................
    .....####...............................
    ......#####.............................
    ......######............................
    .......#######..........................
    ........########........................
    .........#########......................
    ..........#########.....................
    ...........##########...................
    ...........############.................
    ............############................
    .............#############..............
    ..............##############............
    ...............###############..........
    ................###############.........
    ................#################.......
    .................########XOOOOOOOOO.....
    ..................#######OOOOOOOOOO#....
    ...................######OOOOOOOOOO###..
    ....................#####OOOOOOOOOO#####
    .....................####OOOOOOOOOO#####
    .....................####OOOOOOOOOO#####
    ......................###OOOOOOOOOO#####
    .......................##OOOOOOOOOO#####
    ........................#OOOOOOOOOO#####
    .........................OOOOOOOOOO#####
    ..........................##############
    ..........................##############
    ...........................#############
    ............................############
    .............................###########
    

In this example, the _10x10_ square closest to the emitter that fits entirely within the tractor beam has been marked `O`. Within it, the point closest to the emitter (the `X`) is at X=`25`, Y=`20`.

Find the _100x100_ square closest to the emitter that fits entirely within the tractor beam; within that square, find the point closest to the emitter. _What value do you get if you take that point's X coordinate, multiply it by `10000`, then add the point's Y coordinate?_ (In the example above, this would be `250020`.)

Your puzzle answer was `9441282`.


## Solution Notes

Part 1 is well solvable with brute-force iteration, though the runtime is not optimal. The surprising part is that the Intcode VM needs a full restart (including re-initializing the memory) between each query; I assumed that it runs an endless loop that repeatedly queries coordinates instead, which cost me (and many other contestants) a few minutes of debugging.

For part 2, it's clear that brute force is no longer an option. Instead, the edges of the beam need to be traced somehow; I chose the upper edge, and try to find the lowest position for which both (X,Y) and (X-99,Y+99) are in the beam.

My initial approach (expecting the coordinates to be very large) was to compute the slope of the edge, so I have a good approximation of where the upper edge's Y is for any X. Then I did a coarse search for a working X with a large step size, followed by a fine search. This works and is really fast, but it has two caveats: First, the code is quite large. Second, there are situations where a 100x100 square can be found for X-1, but not for X, i.e. the "can a square be found" function is not monotonically increasing with X. This is bad if the coarse search lands at such a local minimum; that actually happened to me until I tweaked the search parameters accordingly.

Since the coordinates turned out to be not *that* large, I tried again with a much simpler approach: Just walk along the upper edge until the square fits. This is naturally much slower, but still bearable, and it's 42 bytes smaller, so I'm fine with that.

* Part 1, Python (brute force): 494 bytes, ~3.5 s
* Part 2, Python (fast search with slope estimation): 561 bytes, ~350 ms
* Part 2, Python (edge walking): 519 bytes, ~5 s
