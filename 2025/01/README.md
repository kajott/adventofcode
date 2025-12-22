# [2025, Day 1: Secret Entrance](https://adventofcode.com/2025/day/1)

The task simulates a rotary dial with 100 positions (0...99), starting at position 50. The input contains (typically) several thousand rotation commands like `L42`, `R1234` etc.

**Part 1** asks how often the dial stops at position 0 after a rotation.

**Part 2** asks how often the dial reaches position 0 at *any* point in time (including _during_ a rotation).


## Solution Notes

Part 2 initially sounds like it requires the kind of modular arithmetic that's _just_ a little bit too complicated for 6 o'clock AM on the first day. However, the numbers are so relatively small (they sum up to ~600k in my input) that a simple iterative solution works well enough, and as a bonus, it comes in at just below 100 bytes.

Because this task is so relatively simple, I tried my hand at x86 assembly again and came up with a 192-byte DOS 2.0 executable that runs both parts on a 1981 IBM 5150 PC with a 4.77 MHz Intel 8088 processor in about 2 seconds, more than half of which is I/O time.

* Part 1, Python: 83 bytes, <100 ms
* Part 2, Python: 91 bytes, ~150 ms
