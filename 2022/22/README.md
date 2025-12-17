# [2022, Day 22: Monkey Map](https://adventofcode.com/2022/day/22)


## Solution Notes

Part 1 is just basic maze traversal code, with the only unusual thing being the odd shape of the maze and the resulting wrapping rules. The star of this show is very clearly part 2, and there are various approaches to take there.

The most obvious one is creating some mapping of the 2D cube net coordinates into the 3D space and then keeping track of the current coordinate in both 2D **and** 3D. I very briefly started doing that, but during 2D->3D map creation, I already noticed that the 3D vector math involved, while not technically very complicated, is still too hard to get exactly right (i.e. without any sign or axis swaps). There must be a better way.

Looking at the 2D net alone, it is clear that at concave corners (i.e. corners where three sides of the net meet), the adjacent edges belong together in 3D space. With that, it's easy to create some kind of "portal" list that maps one of these edges (and the facing direction) to the other, with an appropriately corrected direction. The question is what happens to the edges that are not directly adjacent to a corner. As it turns out, these can be joined with portals as well by simply continuing to "walk along" the edges. Walking starts at concave corners, and at each step, a pair of portals is created (in both directions) and the walk is continued. Walking stops when either side hits another concave corner, or if **both** sides hit a _convex_ (i.e. "outer") corner. This works fine for seven out of eleven possible cube nets; not perfect, but both the example net and the one from the actual input belong into the group that works, so it's good enough for our purposes.

The actual input's net is, in fact, identical for every user who took part in AoC. This means that it's absolutely fine to just hard-code the net, or rather, the resulting portals. My first attempt at this was indeed a bit smaller than the automatic code -- by a whole **two** (in numbers: 2) bytes! The coordinate data for the seven pairs of sides that span the net's circumference was large enough to cancel out almost all of the savings from the removed auto-portal code. It took several rounds of crunching to get the size down to something substantial. The end result of this is an encoding that contains the whole portal list in a single 168-bit number that's encoded in base 36 and decoded with Python's `int` function and a custom radix.

<details><summary><em>(expand this block to see what the data structure looks like)</em></summary>

The 168 bits are comprised of 84 two-bit values; six values for each of the 14 edges of the cube net. The edges, in turn, form seven pairs between which portals are going to be built. The values that define an edge are the following:

| Bits  | Description
|------:|:------
|  1:0  | coarse X start coordinate <br> _(block number; 0-3)_
|    2  | fine   X start coordinate <br> _(0 = left edge, 1 = right edge)_
|  5:4  | coarse Y start coordinate <br> _(block number; 0-3)_
|    6  | fine   Y start coordinate <br> _(0 = top edge, 1 = bottom edge)_
|  9:8  | direction of the edge <br> _(0-3; same encoding as "facing")_
| 11:10 | portal direction <br> _(portal source "facing" value)_

The coordinate encoding might seem a bit strange, but it helps in making the encoding more regular; as said, everything fits into two bits of data, which isn't possible for the "raw" coordinates. There are actually quite a few ways in which data could be saved: The fine coordinates are just 1 bit wide, leaving a gap in the encoding; also, the portal direction is always perpendicular to the edge direction, only the sign isn't clear. In total, it would be possible to save up to 42 bits (leaving 126 bits) if taken to the extreme, but that would require additional decoding logic, which in turn quickly eats up the benefits of a more sophisticated encoding.
</details><br>

* Part 1, Python: 356 bytes, <100 ms
* Part 2, Python (automatic portals): 649 bytes, ~150 ms
* Part 2, Python (hard-coded portals): 557 bytes, <100 ms
