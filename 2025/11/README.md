# 2025, Day 11: Reactor

You hear some loud beeping coming from a hatch in the floor of the factory, so you decide to check it out. Inside, you find several large electrical conduits and a ladder.

Climbing down the ladder, you discover the source of the beeping: a large, toroidal reactor which powers the factory above. Some Elves here are hurriedly running between the reactor and a nearby server rack, apparently trying to fix something.

One of the Elves notices you and rushes over. "It's a good thing you're here! We just installed a new _server rack_, but we aren't having any luck getting the reactor to communicate with it!" You glance around the room and see a tangle of cables and devices running from the server rack to the reactor. She rushes off, returning a moment later with a list of the devices and their outputs (your puzzle input).

## Part 1

For example:

    aaa: you hhh
    you: bbb ccc
    bbb: ddd eee
    ccc: ddd eee fff
    ddd: ggg
    eee: out
    fff: out
    ggg: out
    hhh: ccc fff iii
    iii: out
    

Each line gives the name of a device followed by a list of the devices to which its outputs are attached. So, `bbb: ddd eee` means that device `bbb` has two outputs, one leading to device `ddd` and the other leading to device `eee`.

The Elves are pretty sure that the issue isn't due to any specific device, but rather that the issue is triggered by data following some specific _path_ through the devices. Data only ever flows from a device through its outputs; it can't flow backwards.

After dividing up the work, the Elves would like you to focus on the devices starting with the one next to you (an Elf hastily attaches a label which just says _`you`_) and ending with the main output to the reactor (which is the device with the label _`out`_).

To help the Elves figure out which path is causing the issue, they need you to find _every_ path from `you` to `out`.

In this example, these are all of the paths from `you` to `out`:

*   Data could take the connection from `you` to `bbb`, then from `bbb` to `ddd`, then from `ddd` to `ggg`, then from `ggg` to `out`.
*   Data could take the connection to `bbb`, then to `eee`, then to `out`.
*   Data could go to `ccc`, then `ddd`, then `ggg`, then `out`.
*   Data could go to `ccc`, then `eee`, then `out`.
*   Data could go to `ccc`, then `fff`, then `out`.

In total, there are _`5`_ different paths leading from `you` to `out`.

_How many different paths lead from `you` to `out`?_

Your puzzle answer was `696`.

## Part 2

Thanks in part to your analysis, the Elves have figured out a little bit about the issue. They now know that the problematic data path passes through both `dac` (a [digital-to-analog converter](https://en.wikipedia.org/wiki/Digital-to-analog_converter)) and `fft` (a device which performs a [fast Fourier transform](https://en.wikipedia.org/wiki/Fast_Fourier_transform)).

They're still not sure which specific path is the problem, and so they now need you to find every path from `svr` (the server rack) to `out`. However, the paths you find must all also visit both `dac` _and_ `fft` (in any order).

For example:

    svr: aaa bbb
    aaa: fft
    fft: ccc
    bbb: tty
    tty: ccc
    ccc: ddd eee
    ddd: hub
    hub: fff
    eee: dac
    dac: fff
    fff: ggg hhh
    ggg: out
    hhh: out
    

This new list of devices contains many paths from `svr` to `out`:

    svr,aaa,fft,ccc,ddd,hub,fff,ggg,out
    svr,aaa,fft,ccc,ddd,hub,fff,hhh,out
    svr,aaa,fft,ccc,eee,dac,fff,ggg,out
    svr,aaa,fft,ccc,eee,dac,fff,hhh,out
    svr,bbb,tty,ccc,ddd,hub,fff,ggg,out
    svr,bbb,tty,ccc,ddd,hub,fff,hhh,out
    svr,bbb,tty,ccc,eee,dac,fff,ggg,out
    svr,bbb,tty,ccc,eee,dac,fff,hhh,out
    

However, only _`2`_ paths from `svr` to `out` visit both `dac` and `fft`.

Find all of the paths that lead from `svr` to `out`. _How many of those paths visit both `dac` and `fft`?_

Your puzzle answer was `473741288064360`.


## Solution Notes

There's nothing special about this task: a plain DFS will do. In part 1, it doesn't even need memoization, as the relatively low result suggests.

Memoization is a must for part 2 though, and there are two principal ways to solve the puzzle with it. My first approach, which turned out to be the most size-effective, was to still search from `svr` to `out`, but keep track of the two-bit information whether `dac` and `fft` have been passed along the way. Another solution that many people use is to determine the results from all relevant sub-paths and multiply and add them together as needed. I implemented that one as well, but it doesn't give any tangible benefit compared to by initial solution.

* Part 1, Python: 131 bytes, <100 ms
* Part 2, Python (tagging): 208 bytes, <100 ms
* Part 2, Python (partial paths): 247 bytes, <100 ms
