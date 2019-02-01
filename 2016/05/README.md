# 2016, Day 5: How About a Nice Game of Chess?

You are faced with a security door designed by Easter Bunny engineers that seem to have acquired most of their security knowledge by watching [hacking](https://en.wikipedia.org/wiki/Hackers_(film)) [movies](https://en.wikipedia.org/wiki/WarGames).

## Part 1

The _eight-character password_ for the door is generated one character at a time by finding the [MD5](https://en.wikipedia.org/wiki/MD5) hash of some Door ID (your puzzle input) and an increasing integer index (starting with `0`).

A hash indicates the _next character_ in the password if its [hexadecimal](https://en.wikipedia.org/wiki/Hexadecimal) representation starts with _five zeroes_. If it does, the sixth character in the hash is the next character of the password.

For example, if the Door ID is `abc`:

*   The first index which produces a hash that starts with five zeroes is `3231929`, which we find by hashing `abc3231929`; the sixth character of the hash, and thus the first character of the password, is `1`.
*   `5017308` produces the next interesting hash, which starts with `000008f82...`, so the second character of the password is `8`.
*   The third time a hash starts with five zeroes is for `abc5278568`, discovering the character `f`.

In this example, after continuing this search a total of eight times, the password is `18f47a30`.

Given the actual Door ID, _what is the password_?

Your puzzle input was still `cxdnnyjw`.

Your puzzle answer was `f77a0e6e`.

## Part 2

As the door slides open, you are presented with a second door that uses a slightly more inspired security mechanism. Clearly unimpressed by the last version (in what movie is the password decrypted _in order_?!), the Easter Bunny engineers have worked out [a better solution](https://www.youtube.com/watch?v=NHWjlCaIrQo&t=25).

Instead of simply filling in the password from left to right, the hash now also indicates the _position_ within the password to fill. You still look for hashes that begin with five zeroes; however, now, the _sixth_ character represents the _position_ (`0`\-`7`), and the _seventh_ character is the character to put in that position.

A hash result of `000001f` means that `f` is the _second_ character in the password. Use only the _first result_ for each position, and ignore invalid positions.

For example, if the Door ID is `abc`:

*   The first interesting hash is from `abc3231929`, which produces `0000015...`; so, `5` goes in position `1`: `_5______`.
*   In the previous method, `5017308` produced an interesting hash; however, it is ignored, because it specifies an invalid position (`8`).
*   The second interesting hash is at index `5357525`, which produces `000004e...`; so, `e` goes in position `4`: `_5__e___`.

You almost choke on your popcorn as the final character falls into place, producing the password `05ace8e3`.

Given the actual Door ID and this new method, _what is the password_? Be extra proud of your solution if it uses a cinematic "decrypting" animation.

Your puzzle input was still `cxdnnyjw`.

Your puzzle answer was `999828ec`.


## Solution Notes

Not much of a puzzle, just a plain programming task that takes an annoyingly long time to compute without any way to optimize it significantly.

* Part 1, Python: 123 bytes, ~10 s
* Part 2, Python: 172 bytes, ~40 s
