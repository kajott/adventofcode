# 2025, Day 3: Lobby

You descend a short staircase, enter the surprisingly vast lobby, and are quickly cleared by the security checkpoint. When you get to the main elevators, however, you discover that each one has a red light above it: they're all _offline_.

"Sorry about that," an Elf apologizes as she tinkers with a nearby control panel. "Some kind of electrical surge seems to have fried them. I'll try to get them online soon."

You explain your need to get further underground. "Well, you could at least take the escalator down to the printing department, not that you'd get much further than that without the elevators working. That is, you could if the escalator weren't also offline."

"But, don't worry! It's not fried; it just needs power. Maybe you can get it running while I keep working on the elevators."

## Part 1

There are batteries nearby that can supply emergency power to the escalator for just such an occasion. The batteries are each labeled with their [joltage](/2020/day/10) rating, a value from `1` to `9`. You make a note of their joltage ratings (your puzzle input). For example:

    987654321111111
    811111111111119
    234234234234278
    818181911112111
    

The batteries are arranged into _banks_; each line of digits in your input corresponds to a single bank of batteries. Within each bank, you need to turn on _exactly two_ batteries; the joltage that the bank produces is equal to the number formed by the digits on the batteries you've turned on. For example, if you have a bank like `12345` and you turn on batteries `2` and `4`, the bank would produce `24` jolts. (You cannot rearrange batteries.)

You'll need to find the largest possible joltage each bank can produce. In the above example:

*   In _`98`_`7654321111111`, you can make the largest joltage possible, _`98`_, by turning on the first two batteries.
*   In _`8`_`1111111111111`_`9`_, you can make the largest joltage possible by turning on the batteries labeled `8` and `9`, producing _`89`_ jolts.
*   In `2342342342342`_`78`_, you can make _`78`_ by turning on the last two batteries (marked `7` and `8`).
*   In `818181`_`9`_`1111`_`2`_`111`, the largest joltage you can produce is _`92`_.

The total output joltage is the sum of the maximum joltage from each bank, so in this example, the total output joltage is `98` + `89` + `78` + `92` = _`357`_.

There are many batteries in front of you. Find the maximum joltage possible from each bank; _what is the total output joltage?_

Your puzzle answer was `17383`.

## Part 2

The escalator doesn't move. The Elf explains that it probably needs more joltage to overcome the [static friction](https://en.wikipedia.org/wiki/Static_friction) of the system and hits the big red "joltage limit safety override" button. You lose count of the number of times she needs to confirm "yes, I'm sure" and decorate the lobby a bit while you wait.

Now, you need to make the largest joltage by turning on _exactly twelve_ batteries within each bank.

The joltage output for the bank is still the number formed by the digits of the batteries you've turned on; the only difference is that now there will be _`12`_ digits in each bank's joltage output instead of two.

Consider again the example from before:

    987654321111111
    811111111111119
    234234234234278
    818181911112111
    

Now, the joltages are much larger:

*   In `987654321111`_`111`_, the largest joltage can be found by turning on everything except some `1`s at the end to produce _`987654321111`_.
*   In the digit sequence `81111111111`_`111`_`9`, the largest joltage can be found by turning on everything except some `1`s, producing _`811111111119`_.
*   In `23`_`4`_`2`_`34234234278`_, the largest joltage can be found by turning on everything except a `2` battery, a `3` battery, and another `2` battery near the start to produce _`434234234278`_.
*   In _`8`_`1`_`8`_`1`_`8`_`1`_`911112111`_, the joltage _`888911112111`_ is produced by turning on everything except some `1`s near the front.

The total output joltage is now much larger: `987654321111` + `811111111119` + `434234234278` + `888911112111` = _`3121910778619`_.

_What is the new total output joltage?_

Your puzzle answer was `172601598658203`.

## Solution Notes

Part 1 is easily solvable with a brute-force approach that finds the maximum of all O(n²) combinations. Nice.

Part 2 is one of the typical "what if we crank it up to eleven" (or twelve, in this case) scenarios, and it's a rare case where a classical greedy algorithm is actually the best approach: Select the first occurrence of highest digit of the number, add that digit to the result number, discard all digits up to and including it, and loop again until 12 digits have been collected. The critical point is that the highest digit search must stop at an appropriate point so that 12-digit numbers can still be produced. For example, the maximum search for the first result digit must ignore the last 11 digits of the input number, because otherwise it wouldn't be possible to still construct a 12-digit result. This approach is blazing fast and relatively short; conveniently, it even works on strings and characters that only need to be converted to actual numbers for the final summation.

But this wasn't my initial approach; first I tried with DFS and memoization, but this blew up with some numbers in my input, even after I added a few pruning optimizations. Again, it shows that using search algorithms for puzzles like these is a very fragile undertaking. With a few hints from a friend, I finally managed to get a DFS-based approach working a few hours later, but it's both larger and slower than the simple greedy approach. However, it's good for one thing: It makes it trivial to write a combined solution for parts 1 and 2 with almost no overhead.

I also revisited the nice greedy algorithm again later that day and ported it to x86 assembly and DOS, arriving at a 222-byte executable that runs in about 2 seconds on a 1981-era IBM PC 5150.

* Part 1, Python (brute force): 91 bytes, ~200 ms
* Part 2, Python (greedy algorithm): 151 bytes, <100 ms
* Part 2, Python (DFS+memoization): 191 bytes, ~250 ms
* Parts 1+2, Python (DFS+memoization): 205 bytes, ~250 ms
