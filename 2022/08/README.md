# 2022, Day 8: Treetop Tree House


## Solution Notes

Following the instructions precisely is key here; the most notable detail that can be tricky to get right (and especially hard to golf properly) is that there are _two_ different stopping conditions for the visibility check and score computation loops: It has to stop *after* a large tree has been hit, but *before* the edge of the map.

* Part 1, Python: 220 bytes, <100 ms
* Part 2, Python: 224 bytes, <100 ms
