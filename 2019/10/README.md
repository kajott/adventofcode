# [2019, Day 10: Monitoring Station](https://adventofcode.com/2019/day/10)

The input consists of a (typically) 36x36 grid, populated with objects.

**Part 1** asks to find the object from which the highest amount of other objects can be "seen" in direct line of sight. Visibility is blocked by other objects, i.e. if three objects are colinear, only the one at the center can see both others.

In **part 2**, objects are removed, one after another, in angular sweeps around the object selected in part 1. If multiple objects are in a line, only the closest one is removed during a sweep; further ones will only removed after an additional 360 degrees of rotation. The task asks for the coordinate of the 200th removed object.


## Solution Notes

This one is rather tough, because there's lots of ways in which subtle errors can creep in. The main ingredient for part 1 are reduced fractions, but I learned that the hard way after two unsuccessful attempts without them.

For part 2, my code constructs a sorted list of all possible angles that can be reached with integer coordinates in the desired range. This worked quite well -- after I fixed all the bugs in the angle list generation code, that is.

Part 2 has to contain a solver for part 1 by construction, and I used a different approach there that makes use of the angle list. It is substantially smaller (half the code size, not including the angle list generator itself), but very slow. In fact, my implementation spends almost all of its time computing the monitoring station location, and the asteroid zapping process is nearly instantaneous (less than 20 milliseconds).

* Part 1, Python: 371 bytes, ~1.5 s
* Part 2, Python: 575 bytes, ~7.5 s
* Part 2, Python (with visualization): 701 bytes, artificially slowed down to ~30 s
