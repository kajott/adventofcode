# 2016, Day 21: Scrambled Letters and Hash


## Solution Notes

Part 1 is unremarkable from the puzzle point of view, but quite interesting to make minimal.

Part 2 is not as hard as is first seems: Most operations are their own inverse, others are trivially reversible, only one (`rotate based on position of letter`) is a bit tricky. In the end, I implemented it using a fixed translation table based on the eight possible positions of the pivot element.

* Part 1, Python: 410 bytes, <100 ms
* Part 2, Python: 417 bytes, <100 ms
