# 2018, Day 14: Chocolate Charts


## Solution Notes

A rather straightforward puzzle. I implemented part 1 with Python lists, but switched to strings for part 2 to leverage the `str.find` function. The important thing here is to only search for the puzzle input at the *end* of the recipe; there's no point in searching through the whole string all over again, as the it doesn't ever change.

For fun (and because the Python version is rather slow), I also made a C implementation that's naturally around 50 times faster.

* Part 1, Python: 158 bytes, ~400 ms
* Part 2, Python: 177 bytes, ~20 s
* Part 2, C: 314 bytes, ~500 ms
