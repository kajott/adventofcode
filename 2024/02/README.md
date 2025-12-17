# 2024, Day 2: Red-Nosed Reports


## Solution Notes

A simple by-the-rules affair that requires computing the differences *and* absolute differences of adjacent pairs. Checking the monotonicity criterion can be very elegantly solved by multiplying the minimum and maximum of the pairwise differences together; if there's both positive and negative steps, the result will be negative, but if it's all positive or all negative, the result will be positive. The "levels differ at least by one" criterion can be very conveniently checked at the same time, because if the sequence is only monotonic, but not strongly monotonic, the minimum or maximum is going to be zero, causing the product to become zero too.

Using Python's assignment expressions (`:=` operator), part 1 can be nicely shrunk down to a single line.

* Part 1, Python: 138 bytes, <100 ms
* Part 2, Python: 193 bytes, <100 ms
