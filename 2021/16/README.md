# [2021, Day 16: Packet Decoder](https://adventofcode.com/2021/day/16)

The input consists of a (typically) 1300-digit hexadecimal string that is to be converted to binary first. It contains a _packet_ of data.

Each packet starts with a 3-bit version and a 3-bit type.

Type 4 encodes a literal value, i.e. a single binary number. During encoding, the number is split into 4-bit segments. Then, each of the segments is transmitted, most significant first, preceded by an extra bit incidating whether another segment follows.

All other packet types are _operator_ packets containing one or more sub-packets. Following the type, the length (in bits) of the sub-packets are encoded as a 15-bit number prefixed with a `0` bit, or an 11-bit number prefixed with a `1` it. After the length information, the sub-packet data follows.

Type 0 computes the sum of the sub-packets, type 1 the product, type 2 the minimum, type 3 the maximum. Types 5 to 7 perform comparisons of exactly two packets and result in a value of 1 if the check succeeds and 0 if it fails. Type 5 compares for greater than, type 6 is less than, type 7 compares for equality.

**Part 1** asks for the sum of the version fields in the entire sub-packet hierarchy, disregarding the operators.

**Part 2** asks for the result of the actual computations in the input packet.


## Solution Notes

There is nothing special about this puzzle: follow the instructions to the letter, and that's it. Turning this into a somewhat golfed solution was the greater challenge.

* Part 1, Python: 297 bytes, <100 ms
* Part 2, Python: 438 bytes, <100 ms
