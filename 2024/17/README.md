# 2024, Day 17: Chronospatial Computer

The Historians push the button on their strange device, but this time, you all just feel like you're [falling](../../2018/06).

"Situation critical", the device announces in a familiar voice. "Bootstrapping process failed. Initializing debugger...."

The small handheld device suddenly unfolds into an entire computer! The Historians look around nervously before one of them tosses it to you.

## Part 1

This seems to be a 3-bit computer: its program is a list of 3-bit numbers (0 through 7), like `0,1,2,3`. The computer also has three _registers_ named `A`, `B`, and `C`, but these registers aren't limited to 3 bits and can instead hold any integer.

The computer knows _eight instructions_, each identified by a 3-bit number (called the instruction's _opcode_). Each instruction also reads the 3-bit number after it as an input; this is called its _operand_.

A number called the _instruction pointer_ identifies the position in the program from which the next opcode will be read; it starts at `0`, pointing at the first 3-bit number in the program. Except for jump instructions, the instruction pointer increases by `2` after each instruction is processed (to move past the instruction's opcode and its operand). If the computer tries to read an opcode past the end of the program, it instead _halts_.

So, the program `0,1,2,3` would run the instruction whose opcode is `0` and pass it the operand `1`, then run the instruction having opcode `2` and pass it the operand `3`, then halt.

There are two types of operands; each instruction specifies the type of its operand. The value of a _literal operand_ is the operand itself. For example, the value of the literal operand `7` is the number `7`. The value of a _combo operand_ can be found as follows:

*   Combo operands `0` through `3` represent literal values `0` through `3`.
*   Combo operand `4` represents the value of register `A`.
*   Combo operand `5` represents the value of register `B`.
*   Combo operand `6` represents the value of register `C`.
*   Combo operand `7` is reserved and will not appear in valid programs.

The eight instructions are as follows:

The _`adv`_ instruction (opcode _`0`_) performs _division_. The numerator is the value in the `A` register. The denominator is found by raising 2 to the power of the instruction's _combo_ operand. (So, an operand of `2` would divide `A` by `4` (`2^2`); an operand of `5` would divide `A` by `2^B`.) The result of the division operation is _truncated_ to an integer and then written to the `A` register.

The _`bxl`_ instruction (opcode _`1`_) calculates the [bitwise XOR](https://en.wikipedia.org/wiki/Bitwise_operation#XOR) of register `B` and the instruction's _literal_ operand, then stores the result in register `B`.

The _`bst`_ instruction (opcode _`2`_) calculates the value of its _combo_ operand [modulo](https://en.wikipedia.org/wiki/Modulo) 8 (thereby keeping only its lowest 3 bits), then writes that value to the `B` register.

The _`jnz`_ instruction (opcode _`3`_) does _nothing_ if the `A` register is `0`. However, if the `A` register is _not zero_, it _jumps_ by setting the instruction pointer to the value of its _literal_ operand; if this instruction jumps, the instruction pointer is _not_ increased by `2` after this instruction.

The _`bxc`_ instruction (opcode _`4`_) calculates the _bitwise XOR_ of register `B` and register `C`, then stores the result in register `B`. (For legacy reasons, this instruction reads an operand but _ignores_ it.)

The _`out`_ instruction (opcode _`5`_) calculates the value of its _combo_ operand modulo 8, then _outputs_ that value. (If a program outputs multiple values, they are separated by commas.)

The _`bdv`_ instruction (opcode _`6`_) works exactly like the `adv` instruction except that the result is stored in the _`B` register_. (The numerator is still read from the `A` register.)

The _`cdv`_ instruction (opcode _`7`_) works exactly like the `adv` instruction except that the result is stored in the _`C` register_. (The numerator is still read from the `A` register.)

Here are some examples of instruction operation:

*   If register `C` contains `9`, the program `2,6` would set register `B` to `1`.
*   If register `A` contains `10`, the program `5,0,5,1,5,4` would output `0,1,2`.
*   If register `A` contains `2024`, the program `0,1,5,4,3,0` would output `4,2,5,6,7,7,7,7,3,1,0` and leave `0` in register `A`.
*   If register `B` contains `29`, the program `1,7` would set register `B` to `26`.
*   If register `B` contains `2024` and register `C` contains `43690`, the program `4,0` would set register `B` to `44354`.

The Historians' strange device has finished initializing its debugger and is displaying some _information about the program it is trying to run_ (your puzzle input). For example:

    Register A: 729
    Register B: 0
    Register C: 0
    
    Program: 0,1,5,4,3,0

Your first task is to _determine what the program is trying to output_. To do this, initialize the registers to the given values, then run the given program, collecting any output produced by `out` instructions. (Always join the values produced by `out` instructions with commas.) After the above program halts, its final output will be `_4,6,3,5,6,3,5,2,1,0_`.

Using the information provided by the debugger, initialize the registers to the given values, then run the program. Once it halts, _what do you get if you use commas to join the values it output into a single string?_

Your puzzle answer was `2,0,4,2,7,0,1,0,3`.

## Part 2

Digging deeper in the device's manual, you discover the problem: this program is supposed to _output another copy of the program_! Unfortunately, the value in register `A` seems to have been corrupted. You'll need to find a new value to which you can initialize register `A` so that the program's output instructions produce an exact copy of the program itself.

For example:

    Register A: 2024
    Register B: 0
    Register C: 0
    
    Program: 0,3,5,4,3,0

This program outputs a copy of itself if register `A` is instead initialized to _`117440`_. (The original initial value of register `A`, `2024`, is ignored.)

_What is the lowest positive initial value for register `A` that causes the program to output a copy of itself?_

Your puzzle answer was `265601188299675`.

## Solution Notes

Part 1 is just straight implementation of the spec. Golfing this has been a lot of fun, including tricks like (mostly) branchless execution due to having a neutral fourth register that can be clobbered by operations that don't store anything in the three registers, using shifts to represent constant arrays, and a few other tricks.

Part 2 is a classical reverse engineering puzzle. Obviously, what the program outputs is somehow encoded in the `A` register on startup; the goal is then to set `A` such that the sequence of numbers forming the program is emitted. Now, how does that work? As it turns out, the program always performs some computation on the value of `A` and outputs that, then later shifts `A` three bits down (`adv 3`), and ends in a `jnz 0`. The values of `B` and `C` are always overwritten with each program run, so their initial value doesn't matter, and `A` is only updated by the aforementioned `adv 3` instruction. Essentially, this forms a loop of the form `do { out(f(A) & 7); A >>= 3; } while (A)`. The `f()` function can be anything &ndash; in practice, it seems to be in the form `f(A) = A ^ (const1 ^ const2) ^ (A >> ((A & 7) ^ const1))` (`^` = XOR), with `const1` and `const2` being 3-bit constants.

What this means is that every 3-bit group in `A` generates one output value, starting with the LSBs. For the program, which has length 16, this means that `A` is a 48-bit number, which also makes it clear that brute force is definitely not the way to go about this puzzle. Instead, the value of `A` can be constructed (almost literally) bit by bit, in reverse order: The value of `A` that generates the *last* instruction word has to be found (and there are just 8 possible values, so trying all of them is fine), and then `A` can be shifted up by 3 bits and again some value between 0 and 7 has to be added to get the second-to-last instruction, and so on. Multiple possible addends can result in the same value being output; in these cases, it's *not* sufficient to just take the minimum value, because it can (and does) turn out that sometimes, the necessary bit patterns can't be found to construct a later instruction word. Thus, a full DFS is required, but it's still plenty fast.

I solved part 2 in two ways: First, I had a version that encodes the function of my specific input directly in Python, but later on, I wrote a version that actually runs the program to produce the output. Obviously, the first version is much smaller, since it doesn't need the entire interpreter.

* Part 1, Python: 279 bytes, <100 ms
* Part 2, Python (puzzle input specific): 201 bytes, <100 ms
* Part 2, Python (generic): 391 bytes, <100 ms
