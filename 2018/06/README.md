# 2018, Day 6: Chronal Coordinates


## Solution Notes

If there is an elegant solution that doesn't require brute-force calculation of the minimum distance for all points on the plane, I didn't find it. The bounding box of all input points was small enough (300x300-ish) to make this just barely feasible though.

I used a neat little (though probably obvious) trick to detect the infinite-area sections: I process an additional extra row or column on each edge of the bounding box, and every unique nearest-point solution in this area is marked as being not eligible for the final result.

This is also one of the puzzles where part 2 is actually easier to implement (and compute) than part 1.

* Part 1, Python: 357 bytes, ~2 s
* Part 2, Python: 255 bytes, ~750 ms
