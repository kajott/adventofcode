# 2024, Day 13: Claw Contraption

Next up: the [lobby](../../2020/24) of a resort on a tropical island. The Historians take a moment to admire the hexagonal floor tiles before spreading out.

Fortunately, it looks like the resort has a new [arcade](https://en.wikipedia.org/wiki/Amusement_arcade)! Maybe you can win some prizes from the [claw machines](https://en.wikipedia.org/wiki/Claw_machine)?

## Part 1

The claw machines here are a little unusual. Instead of a joystick or directional buttons to control the claw, these machines have two buttons labeled `A` and `B`. Worse, you can't just put in a token and play; it costs _3 tokens_ to push the `A` button and _1 token_ to push the `B` button.

With a little experimentation, you figure out that each machine's buttons are configured to move the claw a specific amount to the _right_ (along the `X` axis) and a specific amount _forward_ (along the `Y` axis) each time that button is pressed.

Each machine contains one _prize_; to win the prize, the claw must be positioned _exactly_ above the prize on both the `X` and `Y` axes.

You wonder: what is the smallest number of tokens you would have to spend to win as many prizes as possible? You assemble a list of every machine's button behavior and prize location (your puzzle input). For example:

    Button A: X+94, Y+34
    Button B: X+22, Y+67
    Prize: X=8400, Y=5400
    
    Button A: X+26, Y+66
    Button B: X+67, Y+21
    Prize: X=12748, Y=12176
    
    Button A: X+17, Y+86
    Button B: X+84, Y+37
    Prize: X=7870, Y=6450
    
    Button A: X+69, Y+23
    Button B: X+27, Y+71
    Prize: X=18641, Y=10279

This list describes the button configuration and prize location of four different claw machines.

For now, consider just the first claw machine in the list:

*   Pushing the machine's `A` button would move the claw `94` units along the `X` axis and `34` units along the `Y` axis.
*   Pushing the `B` button would move the claw `22` units along the `X` axis and `67` units along the `Y` axis.
*   The prize is located at `X=8400`, `Y=5400`; this means that from the claw's initial position, it would need to move exactly `8400` units along the `X` axis and exactly `5400` units along the `Y` axis to be perfectly aligned with the prize in this machine.

The cheapest way to win the prize is by pushing the `A` button `80` times and the `B` button `40` times. This would line up the claw along the `X` axis (because `80*94 + 40*22 = 8400`) and along the `Y` axis (because `80*34 + 40*67 = 5400`). Doing this would cost `80*3` tokens for the `A` presses and `40*1` for the `B` presses, a total of _`280`_ tokens.

For the second and fourth claw machines, there is no combination of A and B presses that will ever win a prize.

For the third claw machine, the cheapest way to win the prize is by pushing the `A` button `38` times and the `B` button `86` times. Doing this would cost a total of _`200`_ tokens.

So, the most prizes you could possibly win is two; the minimum tokens you would have to spend to win all (two) prizes is _`480`_.

You estimate that each button would need to be pressed _no more than `100` times_ to win a prize. How else would someone be expected to play?

Figure out how to win as many prizes as possible. _What is the fewest tokens you would have to spend to win all possible prizes?_

Your puzzle answer was `35574`.

## Part 2

As you go to win the first prize, you discover that the claw is nowhere near where you expected it would be. Due to a unit conversion error in your measurements, the position of every prize is actually `10000000000000` higher on both the `X` and `Y` axis!

Add `10000000000000` to the `X` and `Y` position of every prize. After making this change, the example above would now look like this:

    Button A: X+94, Y+34
    Button B: X+22, Y+67
    Prize: X=10000000008400, Y=10000000005400
    
    Button A: X+26, Y+66
    Button B: X+67, Y+21
    Prize: X=10000000012748, Y=10000000012176
    
    Button A: X+17, Y+86
    Button B: X+84, Y+37
    Prize: X=10000000007870, Y=10000000006450
    
    Button A: X+69, Y+23
    Button B: X+27, Y+71
    Prize: X=10000000018641, Y=10000000010279

Now, it is only possible to win a prize on the second and fourth claw machines. Unfortunately, it will take _many more than `100` presses_ to do so.

Using the corrected prize coordinates, figure out how to win as many prizes as possible. _What is the fewest tokens you would have to spend to win all possible prizes?_

Your puzzle answer was `80882098756071`.

## Solution Notes

There are a few red herrings in the task description: The maximum of 100 for A and B, for example, really only serves to minimize the search range for a brute-force solution and is otherwise of no significance. (The real input *does* check that the values can go up to 100 and don't stop at 99 though!) Another potential trap is that the question at the end of part 1 implies that there may be multiple ways to reach the target &ndash; but there aren't, and there can't be, as the entire thing is a linear system with 2 unknowns and 4 constraints, so it has to have a unique (though not necessarily integer) solution.

Part 1 is still solvable by brute-forcing through all 10k A/B combinations within the search range, part 2 obviously isn't. Instead, you really need to solve the linear system, and fail if any of the divisions in that process yield a remainder. That's obviously the much faster method, and it completes the task in no time at all.

* Part 1, Python: 182 bytes, ~700 ms
* Part 2, Python: 210 bytes, <100 ms
