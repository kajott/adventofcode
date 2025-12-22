# [2022, Day 9: Rope Bridge](https://adventofcode.com/2022/day/9)

The input consists of a sequence of (tyically) 2000 move instructions in any of the four cardinal directions, each associated with a length between 1 and 19.

These instructions are to be played back for the head of a simulated rope. The _tail_ of the rope always needs to follow the head. It can be at the same location as the head or any of its 8 neighbor cells, but not farther away. If it is, its position is readjusted to the the closest of the 4 neighbors of the head in cardinal directions.

**Part 1** asks for how many distinct cells the tail touches while the head performs the motions described in the input.

**Part 2** asks the same, but now there's not just one head and one tail, but eight additional segments inbetween, and each segment follows the previous segment with the same rules as in part 1.


## Solution Notes

The task description sounds downright intimidating, with (seemingly) complex rules that need to be followed to the letter. In the end, it turns out to be rather simple: If a tail is more than two units away from its head on _either_ axis, it gets "pulled" one unit towards the head on _both_ axes.

The actual fun part here is golfing. I usually use complex numbers for 2D grid stuff like this, but this time I initially dismissed the approach because during the "pull" operation, access to invididual X/Y components is required, which means constantly reading the `.real` and `.imag` properties, which can't be size-optimized. Or can it? It thought about that for a while and ultimately revisited the complex number idea; lo and behold, after refactoring the "pull" operation a bit, it can be reduced to a *single* instance of using `.real` and `.imag` each, ending up with a small 1-byte win for part 1 already, and a very solid 20-byte improvement for part 2!

Another very interesting aspect in the golf versions here is they way the `U`/`D`/`L`/`R` direction parser works. Instead of using a simple map from characters to delta vectors, I came up with a method to derive the vector components directly from the ASCII codes. First, the orientation (horizontal / vertical) and direction (-1 / +1) are detected, and this is then converted into the actual delta vector.

* Part 1, Python (coordinate tuples): 235 bytes, <100 ms
* Part 2, Python (coordinate tuples): 296 bytes, <100 ms
* Part 1, Python (complex numbers): 234 bytes, <100 ms
* Part 2, Python (complex numbers): 279 bytes, ~150 ms
