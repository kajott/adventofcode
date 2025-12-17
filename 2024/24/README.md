# 2024, Day 24: Crossed Wires


## Solution Notes

Part 1 is just simulation. My initial implementation kept track of gates that haven't been evaluated yet because the inputs weren't ready, but for golf's sake, I just let the entire gateware run as often as there are gates, thus making sure that the output stabilized.

Part 2 is a totally different beast. It isn't reverse engineering per se, as the task description states upfront what the circuit is supposed to do, but since it doesn't describe _how_ it's done, some kind of visualization is basically required to make sense of the input. This turns out to be a perfectly normal 45-bit ripple-carry adder, with two half adders (XOR/AND pairs on the same inputs) and one OR (to combine the carry bits) per bit position, for a total of 89 ANDs and XORs each, plus 44 ORs. Thankfully, for all inputs I've seen so far, the defects put into the design are all only swaps _within_ the logic of a bit position; there are no weird bit-5-to-bit-23 crossovers or some such.

Even with that background knowledge, it's not trivial to come up with an _algorithmic_ solution to the problem. Like many others, I got my gold star during the contest by manually examining a diagram of the circuit and writing down the signal names I encountered that were wired incorrectly. It takes a few heuristics to determine the signals that are suspicious:
- All outputs of AND gates (half-adder carry outputs) have to go into OR gates (carry combiners), except the carry of the very first bit.
- All outputs of OR gates (full-adder carry outputs) have to go into half-adders of the next bit, except for the last one, which produces the MSB of the result.
- All outputs from XOR gates (half-adder sum outputs) have to go into either another half adder (if it's the first half-adder that sums `xNN` and `yNN`), or into a `zNN` output bit (if it's the second half-adder that adds the carries).
- The outputs from XOR gates that have only `xNN`/`yNN` inputs have to go into half-adders, whose XOR outputs, in turn, must be a `zNN` output bit.

These four rules combined can find all the incorrect wires in my input. Golfing those was great fun and uses every trick in the book.

* Part 1, Python: 270 bytes, <100 ms
* Part 2, Python: 401 bytes, <100 ms
