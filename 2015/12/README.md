# [2015, Day 12: JSAbacusFramework.io](https://adventofcode.com/2015/day/12)


## Solution Notes

Due to the constraints that are fulfilled by the JSON documents in question, part 1 can be solved by just adding all numbers in the file. Easy.

For part 2, however, full JSON parsing and document tree traversal is required. For golfing, I crammed the traversal function into a single line.

* Part 1, Python: 75 bytes, <100 ms
* Part 2, Python: 186 bytes, <100 ms
