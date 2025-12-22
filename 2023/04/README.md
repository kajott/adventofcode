# [2023, Day 4: Scratchcards](https://adventofcode.com/2023/day/4)

The input consists of (typically) 225 "cards" with 10 1-to-2-digit "winning" numbers on one side and another 25 such "drawn" numbers on the other.

**Part 1** asks for how many of the drawn numbers are in the set of winning numbers for each card.

For **part 2**, the rules are changed: if the are N matches in card K, additional copies of cards K+1 to K+N are created that can then, in turn, win additional cards. The task asks for the total number of cards in the stack after all these duplications.


## Solution Notes

Part 1 is quite easy and even makes for a nice, elegant one-liner. <br>
Part 2 may sound a bit intimidating at first and indeed contains a little trap, but that one's too obvious. Since all copies of a card behave identically, it's sufficient to manage exactly one copy of each card and only keep track of how many instances there are.

* Part 1, Python: 114 bytes, <100 ms
* Part 2, Python: 175 bytes, <100 ms
