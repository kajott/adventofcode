# [2018, Day 15: Beverage Bandits](https://adventofcode.com/2018/day/15)


## Solution Notes

This is an extraordinarily complex and extremely frustrating puzzle. Not because it's hard to find a good algorithm (standard [A* search](https://en.wikipedia.org/wiki/A*_search_algorithm) will do the job fine), but because it's a lot of laborious work and because of the intricate rules that have to be followed to the letter. If even the slightest thing is a bit off, the simulation may diverge heavily from the reference. The provided test cases cover some of the fine points, but not all.

This time, I did not write the implementation in the usual code golf style; I needed much more expressiveness and debugging facilities to preserve my sanity. That's why there's a "non-golf" version here that even has some rudimentary visualization. The compact version has been ported from this, and even then it's over 1 kilobyte. Furthermore, it didn't make much sense to provide a separate solution for parts 1 and 2 here, as they would share 99% of the code; only the outer simulation loop would be slightly different.

* Parts 1+2, Python: 1071 bytes, ~20 s
