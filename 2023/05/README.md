# 2023, Day 5: If You Give A Seed A Fertilizer

You take the boat and find the gardener right where you were told he would be: managing a giant "garden" that looks more to you like a farm.

"A water source? Island Island _is_ the water source!" You point out that Snow Island isn't receiving any water.

"Oh, we had to stop the water because we _ran out of sand_ to [filter](https://en.wikipedia.org/wiki/Sand_filter) it with! Can't make snow with dirty water. Don't worry, I'm sure we'll get more sand soon; we only turned off the water a few days... weeks... oh no." His face sinks into a look of horrified realization.

"I've been so busy making sure everyone here has food that I completely forgot to check why we stopped getting more sand! There's a ferry leaving soon that is headed over in that direction - it's much faster than your boat. Could you please go check it out?"

You barely have time to agree to this request when he brings up another. "While you wait for the ferry, maybe you can help us with our _food production problem_. The latest Island Island [Almanac](https://en.wikipedia.org/wiki/Almanac) just arrived and we're having trouble making sense of it."

## Part 1

The almanac (your puzzle input) lists all of the seeds that need to be planted. It also lists what type of soil to use with each kind of seed, what type of fertilizer to use with each kind of soil, what type of water to use with each kind of fertilizer, and so on. Every type of seed, soil, fertilizer and so on is identified with a number, but numbers are reused by each category - that is, soil `123` and fertilizer `123` aren't necessarily related to each other.

For example:

    seeds: 79 14 55 13
    
    seed-to-soil map:
    50 98 2
    52 50 48
    
    soil-to-fertilizer map:
    0 15 37
    37 52 2
    39 0 15
    
    fertilizer-to-water map:
    49 53 8
    0 11 42
    42 0 7
    57 7 4
    
    water-to-light map:
    88 18 7
    18 25 70
    
    light-to-temperature map:
    45 77 23
    81 45 19
    68 64 13
    
    temperature-to-humidity map:
    0 69 1
    1 0 69
    
    humidity-to-location map:
    60 56 37
    56 93 4
    

The almanac starts by listing which seeds need to be planted: seeds `79`, `14`, `55`, and `13`.

The rest of the almanac contains a list of _maps_ which describe how to convert numbers from a _source category_ into numbers in a _destination category_. That is, the section that starts with `seed-to-soil map:` describes how to convert a _seed number_ (the source) to a _soil number_ (the destination). This lets the gardener and his team know which soil to use with which seeds, which water to use with which fertilizer, and so on.

Rather than list every source number and its corresponding destination number one by one, the maps describe entire _ranges_ of numbers that can be converted. Each line within a map contains three numbers: the _destination range start_, the _source range start_, and the _range length_.

Consider again the example `seed-to-soil map`:

    50 98 2
    52 50 48
    

The first line has a _destination range start_ of `50`, a _source range start_ of `98`, and a _range length_ of `2`. This line means that the source range starts at `98` and contains two values: `98` and `99`. The destination range is the same length, but it starts at `50`, so its two values are `50` and `51`. With this information, you know that seed number `98` corresponds to soil number `50` and that seed number `99` corresponds to soil number `51`.

The second line means that the source range starts at `50` and contains `48` values: `50`, `51`, ..., `96`, `97`. This corresponds to a destination range starting at `52` and also containing `48` values: `52`, `53`, ..., `98`, `99`. So, seed number `53` corresponds to soil number `55`.

Any source numbers that _aren't mapped_ correspond to the _same_ destination number. So, seed number `10` corresponds to soil number `10`.

So, the entire list of seed numbers and their corresponding soil numbers looks like this:

    seed  soil
    0     0
    1     1
    ...   ...
    48    48
    49    49
    50    52
    51    53
    ...   ...
    96    98
    97    99
    98    50
    99    51
    

With this map, you can look up the soil number required for each initial seed number:

*   Seed number `79` corresponds to soil number `81`.
*   Seed number `14` corresponds to soil number `14`.
*   Seed number `55` corresponds to soil number `57`.
*   Seed number `13` corresponds to soil number `13`.

The gardener and his team want to get started as soon as possible, so they'd like to know the closest location that needs a seed. Using these maps, find _the lowest location number that corresponds to any of the initial seeds_. To do this, you'll need to convert each seed number through other categories until you can find its corresponding _location number_. In this example, the corresponding types are:

*   Seed `79`, soil `81`, fertilizer `81`, water `81`, light `74`, temperature `78`, humidity `78`, _location `82`_.
*   Seed `14`, soil `14`, fertilizer `53`, water `49`, light `42`, temperature `42`, humidity `43`, _location `43`_.
*   Seed `55`, soil `57`, fertilizer `57`, water `53`, light `46`, temperature `82`, humidity `82`, _location `86`_.
*   Seed `13`, soil `13`, fertilizer `52`, water `41`, light `34`, temperature `34`, humidity `35`, _location `35`_.

So, the lowest location number in this example is _`35`_.

_What is the lowest location number that corresponds to any of the initial seed numbers?_

Your puzzle answer was `993500720`.

## Part 2

Everyone will starve if you only plant such a small number of seeds. Re-reading the almanac, it looks like the `seeds:` line actually describes _ranges of seed numbers_.

The values on the initial `seeds:` line come in pairs. Within each pair, the first value is the _start_ of the range and the second value is the _length_ of the range. So, in the first line of the example above:

    seeds: 79 14 55 13

This line describes two ranges of seed numbers to be planted in the garden. The first range starts with seed number `79` and contains `14` values: `79`, `80`, ..., `91`, `92`. The second range starts with seed number `55` and contains `13` values: `55`, `56`, ..., `66`, `67`.

Now, rather than considering four seed numbers, you need to consider a total of _27_ seed numbers.

In the above example, the lowest location number can be obtained from seed number `82`, which corresponds to soil `84`, fertilizer `84`, water `84`, light `77`, temperature `45`, humidity `46`, and _location `46`_. So, the lowest location number is _`46`_.

Consider all of the initial seed numbers listed in the ranges on the first line of the almanac. _What is the lowest location number that corresponds to any of the initial seed numbers?_

Your puzzle answer was `4917124`.

## Solution Notes

Part 1 is almost trivial: Run the numbers through the various maps, determine the minimum result, done.

Part 2 seems to be the same, but in a loop; however, the actual input data uses 9-digit ranges, so a more thoughtful approach is required. The basic idea is to run intervals through the maps, not single numbers. At every mapped range, the intervals are split if they intersect with the beginning or the end of the range, and the inner part is mapped according to the almanac. It's a bit finicky to get the conditions just right, and it requires a fair deal of `if`s and comparisons, but it's manageable.

But wait ... is it even true that a clever approach is a must-have and brute force iteration is a no-go? I estimated that a beefy top-of-the-line computer would need several hours on all cores to crunch through the ~2 billion iterations. Nevertheless, I was intrigued enough to actually implement a solution that's at the same time as dumb as possible, but also as efficient as possible: A Python script that translates the input into a C program that contains ~200 lines of the form `if ((n >= A) && (n < B)) { n = n - A + C; goto end_of_this_map; }` (with `A`, `B` and `C` substituted with the appropriate numbers), and a loop around it to find the minimum value of `n`. When running this, I quickly learned that my initial estimate was off by several orders of magnitude: It completes in about a minute on a single core! An iteration only takes between 100 and 200 CPU clock cycles on average (depending on the compiler, CPU microarchitecture, and whether Spectre/Meltdown mitigations are in effect). Indeed, this is about the most performance-optimal code for a modern CPU: It nicely fits into L1 cache, rarely accesses any other memory, and even though it's quite branchy, those branches are *very* consistent between iterations, making the branch predictor's job easier.

* Part 1, Python: 230 bytes, <100 ms
* Part 2, Python (interval processing): 423 bytes, <100 ms
* Part 2, Python-generated C code (brute force): ~70 s
