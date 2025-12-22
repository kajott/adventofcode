# [2023, Day 5: If You Give A Seed A Fertilizer](https://adventofcode.com/2023/day/5)

The input consists of (typically) 20 10-digit numbers of "seed IDs" and seven maps that map IDs from one namespace to the next. Each map consists of (typically) 10-50 triples of IDs. These triples specify a source ID range (start + length pair) and a destination starting ID.

**Part 1** asks for the minimum ID in the final namespace when mapping the seed IDs.

**Part 2** asks the same, but the seed IDs are interpreted as start + length pairs of entire ID ranges.


## Solution Notes

Part 1 is almost trivial: Run the numbers through the various maps, determine the minimum result, done.

Part 2 seems to be the same, but in a loop; however, the actual input data uses 9-digit ranges, so a more thoughtful approach is required. The basic idea is to run intervals through the maps, not single numbers. At every mapped range, the intervals are split if they intersect with the beginning or the end of the range, and the inner part is mapped according to the almanac. It's a bit finicky to get the conditions just right, and it requires a fair deal of `if`s and comparisons, but it's manageable.

But wait ... is it even true that a clever approach is a must-have and brute force iteration is a no-go? I estimated that a beefy top-of-the-line computer would need several hours on all cores to crunch through the ~2 billion iterations. Nevertheless, I was intrigued enough to actually implement a solution that's at the same time as dumb as possible, but also as efficient as possible: A Python script that translates the input into a C program that contains ~200 lines of the form `if ((n >= A) && (n < B)) { n = n - A + C; goto end_of_this_map; }` (with `A`, `B` and `C` substituted with the appropriate numbers), and a loop around it to find the minimum value of `n`. When running this, I quickly learned that my initial estimate was off by several orders of magnitude: It completes in about a minute on a single core! An iteration only takes between 100 and 200 CPU clock cycles on average (depending on the compiler, CPU microarchitecture, and whether Spectre/Meltdown mitigations are in effect). Indeed, this is about the most performance-optimal code for a modern CPU: It nicely fits into L1 cache, rarely accesses any other memory, and even though it's quite branchy, those branches are *very* consistent between iterations, making the branch predictor's job easier.

* Part 1, Python: 230 bytes, <100 ms
* Part 2, Python (interval processing): 423 bytes, <100 ms
* Part 2, Python-generated C code (brute force): ~70 s
