# 2023, Day 16: The Floor Will Be Lava


## Solution Notes

Again a nice use case for sets of complex numbers. The most tedious part is getting the rules for the mirrors just right (_especially_ when doing golf), and also "survive" the small trap in the actual input where a mirror is placed right at the starting location. I didn't have any good ideas on how to optimize part 2, so it's just brute-forcing all (in my case) 440 possible starting constellations, making this a rather slow affair, but still well within tolerable limits.

* Part 1, Python: 356 bytes, <100 ms
* Part 2, Python: 466 bytes, ~10 s
