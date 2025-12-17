# 2023, Day 11: Cosmic Expansion


## Solution Notes

For part 1, actually duplicating the affected rows and columns in the map data is feasible; for part 2, though, it's obviously not. There, a sensible approach is building a translation table from raw map coordinates into expanded coordinates, separately for each dimension. To my surprise, this method even saved a few extra bytes on part 1!

* Part 1, Python (duplicating rows and columns): 310 bytes, <100 ms
* Part 1, Python (coordinate translation): 307 bytes, <100 ms
* Part 2, Python (coordinate translation): 315 bytes, <100 ms
