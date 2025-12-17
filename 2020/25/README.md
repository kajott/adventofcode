# 2020, Day 25: Combo Breaker


## Solution Notes

The task is to break a (quite weak) Diffie-Hellman key exchange. I first feared that the problem size would be large enough to make a brute-force implementation unfeasible, but as the (relatively) low modulus already suggests, this isn't the case.

* Part 1, Python: 116 bytes, ~5 s
