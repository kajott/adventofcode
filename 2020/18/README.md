# 2020, Day 18: Operation Order

As you look out the window and notice a heavily-forested continent slowly appear over the horizon, you are interrupted by the child sitting next to you. They're curious if you could help them with their math homework.

Unfortunately, it seems like this "math" [follows different rules](https://www.youtube.com/watch?v=3QtRK7Y2pPU&t=15) than you remember.

## Part 1

The homework (your puzzle input) consists of a series of expressions that consist of addition (`+`), multiplication (`*`), and parentheses (`(...)`). Just like normal math, parentheses indicate that the expression inside must be evaluated before it can be used by the surrounding expression. Addition still finds the sum of the numbers on both sides of the operator, and multiplication still finds the product.

However, the rules of _operator precedence_ have changed. Rather than evaluating multiplication before addition, the operators have the _same precedence_, and are evaluated left-to-right regardless of the order in which they appear.

For example, the steps to evaluate the expression `1 + 2 * 3 + 4 * 5 + 6` are as follows:

    1 + 2 * 3 + 4 * 5 + 6
      3   * 3 + 4 * 5 + 6
          9   + 4 * 5 + 6
             13   * 5 + 6
                 65   + 6
                     71
    

Parentheses can override this order; for example, here is what happens if parentheses are added to form `1 + (2 * 3) + (4 * (5 + 6))`:

    1 + (2 * 3) + (4 * (5 + 6))
    1 +    6    + (4 * (5 + 6))
         7      + (4 * (5 + 6))
         7      + (4 *   11   )
         7      +     44
                51
    

Here are a few more examples:

*   `2 * 3 + (4 * 5)` becomes _`26`_.
*   `5 + (8 * 3 + 9 + 3 * 4 * 3)` becomes _`437`_.
*   `5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))` becomes _`12240`_.
*   `((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2` becomes _`13632`_.

Before you can help with the homework, you need to understand it yourself. _Evaluate the expression on each line of the homework; what is the sum of the resulting values?_

Your puzzle answer was `4491283311856`.

## Part 2

You manage to answer the child's questions and they finish part 1 of their homework, but get stuck when they reach the next section: _advanced_ math.

Now, addition and multiplication have _different_ precedence levels, but they're not the ones you're familiar with. Instead, addition is evaluated _before_ multiplication.

For example, the steps to evaluate the expression `1 + 2 * 3 + 4 * 5 + 6` are now as follows:

    1 + 2 * 3 + 4 * 5 + 6
      3   * 3 + 4 * 5 + 6
      3   *   7   * 5 + 6
      3   *   7   *  11
         21       *  11
             231
    

Here are the other examples from above:

*   `1 + (2 * 3) + (4 * (5 + 6))` still becomes _`51`_.
*   `2 * 3 + (4 * 5)` becomes _`46`_.
*   `5 + (8 * 3 + 9 + 3 * 4 * 3)` becomes _`1445`_.
*   `5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))` becomes _`669060`_.
*   `((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2` becomes _`23340`_.

_What do you get if you add up the results of evaluating the homework problems using these new rules?_

Your puzzle answer was `68852578641904`.


## Solution Notes

This is all about writing a parser and evaluator with (custom) operator precedence rules -- a thing I always hated. For part 1, this is relatively simple, as there are only parentheses to take care of. Part 2, however, requires a full-blown parser with parenthesis support and at least two levels of precedence. There are many algorithms to choose from; I opted for the [shunting-yard algorithm](https://en.wikipedia.org/wiki/Shunting-yard_algorithm), which is simple enough and converts an expression from infix notation into postfix notation (a.k.a. reverse polish notation, RPN) which, in turn, is easy to evaluate. I'm not 100% sure that this is the best algorithm to use in terms of golfability, but I hate this whole problem field enough to not care and keep it at that.

* Part 1, Python: 263 bytes, <100 ms
* Part 2, Python: 392 bytes, <100 ms
