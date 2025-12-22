# [2020, Day 13: Shuttle Search](https://adventofcode.com/2020/day/13)

The input consists of two parts: a list of (typically) 63 intervals, most of them unknown (`x`), some of them 2-to-3-digit numbers; and a 7-digit start time.

The intervals describe periodic occurrences of an event that happen at time step 0 and all multiples of the interval.

**Part 1** asks for the time and interval of the next occurrence of *any* event, starting at the specified time, disregarding the unkown intervals.

**Part 2** asks to find a time step `t`, starting at 0, where the first listed iterval's event occurs, and the next item in the interval list occurs at `t+1`, the next at `t+2` etc. In other words, for any non-unknown interval at index `i` in the input list, an event shall occur at time step `t+i`.


## Solution Notes

Again one of these ultra math-heavy modular arithmetic puzzles ... or so I thought. Using the observation that all schedule intervals are prime numbers, a rather simple iterative solution can be found. But truth be told, I needed to have a look at the first answer in [a hint thread](https://www.reddit.com/r/adventofcode/comments/kc60ri) first.

* Part 1, Python: 118 bytes, <100 ms
* Part 2, Python: 137 bytes, <100 ms
