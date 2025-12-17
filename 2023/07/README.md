# 2023, Day 7: Camel Cards


## Solution Notes

Part 1 is just simplified Poker hand ranking, without suits and straights. The modified high-card tie-breaking rules are presumably in place to make part 2 a bit easier.

Part 2, too, doesn't bear any nasty surprises. Brute-force substitution of the jokers for all 13 possible cards is viable, since even the `JJJJJ` hand (which is, of course, part of the actual input data) only produces ~370k possible permutations. It took about one second to run through the completele input before I noticed a possible optimization: Instead of trying every possible card, it only makes sense to substitute cards that are part of the hand anyway, because any other card can only lower the precedence of the hand. This brings runtime back down into the unnoticeable range, and it's even tiny bit less code to boot, so I discarded the unoptimized version completely. (But if you're interested, that would be `range(15)` instead of `{*h}` in line 6.)

* Part 1, Python: 274 bytes, <100 ms
* Part 2, Python: 421 bytes, <100 ms
