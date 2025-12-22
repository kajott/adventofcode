# [2019, Day 23: Category Six](https://adventofcode.com/2019/day/23)

This puzzle uses the Intcode virtual machine that has been fully specified in [day 9](../09), and which has been used a lot during AoC 2019.

The input for this task consists of an Intcode core dump of (typically) 2250 words.

The task simulates a network of 50 Intcode VMs, all running the same software. At startup, the program asks for the instance's network address, a number between 0 and 49. After that, the programs enter a loop that sends and receives network traffic.

A network packet consists of two numbers. To send a packet, a VM outputs the target address and the two numbers. To receive a packet, the VM expects to get sent the two numbers, or -1 if there's no packet in the receive queue.

Address 255 has a special meaaning: It is also device on the network that remembers the last packet sent to it. Once all other VMs are idle (i.e. stuck in the wait-for-input-packet loop), it sends the remembered packet to address 0, causing the network to resume operations.

**Part 1** asks for the first packet that is sent to address 255.

**Part 2** asks for the first packet that is sent from address 255 to addres 0 the second time in a row with identical data.


## Solution Notes

A nice and simple puzzle with no unpleasant surprises.

For golfing, I first did the obvious thing and turned the 50 machines into class instances. For the second revision, I put all the machine state (IP and RB registers, input and output queue) into the main memory dictionary at addresses `-1` to `-4`, which is safe because negative addresses are otherwise forbidden by the Intcode spec. This makes register and queue access slighly longer (`X.p` becomes `X[-1]`, +1 byte), but this is far outweighed by the shorter memory accesses (`X.m[i]` -> `X[i]`, -2 bytes) and instantiation.

* Part 1, Python (machines as classes): 690 bytes, ~150 ms
* Part 1, Python (machines as dictionaries): 668 bytes, ~150 ms
* Part 2, Python: 738 bytes, ~1 s
