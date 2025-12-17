# 2024, Day 18: RAM Run


## Solution Notes

This is a plain standard BFS maze search. Part 2 can be solved with brute-force iteration in an acceptable time, but the ideal (albeit larger) solution is of course doing a binary search for the first item in the sequence where the BFS can't reach the exit any longer.

* Part 1, Python: 251 bytes, <100 ms
* Part 2, Python (brute force): 262 bytes, ~10 s
* Part 2, Python (binary search): 317 bytes, <100 ms
