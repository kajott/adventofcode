# [2023 Day 20: Pulse Propagation](https://adventofcode.com/2023/day/20)

The input consists of a netlist of (typically) 60 binary gates, named with random 2-letter identifiers. The gates are pulse-activated, not level activated. Each gate is either a flip-flop that toggles when receiving a low pulse, or a NAND gate that emits a high pulse when it receives any pulse on its two inputs, or a low pulse if the last two pulses received on both inputs were high. Each gate's output is connected to 1 to 7 other gates. A special third type of gate, the "broadcaster", exists only once in the circuit and broadcasts an incoming pulse across all its outputs.

**Part 1** asks for the total numbers of high and low pulses processed by the entire circuit after sending 1000 low pulses into the broadcaster.

**Part 2** asks how many low pulses need to be sent into the broadcaster until a certain gate in the circuit receives a low pulse.


## Solution Notes

The puzzle description is quite elaborate and needs to be followed exactly, but apart from that, part 1 is quite simple.

Part 2, however, is a true complexity bomb. Brute force computation is out of the question, so the solution is really to reverse engineer the input and look what it does. In all reported cases from other users, the structure seems to be similar and the following observations can be made:
- The `broadcaster` node triggers four other nodes.
- The node that `rx` pulls from is a NAND gate ("conjunction") with four inputs.
  - Corollary: `rx` will only receive a low pulse if all of the four NAND inputs receive a high pulse.
- The paths between the four `broadcaster` outputs and pre-`rx` NAND inputs are disjoint and don't interact with each other.
- Each of the four subgraphs generates a period of N-1 low pulses followed by a single high pulse.
  - The period lengths are prime numbers.

With this knowledge (which has to be earned "the hard way"), the eventual solution is relatively straightforward: Let the simulation run until the periods for all four subgraphs are known (i.e. each subgraph has sent a high pulse to the final NAND gate), multiply the period lengths, and done.

But it's possible to do even better in terms of size and performance when exploiting the structure of the input. Visualized as a graph, it looks like this:

![graph of my AoC 2023/20 input](graph.svg)

It's interesting to note (a) how simple the structure is, and (b) how the period lengths can be directly derived from the graph as binary numbers: A FF with a signal going out to the NAND is a `1`, a FF with only a signal coming _in_ from the NAND is a `0`. The MSB is the FF that doesn't output to anything but the NAND (i.e. the bottom in the graph), the LSB (which is connected to the NAND in both directions) is always `1`.

* Part 1, Python: 476 bytes, ~100 ms
* Part 2, Python (simulation): 515 bytes, ~350 ms
* Part 2, Python (input graph parsing): 326 bytes, <100 ms
