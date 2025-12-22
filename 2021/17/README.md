# [2021, Day 17: Trick Shot](https://adventofcode.com/2021/day/17)

The input consists of the position of a rectangle in 2D space, with signed 2-to-3-digit coordinates.

The task is about simulating the motion of a thrown object, starting at the coordinate origin with a certain 2D integer velocity vector. Simulation is done in discrete time steps; at each step, the velocity is added to the position, and then the absolute value of the X component of the velocity is decreased by 1 (unless it's already zero), and the Y component of the velocity is decreased by 1. The object is supposed to hit somewhere within the rectangle at the end of a time step (i.e. it may "overshoot" it if the velocity is too high).

**Part 1** asks for the maximum Y position that could be reached with any trajectory that still hits the target rectangle.

**Part 2** asks how many distinct velocity vectors would hit the target rectangle.


## Solution Notes

The shot simulation part is quite simple, the question is how to guess valid initial velocities. Fortunately, the solution space is small enough that an exhaustive search over the full range is acceptable. For part 2, it's imperative that every possible solution is taken into account, including those with negative initial `y` velocities in general and direct shots at the lower-right corner of the target area in particular.

* Part 1, Python: 232 bytes, ~500 ms
* Part 2, Python: 216 bytes, ~1 s
* Part 1+2, Python: 250 bytes, ~1 s
