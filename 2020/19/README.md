# [2020, Day 19: Monster Messages](https://adventofcode.com/2020/day/19)

The input consists of (typically) 420 binary strings of length 24 to 88, plus a set of (typically) 130 matching rules, identified by a number. Each rule can either be a single-digit binary literal, a concatenation of two other rules, or a choice of _two_ concatenations of other rules.

**Part 1** asks which of the strings match a specific rule.

**Part 2** asks the same, but it replaces two existing rules by new ones. Both new rules are OR rules, however the second option is a single other rule in one case, and a concatenation of _three_ other rules in the other case.


## Solution Notes

My (and certainly many other participants') initial approach was to build a regular expression and then just use that. However, the generated REs contain so many nested subgroups that some engines -- including Python's -- simply give up. So, manual parsing it is, then.

Part 2 caught me by surprise. I debugged multiple hours on my solution until I finally came to the conclusion that I really have to do a multi-path search (essentially a DFS) to get the correct answers.

* Part 1, Python: 431 bytes, <100 ms
* Part 2, Python: 504 bytes, ~300 ms
