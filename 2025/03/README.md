# 2025, Day 3: Lobby


## Solution Notes

Part 1 is easily solvable with a brute-force approach that finds the maximum of all O(n²) combinations. Nice.

Part 2 is one of the typical "what if we crank it up to eleven" (or twelve, in this case) scenarios, and it's a rare case where a classical greedy algorithm is actually the best approach: Select the first occurrence of highest digit of the number, add that digit to the result number, discard all digits up to and including it, and loop again until 12 digits have been collected. The critical point is that the highest digit search must stop at an appropriate point so that 12-digit numbers can still be produced. For example, the maximum search for the first result digit must ignore the last 11 digits of the input number, because otherwise it wouldn't be possible to still construct a 12-digit result. This approach is blazing fast and relatively short; conveniently, it even works on strings and characters that only need to be converted to actual numbers for the final summation.

But this wasn't my initial approach; first I tried with DFS and memoization, but this blew up with some numbers in my input, even after I added a few pruning optimizations. Again, it shows that using search algorithms for puzzles like these is a very fragile undertaking. With a few hints from a friend, I finally managed to get a DFS-based approach working a few hours later, but it's both larger and slower than the simple greedy approach. However, it's good for one thing: It makes it trivial to write a combined solution for parts 1 and 2 with almost no overhead.

I also revisited the nice greedy algorithm again later that day and ported it to x86 assembly and DOS, arriving at a 222-byte executable that runs in about 2 seconds on a 1981-era IBM PC 5150.

* Part 1, Python (brute force): 91 bytes, ~250 ms
* Part 2, Python (greedy algorithm): 151 bytes, <100 ms
* Part 2, Python (DFS+memoization): 191 bytes, ~300 ms
* Parts 1+2, Python (DFS+memoization): 205 bytes, ~300 ms
