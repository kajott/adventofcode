# [2024, Day 11: Plutonian Pebbles](https://adventofcode.com/2024/day/11)


## Solution Notes

Part 1 is perfectly solvable by straight simulation. No notes.

Part 2 is really the killer here. For fun, I let the simulation run for a few steps, but stopped it after 37 iterations, at which point it already consumed like 20 GB of memory. Seeing the final result, it's obvious that simulation can't be the solution here. Instead, there are _two_ completely different ways to solve part 2 in a useful manner.

One way is based on the observation that the order of the pebbles, contrary to what the task description says, doesn't matter at all. Every same-numbered pebble will behave the same, regardless of how many of them there are, so we can work efficiently by only keeping track of _distinct_ pebbles and their respective numbers of occurence (a.k.a. frequency). (Fun fact: there's never more than ~4000 distinct pebbles in use at any time for common inputs.)

The other way, which turned out to be even more compact, is based on the observation that each pebble evolves independently from all others: If it's known how much pebbles a pebble with number N evolves into after T blinks, this knowledge can be re-used if a pebble with number N occurs ever again, which it will definitely do. There are fancy names for that, which are "DFS with memoization" or "dynamic programming", but in Python terms, this boils down to using `functools.cache` on a function that answers the question "if a have a pebble of value N, how many pebbles will I have after T blinks" in a recursive manner. (Normally, I implement the caching by hand, but in this case, using the library one saved a bunch of bytes.)

By the way, it turned out to be consistently a ~~bit~~ byte smaller to keep the numbers as strings and only convert them to integers if needed.

* Part 1, Python: 179 bytes, ~350 ms
* Part 2, Python (type-and-frequency): 239 bytes, ~200 ms
* Part 2, Python (DFS + memoization): 230 bytes, ~200 ms
