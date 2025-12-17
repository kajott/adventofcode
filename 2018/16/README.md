# [2018, Day 16: Chronal Classification](https://adventofcode.com/2018/day/16)


## Solution Notes

The puzzle itself is rather straightforward, but parsing the input and resolving the operations is slightly non-trivial, so I opted for a non-golf implementation first and derived the minimal programs from there. Still, they are relatively large, because the 16 `lambda`s that execute the instructions take up quite some space, especially since the full `lambda` and parameter specification must be repeated ever time.

* Part 1, Python: 631 bytes, <100 ms
* Part 2, Python: 812 bytes, <100 ms
