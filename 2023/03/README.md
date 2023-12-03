# 2023, Day 3: Gear Ratios

You and the Elf eventually reach a [gondola lift](https://en.wikipedia.org/wiki/Gondola_lift) station; he says the gondola lift will take you up to the _water source_, but this is as far as he can bring you. You go inside.

It doesn't take long to find the gondolas, but there seems to be a problem: they're not moving.

"Aaah!"

You turn around to see a slightly-greasy Elf with a wrench and a look of surprise. "Sorry, I wasn't expecting anyone! The gondola lift isn't working right now; it'll still be a while before I can fix it." You offer to help.

The engineer explains that an engine part seems to be missing from the engine, but nobody can figure out which one. If you can _add up all the part numbers_ in the engine schematic, it should be easy to work out which part is missing.

## Part 1

The engine schematic (your puzzle input) consists of a visual representation of the engine. There are lots of numbers and symbols you don't really understand, but apparently _any number adjacent to a symbol_, even diagonally, is a "part number" and should be included in your sum. (Periods (`.`) do not count as a symbol.)

Here is an example engine schematic:

    467..114..
    ...*......
    ..35..633.
    ......#...
    617*......
    .....+.58.
    ..592.....
    ......755.
    ...$.*....
    .664.598..
    

In this schematic, two numbers are _not_ part numbers because they are not adjacent to a symbol: `114` (top right) and `58` (middle right). Every other number is adjacent to a symbol and so _is_ a part number; their sum is _`4361`_.

Of course, the actual engine schematic is much larger. _What is the sum of all of the part numbers in the engine schematic?_

Your puzzle answer was `537732`.

## Part 2

The engineer finds the missing part and installs it in the engine! As the engine springs to life, you jump in the closest gondola, finally ready to ascend to the water source.

You don't seem to be going very fast, though. Maybe something is still wrong? Fortunately, the gondola has a phone labeled "help", so you pick it up and the engineer answers.

Before you can explain the situation, she suggests that you look out the window. There stands the engineer, holding a phone in one hand and waving with the other. You're going so slowly that you haven't even left the station. You exit the gondola.

The missing part wasn't the only issue - one of the gears in the engine is wrong. A _gear_ is any `*` symbol that is adjacent to _exactly two part numbers_. Its _gear ratio_ is the result of multiplying those two numbers together.

This time, you need to find the gear ratio of every gear and add them all up so that the engineer can figure out which gear needs to be replaced.

Consider the same engine schematic again:

    467..114..
    ...*......
    ..35..633.
    ......#...
    617*......
    .....+.58.
    ..592.....
    ......755.
    ...$.*....
    .664.598..
    

In this schematic, there are _two_ gears. The first is in the top left; it has part numbers `467` and `35`, so its gear ratio is `16345`. The second gear is in the lower right; its gear ratio is `451490`. (The `*` adjacent to `617` is _not_ a gear because it is only adjacent to one part number.) Adding up all of the gear ratios produces _`467835`_.

_What is the sum of all of the gear ratios in your engine schematic?_

Your puzzle answer was `84883664`.

## Solution Notes

The tricky part here is coming up with an easy to handle data structure in which to store the input data for easy processing. In the end, what needs to be done is kind of a connected component analysis in horizontal direction, starting at the neighbor positions of the symbols, to retrieve the surrounding numbers.

My initial approach was to use the proven method of a coordinate-as-complex-number to character dictionary, and having a lookup function that "samples" a number at a specified position, if there is one. This does the job well; it even reduces the actual evaluations for both parts to one (lengthly) line each, albeit with lots of nested generator expressions containing nested loops. Still, the "sampling" function stood out as being quite long ... there has to be a better way?

There is another approach, after all: Parse numbers as such right at the beginning, and store them as _(row, start column, end column, value)_ tuples. This indeed simplifies the sampling function a lot (it's a one-liner now), but it makes the input parser more complex (it's no longer a one-liner) and complex numbers are out of the question, because we need to compare coordinates against intervals. In the end, this approach turned out to be significantly worse in terms of code size and, surprisingly, execution time too.

* Part 1, Python (complex number dictionary): 294 bytes, <100 ms
* Part 2, Python (complex number dictionary): 332 bytes, <100 ms
* Part 1, Python (list of spans): 355 bytes, ~800 ms
* Part 2, Python (list of spans): 399 bytes, ~400 ms
