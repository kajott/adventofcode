# 2020, Day 19: Monster Messages


## Solution Notes

My (and certainly many other participants') initial approach was to build a regular expression and then just use that. However, the generated REs contain so many nested subgroups that some engines -- including Python's -- simply give up. So, manual parsing it is, then.

Part 2 caught me by surprise. I debugged multiple hours on my solution until I finally came to the conclusion that I really have to do a multi-path search (essentially a DFS) to get the correct answers.

* Part 1, Python: 431 bytes, <100 ms
* Part 2, Python: 504 bytes, ~300 ms
