# 2019, Day 14: Space Stoichiometry


## Solution Notes

I was overthinking part 1 and thought that it would need some kind of decision tree search. In the end, it turned out to be much simpler than that: Just keep a tally of what resources are needed and how much, then pick a resource that's missing, execute the recipe for that and repeat. In the end, the amount of `ORE` resources that are required is what counts.

Part 2 seems to be a complete reversal of this generation process, but again, there's a short circuit: Just find out the correct number using binary search. And I mean that in the literal sense: The answer for part 2 is computed bit by bit, starting at the MSB.

* Part 1, Python: 314 bytes, <100 ms
* Part 2, Python: 377 bytes, <100 ms
