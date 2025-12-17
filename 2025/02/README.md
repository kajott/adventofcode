# 2025, Day 2: Gift Shop


## Solution Notes

The task obviously calls for regular expressions (and hoping that the ranges aren't extremely large, which they fortunately aren't). However, I initially struggled to get the expressions just right and thus, I first hand-rolled a solution based on string comparisons that ran several seconds for part 2. Later, I finally found the regex-based solution, and what can you say, it not only runs much faster, it also makes the entire thing fit into a single line. The difference between parts 1 and 2 is just a single "`+`" in the expression.

Another few hours later, I came across a third approach for part 2: If the string of digits is duplicated (concatated to itself) and the original digits can be found there at any other position than the beginning or the end, it's eligible for summation. This implementation is even a bit shorter than the regex-based one, and it runs 2-3 times faster as well. This makes part 2 even less complex than part 1, for which a similar optimization exists, but is quite unsuitable for golfing.

* Part 1, Python: 152 bytes, ~1.5 s
* Part 2, Python (regular expressions): 153 bytes, ~2 s
* Part 2, Python (string maninpulation): 150 bytes, ~800 ms
