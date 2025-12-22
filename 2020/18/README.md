# [2020, Day 18: Operation Order](https://adventofcode.com/2020/day/18)

The input consists of (typically) 375 lines of simple math problems, using only single-digit numbers, the `+` and `*` operators and up to two levels of nested braces.

The semantics of the `+` and `*` operators are the usual addition and multiplication, respectively; however the operator precedence rules changed.

**Part 1** asks for the sum of all results with **no** operator precedence (i.e. `+` and `*` are evaluated stricly left-to-right).

**Part 2** asks for the sum of all results with **inverted** operator precedence (i.e. `+` and is evaluated _before_ `*`).


## Solution Notes

This is all about writing a parser and evaluator with (custom) operator precedence rules -- a thing I always hated. For part 1, this is relatively simple, as there are only parentheses to take care of. Part 2, however, requires a full-blown parser with parenthesis support and at least two levels of precedence. There are many algorithms to choose from; I opted for the [shunting-yard algorithm](https://en.wikipedia.org/wiki/Shunting-yard_algorithm), which is simple enough and converts an expression from infix notation into postfix notation (a.k.a. reverse polish notation, RPN) which, in turn, is easy to evaluate.

An alternate implementation is possible though, with a little bit of cheating: By defining a custom class with overloaded operators that swap the meaning of multiplication and addition, and some pre-processing of the input string, the whole thing can be `eval`'d by Python itself, leading to a much cleaner, shorter and faster solution.

* Part 1, Python: 263 bytes, <100 ms
* Part 2, Python (manual parsing): 392 bytes, <100 ms
* Part 2, Python (`eval` hack): 236 bytes, <100 ms
