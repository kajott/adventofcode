# 2024, Day 8: Resonant Collinearity


## Solution Notes

A very complicated task description that ends up in a relatively unspectacular implementation. In part 1, some care has to be taken to (a) only count each antenna pair once, (b) **not** automatically count the antennas themselves as antinodes, unless they are referenced by some other antenna pair, and (c) to precisely exclude results outside the valid area. Even though contraint (c) requires individual component access, complex numbers prove as useful tools here once again.

Part 2 is a great surprise, because it's actually _simpler_ than part 1. It's easy to miss in the description (trust me on that one!), but the antennas now **are** antinodes themselves, so you just need to splat antinodes at each antenna and any multiple of the distance from that to any other same-frequency antenna. You _could_ compute how many antinodes to put, but you could also rightly assume that it's never more than the map size and prune out-of-map antinodes during the final count, as was a good idea for part 1 already.

The interesting thing is, as a friend pointed out, that the simplicity of part 2 is only due to the construction of the input data. The X and Y deltas of any same-frequency antenna pair are always coprime, meaning that "exactly in line with two antennas" really only yields multiples of the X and Y deltas. If delta-X and delta-Y were both even, for example, there would be additional antinodes at the halfway point between them - but that just never happens in the input data, and at around 500 antenna pairs for a typical input, that can't be coincidence.

* Part 1, Python: 247 bytes, <100 ms
* Part 2, Python: 233 bytes, <100 ms
