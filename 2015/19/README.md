# 2015, Day 19: Medicine for Rudolph

Rudolph the Red-Nosed Reindeer is sick! His nose isn't shining very brightly, and he needs medicine.

Red-Nosed Reindeer biology isn't similar to regular reindeer biology; Rudolph is going to need custom-made medicine. Unfortunately, Red-Nosed Reindeer chemistry isn't similar to regular reindeer chemistry, either.

The North Pole is equipped with a Red-Nosed Reindeer nuclear fusion/fission plant, capable of constructing any Red-Nosed Reindeer molecule you need. It works by starting with some input molecule and then doing a series of _replacements_, one per step, until it has the right molecule.

## Part 1

However, the machine has to be calibrated before it can be used. Calibration involves determining the number of molecules that can be generated in one step from a given starting point.

For example, imagine a simpler machine that supports only the following replacements:

    H => HO
    H => OH
    O => HH
    

Given the replacements above and starting with `HOH`, the following molecules could be generated:

*   `HOOH` (via `H => HO` on the first `H`).
*   `HOHO` (via `H => HO` on the second `H`).
*   `OHOH` (via `H => OH` on the first `H`).
*   `HOOH` (via `H => OH` on the second `H`).
*   `HHHH` (via `O => HH`).

So, in the example above, there are `4` _distinct_ molecules (not five, because `HOOH` appears twice) after one replacement from `HOH`. Santa's favorite molecule, `HOHOHO`, can become `7` _distinct_ molecules (over nine replacements: six from `H`, and three from `O`).

The machine replaces without regard for the surrounding characters. For example, given the string `H2O`, the transition `H => OO` would result in `OO2O`.

Your puzzle input describes all of the possible replacements and, at the bottom, the medicine molecule for which you need to calibrate the machine. _How many distinct molecules can be created_ after all the different ways you can do one replacement on the medicine molecule?

Your puzzle answer was `518`.

## Part 2

Now that the machine is calibrated, you're ready to begin molecule fabrication.

Molecule fabrication always begins with just a single electron, `e`, and applying replacements one at a time, just like the ones during calibration.

For example, suppose you have the following replacements:

    e => H
    e => O
    H => HO
    H => OH
    O => HH
    

If you'd like to make `HOH`, you start with `e`, and then make the following replacements:

*   `e => O` to get `O`
*   `O => HH` to get `HH`
*   `H => OH` (on the second `H`) to get `HOH`

So, you could make `HOH` after _`3` steps_. Santa's favorite molecule, `HOHOHO`, can be made in _`6` steps_.

How long will it take to make the medicine? Given the available _replacements_ and the _medicine molecule_ in your puzzle input, what is the _fewest number of steps_ to go from `e` to the medicine molecule?

Your puzzle answer was `200`.


## Solution Notes

The second part has the potential to be a major headache, and indeed a standard BFS approach blows up quite spectacularly. So imagine my surprise when I found out that even the dumbest DFS implementation works just fine! I actually added a greedy optimization later on to be a bit on the safe side in case my input was too optimistic, but there seems to be only a single input to begin with: I found the exact same input file in other people's repositories ...

* Part 1, Python: 275 bytes, <100 ms
* Part 2, Python (dumb DFS): 240 bytes, <100 ms
* Part 2, Python (greedy DFS): 281 bytes, <100 ms
