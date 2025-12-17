# 2024, Day 12: Garden Groups


## Solution Notes

Isolating the several regions obivously calls for connected component analysis; so far, so simple. Determining the area is trivial too, but the perimeter is already the first pitfall: for getting the correct result even on non-convex regions or regions with holes in them, it's really required to count the neighbor tiles in all four directions _separately_. This took me a while to figure out, but it's quite obvious in hindsight, and the examples do a good job at exercising the possible corner cases.

Part 2 is making things even more complicated, but the solution for that isn't too far-fetched as well: We only need to count _distinct_ runs of neighbors for each direction &ndash; so we can basically run another connected component analysis for the neighbor tiles in each direction.

* Part 1, Python: 268 bytes, ~500 ms
* Part 2, Python: 325 bytes, ~300 ms
