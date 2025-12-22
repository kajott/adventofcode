# [2019, Day 14: Space Stoichiometry](https://adventofcode.com/2019/day/14)

The input consists of (typically) 60 pseudo-chemical reaction equations, with up to 8 resources ("chemicals") with 1-to-2-digit numbers on the left, and a single resource with a 1-digit number on the right side. Resources are identified by random 5-letter strings. There's one specific resource that can be used to synthesize all others (indirectly), and one specific resource that is the production goal.

**Part 1** asks for the minimum amount of the input resource to produce one item of the output resource.

**Part 2** asks for the maximum amount of the output resource that can be produced with 10^12 items of the input resource.


## Solution Notes

I was overthinking part 1 and thought that it would need some kind of decision tree search. In the end, it turned out to be much simpler than that: Just keep a tally of what resources are needed and how much, then pick a resource that's missing, execute the recipe for that and repeat. In the end, the amount of `ORE` resources that are required is what counts.

Part 2 seems to be a complete reversal of this generation process, but again, there's a short circuit: Just find out the correct number using binary search. And I mean that in the literal sense: The answer for part 2 is computed bit by bit, starting at the MSB.

* Part 1, Python: 314 bytes, <100 ms
* Part 2, Python: 377 bytes, <100 ms
