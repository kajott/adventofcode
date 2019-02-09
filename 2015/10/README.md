# 2015, Day 10: Elves Look, Elves Say

Today, the Elves are playing a game called [look-and-say](https://en.wikipedia.org/wiki/Look-and-say_sequence). They take turns making sequences by reading aloud the previous sequence and using that reading as the next sequence. For example, `211` is read as "one two, two ones", which becomes `1221` (`1` `2`, `2` `1`s).

## Part 1

Look-and-say sequences are generated iteratively, using the previous value as input for the next step. For each step, take the previous value, and replace each run of digits (like `111`) with the number of digits (`3`) followed by the digit itself (`1`).

For example:

*   `1` becomes `11` (`1` copy of digit `1`).
*   `11` becomes `21` (`2` copies of digit `1`).
*   `21` becomes `1211` (one `2` followed by one `1`).
*   `1211` becomes `111221` (one `1`, one `2`, and two `1`s).
*   `111221` becomes `312211` (three `1`s, two `2`s, and one `1`).

Starting with the digits in your puzzle input, apply this process 40 times. What is _the length of the result_?

Your puzzle input was `1321131112`.

Your puzzle answer was `492982`.

## Part 2

Neat, right? You might also enjoy hearing [John Conway talking about this sequence](https://www.youtube.com/watch?v=ea7lJkEhytA) (that's Conway of _Conway's Game of Life_ fame).

Now, starting again with the digits in your puzzle input, apply this process _50_ times. What is _the length of the new result_?

Your puzzle input was still `1321131112`.

Your puzzle answer was `6989950`.


## Solution Notes

There are two basic ways to implement this: regular expressions (which is compact, but slow) and doing the Run-Length Encoding "by hand" (which is much longer, but also faster). For part 1, I used the former approach, and for part 2, the latter (and even then, it takes *really* long to compute). Both ways work for both parts of the puzzle though; just replace the constant `40` by `50` or vice-versa.

* Part 1, Python: 121 bytes, ~700 ms
* Part 2, Python: 133 bytes, ~6 s
