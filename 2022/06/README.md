# 2022, Day 6: Tuning Trouble

The preparations are finally complete; you and the Elves leave camp on foot and begin to make your way toward the _star_ fruit grove.

As you move through the dense undergrowth, one of the Elves gives you a handheld _device_. He says that it has many fancy features, but the most important one to set up right now is the _communication system_.

However, because he's heard you have [significant](../../2016/6) [experience](../../2016/25) [dealing](../../2019/7) [with](../../2019/9) [signal-based](../../2019/16) [systems](../../2021/25), he convinced the other Elves that it would be okay to give you their one malfunctioning device - surely you'll have no problem fixing it.

As if inspired by comedic timing, the device emits a few colorful sparks.

To be able to communicate with the Elves, the device needs to _lock on to their signal_. The signal is a series of seemingly-random characters that the device receives one at a time.

To fix the communication system, you need to add a subroutine to the device that detects a _start-of-packet marker_ in the datastream. In the protocol being used by the Elves, the start of a packet is indicated by a sequence of _four characters that are all different_.

## Part 1

The device will send your subroutine a datastream buffer (your puzzle input); your subroutine needs to identify the first position where the four most recently received characters were all different. Specifically, it needs to report the number of characters from the beginning of the buffer to the end of the first such four-character marker.

For example, suppose you receive the following datastream buffer:

    mjqjpqmgbljsphdztnvjfqwrcgsmlb

After the first three characters (`mjq`) have been received, there haven't been enough characters received yet to find the marker. The first time a marker could occur is after the fourth character is received, making the most recent four characters `mjqj`. Because `j` is repeated, this isn't a marker.

The first time a marker appears is after the _seventh_ character arrives. Once it does, the last four characters received are `jpqm`, which are all different. In this case, your subroutine should report the value _`7`_, because the first start-of-packet marker is complete after 7 characters have been processed.

Here are a few more examples:

*   `bvwbjplbgvbhsrlpgdmjqwftvncz`: first marker after character _`5`_
*   `nppdvjthqldpwncqszvftbrmjlhg`: first marker after character _`6`_
*   `nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg`: first marker after character _`10`_
*   `zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw`: first marker after character _`11`_

_How many characters need to be processed before the first start-of-packet marker is detected?_

Your puzzle answer was `1802`.

## Part 2

Your device's communication system is correctly detecting packets, but still isn't working. It looks like it also needs to look for _messages_.

A _start-of-message marker_ is just like a start-of-packet marker, except it consists of _14 distinct characters_ rather than 4.

Here are the first positions of start-of-message markers for all of the above examples:

*   `mjqjpqmgbljsphdztnvjfqwrcgsmlb`: first marker after character _`19`_
*   `bvwbjplbgvbhsrlpgdmjqwftvncz`: first marker after character _`23`_
*   `nppdvjthqldpwncqszvftbrmjlhg`: first marker after character _`23`_
*   `nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg`: first marker after character _`29`_
*   `zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw`: first marker after character _`26`_

_How many characters need to be processed before the first start-of-message marker is detected?_

Your puzzle answer was `3551`.

## Solution Notes

This task is almost comically easy; the only prerequisite is understanding how to use sets. The difference between parts 1 and 2 is just a parameter that increases runtime by a mere factor of seven. I guess that for people who tried to solve part 1 in terms of mere comparisons (i.e. `a!=b and a!=c and a!=d and b!=c and b!=d and c!=d`), part 2 might have been a nastier surprise.

The x86 DOS version is also very compact this time. It uses a small histogram of 32 bins (enough to tell letters apart) that counts how often each byte / letter has been seen in the previous N (with N=4 or N=14) characters. The histogram is only updated at the "head" when a new byte is examined, and later at the "tail", which is always N bytes behind the head and decrements the histogram bins again. Every time a histogram bin changes its value from or to zero, a second counter is incremented or decremented; effectively, this counter tells how many histogram bins are non-zero, i.e. how many distinct characters are found in the last N bytes. If that number reaches N, we've found a match.

* Part 1, Python: 86 bytes, <100 ms
* Part 2, Python: 88 bytes, <100 ms
* Parts 1+2, x86 DOS Assembly: 142 bytes (assembled)
