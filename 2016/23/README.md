# [2016, Day 23: Safe Cracking](https://adventofcode.com/2016/day/23)


## Solution Notes

This puzzle is based on a very weird kind of self-modifying code that makes reverse-engineering harder than it needs to be. Unfortunately, understanding what the code does *is* required to solve part 2, because the problem size is almost 100k times as large as it was for part 1. In the end it turns out to compute <span style="color:silver;background:silver;">the factorials of 7 or 12</span>, plus a fixed offset that's encoded as two constants in the code<span style="color:silver;background:silver;">, multiplied together</span>. So the only sane way to solve part 2 is to grab these constants (it's generally the two largest numbers in the input code) and perform the computation on the host side.

* Part 1, Python: 367 bytes, <100 ms
* Part 2, Python: 100 bytes, <100 ms
