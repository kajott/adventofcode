# 2022, Day 23: Unstable Diffusion


## Solution Notes

This is essentially just a simulation of a 2D cellular automaton, with a few minor twists: First, there's global state (the direction priority) that changes the rules slightly between ticks, and second, the "collision detection" rules are quite peculiar.

All my implementations, whether golf or not, operate on a set of Elf positions as the basic data structure. Elves are not addressed individually, nor do they need to be. If the rules are implemented correctly, the amount of Elves in the set stays constant over time.

The two phases of the move are actually modelled as such in the golfed code: In the first phase, a list of potential ("free") movement directions is generated for each Elf. If there is at least one free direction, but **not** all four directions are free (which means that all eight neighbor locations are empty and the Elf shall not move), the Elf's target location is set to the first potential movement direction, otherwise it's set to the Elf's original position. The moves are entered into a dictionary that maps _target_ positions to a _set_ of original positions. This becomes important in the second phase, where the set of Elves is reconstructed from that dictionary: If a destination's entry contains exactly one source Elf location, the Elf spawns at the destination location; otherwise (i.e. there is more than one Elf who wants to move to the given location), the source Elves are spawned at their old locations again.

This approach works nicely, but it ain't exactly fast, as there's a lot of looping over individual Elves and their positions involved. However, at 10-15 seconds, it's still not bad enough to warrant refactoring.

The code size is dominated by the simulation aspect, hence it makes a lot of sense to combine both parts into a common solution. Part 1 alone is larger than Part 2, because determining the bounding box is always a tedious process in Python, let alone when complex numbers (which I used here extensively) need to be unpacked.

An experimental (non-golf) C implementation that works on a grid instead of a set of coordinates runs both parts in less than 200 milliseconds including compilation, and less than 100 ms without.

* Part 1, Python: 424 bytes, ~150 ms
* Part 2, Python: 333 bytes, ~15 s
* Parts 1+2, Python: 441 bytes, ~15 s
