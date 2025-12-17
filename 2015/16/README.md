# [2015, Day 16: Aunt Sue](https://adventofcode.com/2015/day/16)


## Solution Notes

A nice matching puzzle which can be solved with a single (but complex) set of nested generator expressions. Part 2 just replaces exact matching with sets. Bounded sets are sufficient, because object counts for the aunts rarely go into the double-digits, so "anything between `4` and `98`" is a good enough representation of "anything above `3`" here.

* Part 1, Python: 264 bytes, <100 ms
* Part 2, Python: 327 bytes, <100 ms
