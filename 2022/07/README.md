# [2022, Day 7: No Space Left On Device](https://adventofcode.com/2022/day/7)


## Solution Notes

This task is not a complicated one at all, but the devil's in the details and there are various ways to introduce subtle bugs.

What definitely helps is that the input is constructed in a non-malicious way; specifically, there's exactly one `cd /` at the beginning of the file (which means that it can be ignored completely, and `ls` is called exactly *once* for each directory. This means that a separate data structure that keeps track of "visited" directories is not necessary; we can just add all file sizes we encounter to their parent directories right during parsing.

I combined the solutions for both parts into a single file, because only the final `print` statement would be different between the individual parts' solutions.

* Parts 1+2, Python: 261 bytes, <100 ms
