# [2024, Day 14: Restroom Redoubt](https://adventofcode.com/2024/day/14)


## Solution Notes

Part 1 is quite straightforward. It doesn't make much sense to even _try_ to implement a simulation-based approach, as it's quite obvious that the robot positions can be computed for any timestep using simple modular arithmetic. The quadrant rules are a bit strange, but easily manageable.

Part 2, then, hits like a truck. There's no specification whatsoever as to what the tree should look like, so no pattern to search for or anything. Contrary to the classic [Stars Align](../../2018/10) puzzle several years back, there's no obvious starting point. No, this puzzle requires coming up with several heuristics ... and I found three of them that work to various extents.

**Heuristic 1: Unique Positions** assumes that the input is constructed such that at the relevant time step, there's no spot covered by more than one robot (which turns out to be generally true), and that such a situation never occurs before &ndash; which turns out to be *not* the case for some users' inputs, but I was lucky. So it isn't the most general solution, but when it works, it works, and it's quite elegant as well: it requires even less code than part 1!

**Heuristic 2: Run of Adjacent Spots** assumes that the tree is filled, i.e. that there are a lot of covered spots close to each other. In particular, let's say there should be a run of ~10 horizontally adjacent spots, which is next to impossible at any other time step when the image is just noise. So we can just turn the playfield into a string at each time step and search for `#########`, and indeed that only happens at the requested time step. That method is the slowest of all, but it has a nice low-tech "whatever it takes" vibe to it. In fact, I've heard from people who solved the task by just dumping the playfield at each timestep into a giant text file and searching for such a run in an editor.

**Heuristic 3: Minimum Variance** also uses the assumption that the tree results in a compact cluster of covered spots, but it uses a more rigorous scientific/mathematical approach to detecting that &ndash; namely, it computes the variance of the covered positions in the first 101*103 = 10403 time steps finds the minimum there. Any variance metric will do here: I use standard variance without squaring and normalization, and adding the variances of the X and Y components, but it's been reported that using part 1's weird "safety factor" metric does the job too, if only because the tree isn't perfectly centered on the grid.

**Heuristic 4: Independent Axis Minimum Variance** takes the previous approach one step further by throwing even more maths at it. It's based on the observation that the X and Y axes are independent from each other (like in [another (in)famous past puzzle](../../2019/12)), and that the X coordinates of all robots repeat every 101 steps, while the Y coordinates repeat every 103 steps. This also means that the minimum variance states of these axes occur periodically at x0 + nx * 101 and y0 + ny * 103; the time where both coincide is the puzzle answer. So it's sufficient to find the X variance minimum for the first 101 steps and the Y variance minimum for the first 103 steps, and from there on it's all about modular arithmetics &ndash; or maybe not, because the factors are small enough that we can just try X minimum-variance step times until we find one that's also a valid Y minimum-variance step time. The end result is the largest implementation, but also the fastest one by quite some margin.

* Part 1, Python: 198 bytes, <100 ms
* Part 2, Python (Unique Positions): 178 bytes, ~1.5 s
* Part 2, Python (Run of Adjacent Spots): 222 bytes, ~15 s
* Part 2, Python (Minimum Variance): 235 bytes, ~2.5 s
* Part 2, Python (Independent Axis Minimum Variance): 265 bytes, <100 ms
