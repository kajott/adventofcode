# [2019, Day 22: Slam Shuffle](https://adventofcode.com/2019/day/22)

The input consists of (typically) 100 instructions of how to shuffle a deck of initially ordered numbered cards.

There are three different shuffling instructions:
- `deal into new stack`: reverse the card order
- `cut N`: move `N` cards from to top to the bottom of the deck if `N` is positive, or from the bottom to the top if `N` is negative
- `deal with increment N`: re-arrange cards such that the card at index `i` in the stack is mapped to index `i*N` modulo the number of cards

**Part 1** asks for the position of card number 2019 after one round of shuffling a 10007-card deck with all the instructions from the input.

**Part 2** asks for the position of card number 2020 after 101,741,582,076,661 rounds of shuffling a deck of 119,315,717,514,047 cards.


## Solution Notes

Part 1 is nice and easy. After doing a simple full-deck simulation, I noticed that it's much easier to just track the position of card 2019.

Part 2 is where all that nasty modular arithmetic math comes into play. The key ingredient is to recognize that each shuffle operation corresponds to a simple `(a*x + b) mod N` transform: "cut" is addition, "deal with increment X" is multiplication by the [multiplicative inverse](https://en.wikipedia.org/wiki/Modular_multiplicative_inverse) of X modulo N &ndash; and "deal into new stack", it turns out, is basically `deal with increment N-1` followed by `cut 1`. Using this, it's possible to collapse the whole shuffle instruction list into a single `a,b` value pair. The effect of applying the whole transformation `p` times is then `(a*x + b)^p mod N`. It took me an eternity to figure out, but this can be computed by an extended implementation of [modular exponentiation](https://en.wikipedia.org/wiki/Modular_exponentiation), which takes O(log N) time. The result is a new `a,b` pair that can be applied to `x=2020` to get the final result.

My first implementation of part 2 builds the decomposition in reverse order, after a lot of trial-and-error iterations. Later, I found out that it's just as easy to generate the decomposition in forward order (in fact, that's what I tried to do first, but failed, and settled with reverse). This saves a few more bytes.

* Part 1, Python (full deck simulation): 208 bytes, ~100 ms
* Part 1, Python (single card tracing): 146 bytes, <100 ms
* Part 2, Python (reverse construction): 387 bytes, <100 ms
* Part 2, Python (forward construction): 337 bytes, <100 ms
