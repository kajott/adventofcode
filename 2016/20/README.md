# 2016, Day 20: Firewall Rules

You'd like to set up a small hidden computer here so you can use it to get back into the network later. However, the corporate firewall only allows communication with certain external [IP addresses](https://en.wikipedia.org/wiki/IPv4#Addressing).

## Part 1

You've retrieved the list of blocked IPs from the firewall, but the list seems to be messy and poorly maintained, and it's not clear which IPs are allowed. Also, rather than being written in [dot-decimal](https://en.wikipedia.org/wiki/Dot-decimal_notation) notation, they are written as plain [32-bit integers](https://en.wikipedia.org/wiki/32-bit), which can have any value from `0` through `4294967295`, inclusive.

For example, suppose only the values `0` through `9` were valid, and that you retrieved the following blacklist:

    5-8
    0-2
    4-7
    

The blacklist specifies ranges of IPs (inclusive of both the start and end value) that are _not_ allowed. Then, the only IPs that this firewall allows are `3` and `9`, since those are the only numbers not in any range.

Given the list of blocked IPs you retrieved from the firewall (your puzzle input), _what is the lowest-valued IP_ that is not blocked?

Your puzzle answer was `31053880`.

## Part 2

_How many IPs_ are allowed by the blacklist?

Your puzzle answer was `117`.


## Solution Notes

Both parts require coming up with a good first idea for an algorithm, which took me some time. Conveniently, the solution for part 2 can be built upon the solution for part 1.

I was really surprised of just how restrictive the "blacklist" is ...

* Part 1, Python: 127 bytes, <100 ms
* Part 2, Python: 179 bytes, <100 ms
