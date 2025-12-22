# [2023, Day 7: Camel Cards](https://adventofcode.com/2023/day/7)

The input consists of (typically) 1000 pairs of five Poker hands (i.e. five letters out of the set `23456789TJQKA`, in ascending order of value). Hands are categorized into the types "high card", "one pair", "two pairs", "three of a kind", "full house", "four of a kind" and "five of a kind", with increasing value. Every hand of a certain category wins against every hand of all lesser categories. Tie-breaking is done by checking the _first_ (*not* the highest!) card of a hand.

**Part 1** asks to rank all the hands in the input.

**Part 2** asks the same, but with the rules changed: `J` becomes a joker that can stand in for any card to get the best type of hand, but it's the weakest card during tie-breaking.


## Solution Notes

Part 1 is just simplified Poker hand ranking, without suits and straights. The modified high-card tie-breaking rules are presumably in place to make part 2 a bit easier.

Part 2, too, doesn't bear any nasty surprises. Brute-force substitution of the jokers for all 13 possible cards is viable, since even the `JJJJJ` hand (which is, of course, part of the actual input data) only produces ~370k possible permutations. It took about one second to run through the completele input before I noticed a possible optimization: Instead of trying every possible card, it only makes sense to substitute cards that are part of the hand anyway, because any other card can only lower the precedence of the hand. This brings runtime back down into the unnoticeable range, and it's even tiny bit less code to boot, so I discarded the unoptimized version completely. (But if you're interested, that would be `range(15)` instead of `{*h}` in line 6.)

* Part 1, Python: 274 bytes, <100 ms
* Part 2, Python: 421 bytes, <100 ms
