# [2023, Day 6: Wait For It](https://adventofcode.com/2023/day/6)

The input consists of (typically) four pairs of 2-digit times and 3-to-4-digit distances.

The task is about simulating a race. The time from the input specifies how long a race takes. At the start, the racer can select how many time units they want to spend on accelerating; with every time unit spent for accelerating, velocity increases by one. However, the vehicle does _not_ move during the acceleration phase; it only starts moving with its final velocity _after_ accelerating, and keeps this speed until the end of the race.

**Part 1** asks how many different acceleration strategies would cause the player to win each of the races, i.e. beat the distance recorded in the input.

**Part 2** asks the same, however there is only a single race, and the time and distance number are just a concatenation of the digits provided for the multiple races that have been simulated in part 1.


## Solution Notes

A very easy puzzle. The problem size in part 2 is fortunately small enough that brute force is a [perfectly cromulent](https://www.merriam-webster.com/wordplay/what-does-cromulent-mean) approach to solving it, and it doesn't exceed the range and precision of 64-bit floating-point values either, so solving the underlying quadratic equation is also not a problem. I tried both solutions, and it's the classic code size vs. run time tradeoff: Brute force takes 5 seconds, but it's also 6 bytes shorter.

* Part 1, Python: 116 bytes, <100 ms
* Part 2, Python (brute force): 99 bytes, ~5 s
* Part 2, Python (quadratic equation solving): 105 bytes, <100 ms
