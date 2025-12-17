# 2018, Day 10: The Stars Align


## Solution Notes

A quick glance at the inputs shows coordinates in the positive or negative 10000s and velocities in single-digit numbers with the same starting digit, but opposite sign, so it's fair to assume that the stars "converge" somewhere around the 10000 step mark. To find the exact point in time, I used a simple heuristic: assuming that the message is as compact as possible and every step before and after it has stars flying around outside of the message's display area, I simply had the code search for the time step where the bounding box of all stars has the minimal area. This works just fine and finds the exact solution in no time. The resulting bounding box (62x10) is small enough to allow for a simple ASCII-dot rendition of the final constellation on the console.

This puzzle is a little unusual in that the solution for part 2 is actually an interim result of part 1, so there's not even a separate implementation required for it.

* Parts 1+2, Python: 365 bytes, <100 ms
