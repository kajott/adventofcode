# 2019, Day 4: Secure Container

You arrive at the Venus fuel depot only to discover it's protected by a password. The Elves had written the password on a sticky note, but someone threw it out.

## Part 1

However, they do remember a few key facts about the password:

*   It is a six-digit number.
*   The value is within the range given in your puzzle input.
*   Two adjacent digits are the same (like `22` in `1`_`22`_`345`).
*   Going from left to right, the digits _never decrease_; they only ever increase or stay the same (like `111123` or `135679`).

Other than the range rule, the following are true:

*   `111111` meets these criteria (double `11`, never decreases).
*   `2234`_`50`_ does not meet these criteria (decreasing pair of digits `50`).
*   `123789` does not meet these criteria (no double).

_How many different passwords_ within the range given in your puzzle input meet these criteria?

Your puzzle input was `158126-624574`.

Your puzzle answer was `1665`.

## Part 2

An Elf just remembered one more important detail: the two adjacent matching digits _are not part of a larger group of matching digits_.

Given this additional criterion, but still ignoring the range rule, the following are now true:

*   `112233` meets these criteria because the digits never decrease and all repeated digits are exactly two digits long.
*   `123`_`444`_ no longer meets the criteria (the repeated `44` is part of a larger group of `444`).
*   `111122` meets the criteria (even though `1` is repeated more than twice, it still contains a double `22`).

_How many different passwords_ within the range given in your puzzle input meet all of the criteria?

Your puzzle answer was `1131`.


## Solution Notes

A relatively simple task that is best done by converting the numbers to strings and operating on these. Minifying the code was quite fun, and I ended up with only minimally different oneliners for both parts, but that came at the expense of performance.

* Part 1, Python: 121 bytes, ~1 s
* Part 2, Python: 122 bytes, ~1 s
