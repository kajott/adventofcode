# [2023, Day 16: The Floor Will Be Lava](https://adventofcode.com/2023/day/16)

The input consists of a (typically) 110x100 grid, sparsely populated with horizontal, vertical or diagonal marks.

The task is about an optical beam simulation. The diagonal marks represent mirrors, the horizontal and vertical marks represent beam splitters.

**Part 1** asks how many grid cells would have a beam in them if the initial beam started at the upper-left corner.

**Part 2** asks to find the initial beam position on the edges of the grid that maximizes the number of cells touched by the beam.


## Solution Notes

Again a nice use case for sets of complex numbers. The most tedious part is getting the rules for the mirrors just right (_especially_ when doing golf), and also "survive" the small trap in the actual input where a mirror is placed right at the starting location. I didn't have any good ideas on how to optimize part 2, so it's just brute-forcing all (in my case) 440 possible starting constellations, making this a rather slow affair, but still well within tolerable limits.

* Part 1, Python: 356 bytes, <100 ms
* Part 2, Python: 466 bytes, ~10 s
