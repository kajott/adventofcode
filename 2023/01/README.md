# 2023, Day 1: Trebuchet?!


## Solution Notes

Part 2 of this task is surprisingly complex for a day-one puzzle. There are quite a few special cases that need to be covered, specifically around the question how to deal with overlapping numbers (e.g. `eightwo`). What the description inconveniently fails to mention, and the test data for part 2 fails to check in a meaningful way either, is that those are supposed to count as _both_, i.e. `eightwo` = `82`. In the end, the only proper solution is to either compile a list of **all** occurrences of any digits or numerals and pick the first and last of them; or (and this is what I ultimately used) search specifically for the _first and last_ occurrences of any digit or numeral and combine those.

* Part 1, Python: 88 bytes, <100 ms
* Part 2, Python: 246 bytes, <100 ms
