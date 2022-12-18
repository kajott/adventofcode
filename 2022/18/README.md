# 2022, Day 18: Boiling Boulders

You and the elephants finally reach fresh air. You've emerged near the base of a large volcano that seems to be actively erupting! Fortunately, the lava seems to be flowing away from you and toward the ocean.

Bits of lava are still being ejected toward you, so you're sheltering in the cavern exit a little longer. Outside the cave, you can see the lava landing in a pond and hear it loudly hissing as it solidifies.

Depending on the specific compounds in the lava and speed at which it cools, it might be forming [obsidian](https://en.wikipedia.org/wiki/Obsidian)! The cooling rate should be based on the surface area of the lava droplets, so you take a quick scan of a droplet as it flies past you (your puzzle input).

## Part 1

Because of how quickly the lava is moving, the scan isn't very good; its resolution is quite low and, as a result, it approximates the shape of the lava droplet with _1x1x1 cubes on a 3D grid_, each given as its `x,y,z` position.

To approximate the surface area, count the number of sides of each cube that are not immediately connected to another cube. So, if your scan were only two adjacent cubes like `1,1,1` and `2,1,1`, each cube would have a single side covered and five sides exposed, a total surface area of _`10`_ sides.

Here's a larger example:

    2,2,2
    1,2,2
    3,2,2
    2,1,2
    2,3,2
    2,2,1
    2,2,3
    2,2,4
    2,2,6
    1,2,5
    3,2,5
    2,1,5
    2,3,5
    

In the above example, after counting up all the sides that aren't connected to another cube, the total surface area is _`64`_.

_What is the surface area of your scanned lava droplet?_

Your puzzle answer was `3390`.

## Part 2

Something seems off about your calculation. The cooling rate depends on exterior surface area, but your calculation also included the surface area of air pockets trapped in the lava droplet.

Instead, consider only cube sides that could be reached by the water and steam as the lava droplet tumbles into the pond. The steam will expand to reach as much as possible, completely displacing any air on the outside of the lava droplet but never expanding diagonally.

In the larger example above, exactly one cube of air is trapped within the lava droplet (at `2,2,5`), so the exterior surface area of the lava droplet is _`58`_.

_What is the exterior surface area of your scanned lava droplet?_

Your puzzle answer was `2058`.

## Solution Notes

This is a relatively easy task: Count how many of the eight neighbors of each block are air, and that's already it for part 1. Part 2 requires filling the space with (BFS-generated) "confirmed air" first, but is otherwise near-identical. The fact that the inputs only use a 20x20x20 grid is very helpful here - if the space was much larger, clusters of rock would need to be identified first in order to still be runtime-efficient.

* Part 1, Python: 153 bytes, <100 ms
* Part 2, Python: 295 bytes, ~150 ms
