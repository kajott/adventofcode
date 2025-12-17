# [2024, Day 17: Chronospatial Computer](https://adventofcode.com/2024/day/17)


## Solution Notes

Part 1 is just straight implementation of the spec. Golfing this has been a lot of fun, including tricks like (mostly) branchless execution due to having a neutral fourth register that can be clobbered by operations that don't store anything in the three registers, using shifts to represent constant arrays, and a few other tricks.

Part 2 is a classical reverse engineering puzzle. Obviously, what the program outputs is somehow encoded in the `A` register on startup; the goal is then to set `A` such that the sequence of numbers forming the program is emitted. Now, how does that work? As it turns out, the program always performs some computation on the value of `A` and outputs that, then later shifts `A` three bits down (`adv 3`), and ends in a `jnz 0`. The values of `B` and `C` are always overwritten with each program run, so their initial value doesn't matter, and `A` is only updated by the aforementioned `adv 3` instruction. Essentially, this forms a loop of the form `do { out(f(A) & 7); A >>= 3; } while (A)`. The `f()` function can be anything &ndash; in practice, it seems to be in the form `f(A) = A ^ (const1 ^ const2) ^ (A >> ((A & 7) ^ const1))` (`^` = XOR), with `const1` and `const2` being 3-bit constants.

What this means is that every 3-bit group in `A` generates one output value, starting with the LSBs. For the program, which has length 16, this means that `A` is a 48-bit number, which also makes it clear that brute force is definitely not the way to go about this puzzle. Instead, the value of `A` can be constructed (almost literally) bit by bit, in reverse order: The value of `A` that generates the *last* instruction word has to be found (and there are just 8 possible values, so trying all of them is fine), and then `A` can be shifted up by 3 bits and again some value between 0 and 7 has to be added to get the second-to-last instruction, and so on. Multiple possible addends can result in the same value being output; in these cases, it's *not* sufficient to just take the minimum value, because it can (and does) turn out that sometimes, the necessary bit patterns can't be found to construct a later instruction word. Thus, a full DFS is required, but it's still plenty fast.

I solved part 2 in two ways: First, I had a version that encodes the function of my specific input directly in Python, but later on, I wrote a version that actually runs the program to produce the output. Obviously, the first version is much smaller, since it doesn't need the entire interpreter.

* Part 1, Python: 279 bytes, <100 ms
* Part 2, Python (puzzle input specific): 201 bytes, <100 ms
* Part 2, Python (generic): 391 bytes, <100 ms
