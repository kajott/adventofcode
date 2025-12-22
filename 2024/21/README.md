# [2024, Day 21: Keypad Conundrum](https://adventofcode.com/2024/day/21)

The task simulates a keypad with ten number buttons, an Enter button, and a forbidden position in a 3x4 grid. The input contains (typically) 5 3-digit numbers (plus Enter) that shall be entered into this keypad.

The keypad may not be used directly, but only with a "cursor" that can be moved in the four cardinal directions plus a "press key" command.

This cursor, in turn, is controlled by _another_ 3x2-grid keypad, containing the four direction buttons, an Enter button, and a forbidden position.

The cursor may not be moved over the forbidden position.

**Parts 1 and 2** ask for the shortest possible sequence to enter the requested numbers in an arrangement of a numeric keypad controlled by **3** and **25** levels of nested directional keypads, respectively.


## Solution Notes

This puzzle has a lot of pitfalls that make it extra hard to solve (I took several hours and one full rewrite), but at its core, it's just a recursive search for the path through the keypad that enters a certain sequence with minimal input length on the _next_ keypad. Memoization is required for part 2, lest the search tree becomes too deep to be feasible without it, but that's in fact the only required change once the rest of the algorithm is sound. It's only about 50 lines of non-golf Python, but unfortunately it doesn't golf too well, coming in at about 500 bytes.

* Part 1, Python: 478 bytes, <100 ms
* Part 2, Python: 510 bytes, <100 ms
