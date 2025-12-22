# [2020, Day 22: Crab Combat](https://adventofcode.com/2020/day/22)

The input describes the starting decks of two players in a card game. Each deck consists of 25 cards, numbered 1 to 50.

In each round, both players take the topmost cards from their stacks, compare them, and the player with the higher card gets both cards at the _bottom_ of their stacks.

**Part 1** asks to simulate the game until one player runs out of cards.

**Part 2** asks to simulate a **recursive** game: The topmost cards are drawn as usual, but if both players have at least as many cards remaining in their stack as the topmost card said (not counting the topmost card itself), the winner of the round is determined by playing a recursive game with a *copy* of as many cards from the stack as the topmost card said (again, not including the topmost card itself). If at least one player doesn't have enough cards, the old high-card rule applies. To prevent infinite loops, player 1 wins a game if exactly the same card configuration has appeared already.


## Solution Notes

This is another case where the rules simply need to be followed by the letter. A stupid bug cost me quite some debugging time in part 2, but that's the price you pay for writing directly in golf, in guess :)

* Part 1, Python: 217 bytes, <100 ms
* Part 2, Python: 358 bytes, ~2.5 s
