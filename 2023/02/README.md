# [2023, Day 2: Cube Conundrum](https://adventofcode.com/2023/day/2)

The input consists of (typically) 100 logs of a draw of differently-colored objects. Each log contains up to three separate draws that specify how many instances of the three color have been drawn.

**Part 1** asks which of these logs are plausible if there is only a certain maximum number of objects in each of the colors available.

**Part 2** asks, for each of the logs, the minimum number of objects per color that would make all draws possible.


## Solution Notes

A quite straightforward puzzle, without any pitfalls in the input data (like some color missing from a game). The greatest challenge is coming up with a nice way to parse the input data.

* Part 1, Python: 179 bytes, <100 ms
* Part 2, Python: 184 bytes, <100 ms
