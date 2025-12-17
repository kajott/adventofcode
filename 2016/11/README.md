# 2016, Day 11: Radioisotope Thermoelectric Generators


## Solution Notes

It's pretty obvious that the task of the puzzle is to implement a breadth-first search on the tree of possible moves; the complicated part is how to make it fast enough to be bearable. The bare minimum is recognition of already visited states to avoid cycles. With that, the Python solution runs in a barely acceptable timeframe for part 1, but part 2 with its 256-fold increase in problem size becomes unfeasible. So I turned to C, shoved the whole state into 32-bit words, used a full bitmap for tracking visited states, and arrived at a barely acceptable runtime for part 2.

But there's more. Reading the discussions at Reddit, I noticed that I missed another very important optimization: The order of the elements doesn't matter. In the example, the names of hydrogen and lithium could be swapped at any point without changing the outcome. As a result, if a state has been visited, the states with all permutations of element names also count as visited. In my solution, I implemented this by bringing every new state into a canonical order by sorting the generator-chip pairs by floor numbers. With that, the Python code for part 2 comfortably outperforms the C code (which doesn't use canonicalization).

* Part 1, Python (without canonicalization): 640 bytes, ~15 s
* Part 1, C (non-golf, without canonicalization): ~300 ms
* Part 2, C (non-golf, without canonicalization): ~25 s
* Part 2, Python (with canonicalization): 701 bytes, ~6 s
