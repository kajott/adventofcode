# 2025, Day 12: Christmas Tree Farm

You're almost out of time, but there can't be much left to decorate. Although there are no stairs, elevators, escalators, tunnels, chutes, teleporters, firepoles, or conduits here that would take you deeper into the North Pole base, there _is_ a ventilation duct. You jump in.

After bumping around for a few minutes, you emerge into a large, well-lit cavern full of Christmas trees!

There are a few Elves here frantically decorating before the deadline. They think they'll be able to finish most of the work, but the one thing they're worried about is the _presents_ for all the young Elves that live here at the North Pole. It's an ancient tradition to put the presents under the trees, but the Elves are worried they won't _fit_.

The presents come in a few standard but very weird shapes. The shapes and the regions into which they need to fit are all measured in standard _units_. To be aesthetically pleasing, the presents need to be placed into the regions in a way that follows a standardized two-dimensional unit grid; you also can't stack presents.

## Part 1

As always, the Elves have a summary of the situation (your puzzle input) for you. First, it contains a list of the presents' shapes. Second, it contains the size of the region under each tree and a list of the number of presents of each shape that need to fit into that region. For example:

    0:
    ###
    ##.
    ##.
    
    1:
    ###
    ##.
    .##
    
    2:
    .##
    ###
    ##.
    
    3:
    ##.
    ###
    ##.
    
    4:
    ###
    #..
    ###
    
    5:
    ###
    .#.
    ###
    
    4x4: 0 0 0 0 2 0
    12x5: 1 0 1 0 2 2
    12x5: 1 0 1 0 3 2
    

The first section lists the standard present _shapes_. For convenience, each shape starts with its _index_ and a colon; then, the shape is displayed visually, where `#` is part of the shape and `.` is not.

The second section lists the _regions_ under the trees. Each line starts with the width and length of the region; `12x5` means the region is `12` units wide and `5` units long. The rest of the line describes the presents that need to fit into that region by listing the _quantity of each shape_ of present; `1 0 1 0 3 2` means you need to fit one present with shape index 0, no presents with shape index 1, one present with shape index 2, no presents with shape index 3, three presents with shape index 4, and two presents with shape index 5.

Presents can be _rotated and flipped_ as necessary to make them fit in the available space, but they have to always be placed perfectly on the grid. Shapes can't overlap (that is, the `#` part from two different presents can't go in the same place on the grid), but they _can_ fit together (that is, the `.` part in a present's shape's diagram does not block another present from occupying that space on the grid).

The Elves need to know _how many of the regions_ can fit the presents listed. In the above example, there are six unique present shapes and three regions that need checking.

The first region is 4x4:

    ....
    ....
    ....
    ....
    

In it, you need to determine whether you could fit two presents that have shape index `4`:

    ###
    #..
    ###
    

After some experimentation, it turns out that you _can_ fit both presents in this region. Here is one way to do it, using `A` to represent one present and `B` to represent the other:

    AAA.
    ABAB
    ABAB
    .BBB
    

The second region, `12x5: 1 0 1 0 2 2`, is `12` units wide and `5` units long. In that region, you need to try to fit one present with shape index `0`, one present with shape index `2`, two presents with shape index `4`, and two presents with shape index `5`.

It turns out that these presents _can_ all fit in this region. Here is one way to do it, again using different capital letters to represent all the required presents:

    ....AAAFFE.E
    .BBBAAFFFEEE
    DDDBAAFFCECE
    DBBB....CCC.
    DDD.....C.C.
    

The third region, `12x5: 1 0 1 0 3 2`, is the same size as the previous region; the only difference is that this region needs to fit one additional present with shape index `4`. Unfortunately, no matter how hard you try, there is _no way to fit all of the presents_ into this region.

So, in this example, _`2`_ regions can fit all of their listed presents.

Consider the regions beneath each tree and the presents the Elves would like to fit into each of them. _How many of the regions can fit all of the presents listed?_

Your puzzle answer was `499`.

## Part 2

The Elves thank you profusely for the help and start rearranging the oddly-shaped presents. As you look up, you notice that a lot more Elves have arrived here at the Christmas tree farm.

In fact, many of these new arrivals look _familiar_: they're the Elves you helped while decorating the North Pole base. Right on [schedule](1), each group seems to have brought a _star_ to put atop one of the Christmas trees!

Before any of them can find a ladder, a particularly large Christmas tree suddenly flashes brightly when a large _star_ magically appears above it! As your eyes readjust, you think you notice a portly man with a white beard disappear into the crowd.

You go look for a ladder; only _23 stars_ to go.


## Solution Notes

This task is just pure evil. You may be tempted to actually come up with an (already extraordinarily complicated) solution for the example, only to find that the actual input calls for grid sizes around 50x50, with several dozens of tiles per shape, and there's over 1000 of them. No way to solve this easily, and I doubt that there's a nice library to do that either. However, as it turns out that it's all just a ruse ...

<details>
<summary>Spoiler <em>(click to expand)</em></summary>
... and simply comparing the areas of the puzzle pieces and the target area is sufficient.
</details>
&nbsp;

* Part 1, Python: 198 bytes, <100 ms
