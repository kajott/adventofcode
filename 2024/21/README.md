# 2024, Day 21: Keypad Conundrum


## Solution Notes

This puzzle has a lot of pitfalls that make it extra hard to solve (I took several hours and one full rewrite), but at its core, it's just a recursive search for the path through the keypad that enters a certain sequence with minimal input length on the _next_ keypad. Memoization is required for part 2, lest the search tree becomes too deep to be feasible without it, but that's in fact the only required change once the rest of the algorithm is sound. It's only about 50 lines of non-golf Python, but unfortunately it doesn't golf too well, coming in at about 500 bytes.

* Part 1, Python: 478 bytes, <100 ms
* Part 2, Python: 510 bytes, <100 ms
