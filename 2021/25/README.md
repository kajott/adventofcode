# [2021, Day 25: Sea Cucumber](https://adventofcode.com/2021/day/25)

The input consists of a (typically) 140x140 grid, densely populated with objects ("sea cucumbers") moving either right (`>`) or down (`v`).

With each time step, all right-moving objects move first, followed by all downwards-moving objects. Objects wrap around the grid edges on both axes. If an object's target cell is occupied, it stays put.

The task asks for home many time steps it takes until all objects are deadlocked and won't move any longer.


## Solution Notes

This puzzle is technically a cellular automaton, or rather two of them, because each step is carried out in two phases with slightly different rules.

My first idea was to use sets to represent the object positions, which makes for a nice, albeit repetitive, implementation. That, however, turned out to be far too slow for the actual input, going far beyond the 1 minute mark.

So "conventional" 2D arrays it was, then. The specific rules for repetitions are quite delicate: avoiding double substitutions (i.e. moving an object that has already been moved in the same round) isn't as easy as it seems. I don't think for a second that my array-based solution is optimal in anyway, but it gets the job done.

That, however, made me think: What's a good way to apply these motion rules without having to worry about double substitutions? `str.replace` is! The vertical direction can easily be implemented by transposing, applying the rules horizontally, and transposing back. This approach worked perfectly, and is the smallest, fastest and most elegant I came up with.

* Part 1, Python (sets): 337 bytes, ~20 min
* Part 1, Python (2D array): 361 bytes, ~3 s
* Part 1, Python (strings): 181 bytes, ~350 ms
