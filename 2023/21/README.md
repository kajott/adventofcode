# [2023, Day 21: Step Counter](https://adventofcode.com/2023/day/21)


## Solution Notes

Part 1 is almost trivial to solve with out best friend, the set of complex numbers. (For part 2, the switch to tuples had to be made to accomodate the required modulo operations for the obstacle coordinates.)

Part 2 is clearly another "find the cycle and extrapolate" kind of problem. In this case, the number of reachable spots for each time step modulo the maze size follows a quadratic progression. (It may not be immediately obvious why, but it actually makes sense: It's quadratic because it expands in area, and the period size is equal to the maze size, because what else could it be that makes the problem periodic?) So run the simulation, note the results for each time step that's 26501365 modulo the maze size until three samples have been found, and extrapolate the quadratic function. That's what my initial approach did.

The problem with this first attempt was runtime. While ~18 seconds isn't totally off the charts, it's still unwieldy. (I already sacrificed a whopping 3 bytes in order to avoid another 2x slowdown!) There needs to be something else that can be optimized, and of course there is! Not only is the problem periodic modulo the maze size, there's also a certain periodicity between odd and even time steps: At t+1, the reachable spots are going to be mostly the same as at t-1, except for a few extra spots on the periphery. This means that it's sufficient to simulate the "active edge" and ignore all interior spots, causing the runtime to drop dramatically, because instead of O(t^2) positions, only O(t) positions need to be evaluated. This optimization costs a few bytes (roughly 10% of the total size), but it's easily worth it.

* Part 1, Python: 191 bytes, <100 ms
* Part 2, Python (full simulation): 329 bytes, ~20 s
* Part 2, Python (edge only): 358 bytes, ~600 ms
