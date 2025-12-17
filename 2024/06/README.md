# 2024, Day 6: Guard Gallivant


## Solution Notes

Part 1 is a fun exercise in utilizing the good old playfield-as-dictionary-indexed-by-complex-numbers approach, this time with a weirdly arranged coordinate system to make the initial direction constant shorter.

For part 2, there are two challenges: First, getting the loop check conditions exactly right, which is a bit finicky; and second, reducing the search space so runtime is acceptable. My very first approach tried to put an obstacle at every point of the maze (which has 130x130 elements in my case), but that took more than half a minute to compute. A straightforward way to reduce the search space is to only put obstacles where the guard's normal path (from part 1) was. This is only good for a ~3x reduction, but it's better than nothing, and allows for solving both parts with little more code than what's needed part 2 alone.

* Part 1, Python: 193 bytes, <100 ms
* Part 2, Python: 318 bytes, ~25 s
* Parts 1+2, Python: 350 bytes, ~25 s
