# 2016, Day 7: Internet Protocol Version 7


## Solution Notes

The heavy lifting for part 1 can be done with a regular expression containing backreferences; that doesn't work for part 2 though, as the matches can (and do) overlap. However, regular expressions aren't *fully* out of the equation either, because they're the most convenient way (that I can think of at the moment) to split the string into bracketed and non-bracketed sections.

* Part 1, Python: 147 bytes, <100 ms
* Part 2, Python: 208 bytes, <100 ms
