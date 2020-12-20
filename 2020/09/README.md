# 2020, Day 9: Encoding Error

With your neighbor happily enjoying their video game, you turn your attention to an open data port on the little screen in the seat in front of you.

Though the port is non-standard, you manage to connect it to your computer through the clever use of several paperclips. Upon connection, the port outputs a series of numbers (your puzzle input).

The data appears to be encrypted with the eXchange-Masking Addition System (XMAS) which, conveniently for you, is an old cypher with an important weakness.

## Part 1

XMAS starts by transmitting a _preamble_ of 25 numbers. After that, each number you receive should be the sum of any two of the 25 immediately previous numbers. The two numbers will have different values, and there might be more than one such pair.

For example, suppose your preamble consists of the numbers `1` through `25` in a random order. To be valid, the next number must be the sum of two of those numbers:

*   `26` would be a _valid_ next number, as it could be `1` plus `25` (or many other pairs, like `2` and `24`).
*   `49` would be a _valid_ next number, as it is the sum of `24` and `25`.
*   `100` would _not_ be valid; no two of the previous 25 numbers sum to `100`.
*   `50` would also _not_ be valid; although `25` appears in the previous 25 numbers, the two numbers in the pair must be different.

Suppose the 26th number is `45`, and the first number (no longer an option, as it is more than 25 numbers ago) was `20`. Now, for the next number to be valid, there needs to be some pair of numbers among `1`\-`19`, `21`\-`25`, or `45` that add up to it:

*   `26` would still be a _valid_ next number, as `1` and `25` are still within the previous 25 numbers.
*   `65` would _not_ be valid, as no two of the available numbers sum to it.
*   `64` and `66` would both be _valid_, as they are the result of `19+45` and `21+45` respectively.

Here is a larger example which only considers the previous _5_ numbers (and has a preamble of length 5):

    35
    20
    15
    25
    47
    40
    62
    55
    65
    95
    102
    117
    150
    182
    127
    219
    299
    277
    309
    576
    

In this example, after the 5-number preamble, almost every number is the sum of two of the previous 5 numbers; the only number that does not follow this rule is _`127`_.

The first step of attacking the weakness in the XMAS data is to find the first number in the list (after the preamble) which is _not_ the sum of two of the 25 numbers before it. _What is the first number that does not have this property?_

Your puzzle answer was `18272118`.

## Part 2

The final step in breaking the XMAS encryption relies on the invalid number you just found: you must _find a contiguous set of at least two numbers_ in your list which sum to the invalid number from step 1.

Again consider the above example:

    35
    20
    15
    25
    47
    40
    62
    55
    65
    95
    102
    117
    150
    182
    127
    219
    299
    277
    309
    576
    

In this list, adding up all of the numbers from `15` through `40` produces the invalid number from step 1, `127`. (Of course, the contiguous set of numbers in your actual list might be much longer.)

To find the _encryption weakness_, add together the _smallest_ and _largest_ number in this contiguous range; in this example, these are `15` and `47`, producing _`62`_.

_What is the encryption weakness in your XMAS-encrypted list of numbers?_

Your puzzle answer was `2186361`.


## Solution Notes

The sheer number of combinations that need to be tested for a brute-force solution might sound high at first, but it's in fact much less than a million combinations in total, so even though we're dealing with O(n^3) here, it's not really an issue.

As the problem description already states, part 2 is (almost) a true superset of part 1. (In fact, a combined solution would just use an additional `print` statement.)

* Part 1, Python: 144 bytes, ~150 ms
* Part 2, Python: 227 bytes, ~250 ms
