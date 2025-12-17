# 2022, Day 13: Distress Signal


## Solution Notes

Parsing the input is quite easy, because the lists are valid JSON and even Python and thus can be `eval`'d just fine. After that, the troubles start, as the comparison function must be written _exactly_ according to spec, and the example input doesn't even test all corner cases. This is overall a totally-not-fun task, but at least it isn't too complex.

For part 2, though, there is a very nice shortcut: The "divider" packets are always the first packets that start with a `2` and a `6`. Thus it isn't even necessary to fully parse the input; the first number on a line (and whether it's preceded by an empty list) is all that's needed. In the extreme, the whole code fits into a single line.

* Part 1, Python: 276 bytes, <100 ms
* Part 2, Python (with proper parsing and comparison): 264 bytes, <100 ms
* Part 2, Python (shortcut, list-based): 165 bytes, <100 ms
* Part 2, Python (shortcut, string-based): 137 bytes, <100 ms
