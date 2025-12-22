# [2020, Day 25: Combo Breaker](https://adventofcode.com/2020/day/25)

The input consists of two 7-to-8-digit numbers, which are the *public keys* of two communication partners in a key exchange algorithm. In addition to the public keys, each partner has a private key that is not disclosed. The task asks for the encryption key `key = (A_public ^ B_private) mod m = (B_public ^ A_private) mod m`, with `^` denoting exponentiation, and a fixed modulus `m` of 20201227.


## Solution Notes

The task is to break a (quite weak) Diffie-Hellman key exchange. I first feared that the problem size would be large enough to make a brute-force implementation unfeasible, but as the (relatively) low modulus already suggests, this isn't the case.

* Part 1, Python: 116 bytes, ~5 s
