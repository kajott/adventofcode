# [2021, Day 21: Dirac Dice](https://adventofcode.com/2021/day/21)

The input consists of the single-digit starting positions of two players on a circular playfield with 10 spaces. The two players make their moves in alternating order. Each move is performed by rolling a die three times, adding their results, moving the indicated number of places forwards, and adding the number of the space the player ends up on to their score.

**Part 1** asks to simulate a game until the first player reaches at total score of 1000, using a "deterministic die" that rolls the numbers 1 to 100 in sequence and then repeats.

For **part 2**, a "Dirac die" is used instead. It only rolls the numbers 1 to 3, but *at the same time*, i.e. there are multiple possible outcomes. The tasks asks for the number of outcomes for a game that stops when the first player reaches a total score of 21.


## Solution Notes

Part 1 is just a small and easy starter dish.

Part 2, however, is essentially impossible to solve with any straightforward algorithm. You just have to **know** that you're supposed to encode the game state as a 5D vector (with score and position of both players, and the current player ID) and implement a function that recursively explores the derivative game states, with caching for already visited states, returning a 2-tuple of winning universes for both players. This is _incredibly_ hard to come up with.

* Part 1, Python: 194 bytes, <100 ms
* Part 2, Python: 346 bytes, ~250 ms
