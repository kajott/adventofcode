# 2024, Day 11: Plutonian Pebbles

The ancient civilization on [Pluto](../../2019/20) was known for its ability to manipulate spacetime, and while The Historians explore their infinite corridors, you've noticed a strange set of physics-defying stones.

## Part 1

At first glance, they seem like normal stones: they're arranged in a perfectly _straight line_, and each stone has a _number_ engraved on it.

The strange part is that every time you blink, the stones _change_.

Sometimes, the number engraved on a stone changes. Other times, a stone might _split in two_, causing all the other stones to shift over a bit to make room in their perfectly straight line.

As you observe them for a while, you find that the stones have a consistent behavior. Every time you blink, the stones each _simultaneously_ change according to the _first applicable rule_ in this list:

*   If the stone is engraved with the number `0`, it is replaced by a stone engraved with the number `1`.
*   If the stone is engraved with a number that has an _even_ number of digits, it is replaced by _two stones_. The left half of the digits are engraved on the new left stone, and the right half of the digits are engraved on the new right stone. (The new numbers don't keep extra leading zeroes: `1000` would become stones `10` and `0`.)
*   If none of the other rules apply, the stone is replaced by a new stone; the old stone's number _multiplied by 2024_ is engraved on the new stone.

No matter how the stones change, their _order is preserved_, and they stay on their perfectly straight line.

How will the stones evolve if you keep blinking at them? You take a note of the number engraved on each stone in the line (your puzzle input).

If you have an arrangement of five stones engraved with the numbers `0 1 10 99 999` and you blink once, the stones transform as follows:

*   The first stone, `0`, becomes a stone marked `1`.
*   The second stone, `1`, is multiplied by 2024 to become `2024`.
*   The third stone, `10`, is split into a stone marked `1` followed by a stone marked `0`.
*   The fourth stone, `99`, is split into two stones marked `9`.
*   The fifth stone, `999`, is replaced by a stone marked `2021976`.

So, after blinking once, your five stones would become an arrangement of seven stones engraved with the numbers `1 2024 1 0 9 9 2021976`.

Here is a longer example:

    Initial arrangement:
    125 17
    
    After 1 blink:
    253000 1 7
    
    After 2 blinks:
    253 0 2024 14168
    
    After 3 blinks:
    512072 1 20 24 28676032
    
    After 4 blinks:
    512 72 2024 2 0 2 4 2867 6032
    
    After 5 blinks:
    1036288 7 2 20 24 4048 1 4048 8096 28 67 60 32
    
    After 6 blinks:
    2097446912 14168 4048 2 0 2 4 40 48 2024 40 48 80 96 2 8 6 7 6 0 3 2

In this example, after blinking six times, you would have `22` stones. After blinking 25 times, you would have `_55312_` stones!

Consider the arrangement of stones in front of you. _How many stones will you have after blinking 25 times?_

Your puzzle answer was `193899`.

## Part 2

The Historians sure are taking a long time. To be fair, the infinite corridors _are_ very large.

_How many stones would you have after blinking a total of 75 times?_

Your puzzle answer was `229682160383225`.

## Solution Notes

Part 1 is perfectly solvable by straight simulation. No notes.

Part 2 is really the killer here. For fun, I let the simulation run for a few steps, but stopped it after 37 iterations, at which point it already consumed like 20 GB of memory. Seeing the final result, it's obvious that simulation can't be the solution here. Instead, there are _two_ completely different ways to solve part 2 in a useful manner.

One way is based on the observation that the order of the pebbles, contrary to what the task description says, doesn't matter at all. Every same-numbered pebble will behave the same, regardless of how many of them there are, so we can work efficiently by only keeping track of _distinct_ pebbles and their respective numbers of occurence (a.k.a. frequency). (Fun fact: there's never more than ~4000 distinct pebbles in use at any time for common inputs.)

The other way, which turned out to be even more compact, is based on the observation that each pebble evolves independently from all others: If it's known how much pebbles a pebble with number N evolves into after T blinks, this knowledge can be re-used if a pebble with number N occurs ever again, which it will definitely do. There are fancy names for that, which are "DFS with memoization" or "dynamic programming", but in Python terms, this boils down to using `functools.cache` on a function that answers the question "if a have a pebble of value N, how many pebbles will I have after T blinks" in a recursive manner. (Normally, I implement the caching by hand, but in this case, using the library one saved a bunch of bytes.)

By the way, it turned out to be consistently a ~~bit~~ byte smaller to keep the numbers as strings and only convert them to integers if needed.

* Part 1, Python: 179 bytes, ~350 ms
* Part 2, Python (type-and-frequency): 239 bytes, ~200 ms
* Part 2, Python (DFS + memoization): 230 bytes, ~200 ms