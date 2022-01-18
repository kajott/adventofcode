# 2021, Day 18: Snailfish

You descend into the ocean trench and encounter some [snailfish](https://en.wikipedia.org/wiki/Snailfish). They say they saw the sleigh keys! They'll even tell you which direction the keys went if you help one of the smaller snailfish with his _math homework_.

## Part 1

Snailfish numbers aren't like regular numbers. Instead, every snailfish number is a _pair_ - an ordered list of two elements. Each element of the pair can be either a regular number or another pair.

Pairs are written as `[x,y]`, where `x` and `y` are the elements within the pair. Here are some example snailfish numbers, one snailfish number per line:

    [1,2]
    [[1,2],3]
    [9,[8,7]]
    [[1,9],[8,5]]
    [[[[1,2],[3,4]],[[5,6],[7,8]]],9]
    [[[9,[3,8]],[[0,9],6]],[[[3,7],[4,9]],3]]
    [[[[1,3],[5,3]],[[1,3],[8,7]]],[[[4,9],[6,9]],[[8,2],[7,3]]]]
    

This snailfish homework is about _addition_. To add two snailfish numbers, form a pair from the left and right parameters of the addition operator. For example, `[1,2]` + `[[3,4],5]` becomes `[[1,2],[[3,4],5]]`.

There's only one problem: _snailfish numbers must always be reduced_, and the process of adding two snailfish numbers can result in snailfish numbers that need to be reduced.

To _reduce a snailfish number_, you must repeatedly do the first action in this list that applies to the snailfish number:

*   If any pair is _nested inside four pairs_, the leftmost such pair _explodes_.
*   If any regular number is _10 or greater_, the leftmost such regular number _splits_.

Once no action in the above list applies, the snailfish number is reduced.

During reduction, at most one action applies, after which the process returns to the top of the list of actions. For example, if _split_ produces a pair that meets the _explode_ criteria, that pair _explodes_ before other _splits_ occur.

To _explode_ a pair, the pair's left value is added to the first regular number to the left of the exploding pair (if any), and the pair's right value is added to the first regular number to the right of the exploding pair (if any). Exploding pairs will always consist of two regular numbers. Then, the entire exploding pair is replaced with the regular number `0`.

Here are some examples of a single explode action:

*   `[[[[[9,8],1],2],3],4]` becomes `[[[[0,9],2],3],4]` (the `9` has no regular number to its left, so it is not added to any regular number).
*   `[7,[6,[5,[4,[3,2]]]]]` becomes `[7,[6,[5,[7,0]]]]` (the `2` has no regular number to its right, and so it is not added to any regular number).
*   `[[6,[5,[4,[3,2]]]],1]` becomes `[[6,[5,[7,0]]],3]`.
*   `[[3,[2,[1,[7,3]]]],[6,[5,[4,[3,2]]]]]` becomes `[[3,[2,[8,0]]],[9,[5,[4,[3,2]]]]]` (the pair `[3,2]` is unaffected because the pair `[7,3]` is further to the left; `[3,2]` would explode on the next action).
*   `[[3,[2,[8,0]]],[9,[5,[4,[3,2]]]]]` becomes `[[3,[2,[8,0]]],[9,[5,[7,0]]]]`.

To _split_ a regular number, replace it with a pair; the left element of the pair should be the regular number divided by two and rounded _down_, while the right element of the pair should be the regular number divided by two and rounded _up_. For example, `10` becomes `[5,5]`, `11` becomes `[5,6]`, `12` becomes `[6,6]`, and so on.

Here is the process of finding the reduced result of `[[[[4,3],4],4],[7,[[8,4],9]]]` + `[1,1]`:

    after addition: [[[[[4,3],4],4],[7,[[8,4],9]]],[1,1]]
    after explode:  [[[[0,7],4],[7,[[8,4],9]]],[1,1]]
    after explode:  [[[[0,7],4],[15,[0,13]]],[1,1]]
    after split:    [[[[0,7],4],[[7,8],[0,13]]],[1,1]]
    after split:    [[[[0,7],4],[[7,8],[0,[6,7]]]],[1,1]]
    after explode:  [[[[0,7],4],[[7,8],[6,0]]],[8,1]]
    

Once no reduce actions apply, the snailfish number that remains is the actual result of the addition operation: `[[[[0,7],4],[[7,8],[6,0]]],[8,1]]`.

The homework assignment involves adding up a _list of snailfish numbers_ (your puzzle input). The snailfish numbers are each listed on a separate line. Add the first snailfish number and the second, then add that result and the third, then add that result and the fourth, and so on until all numbers in the list have been used once.

For example, the final sum of this list is `[[[[1,1],[2,2]],[3,3]],[4,4]]`:

    [1,1]
    [2,2]
    [3,3]
    [4,4]
    

The final sum of this list is `[[[[3,0],[5,3]],[4,4]],[5,5]]`:

    [1,1]
    [2,2]
    [3,3]
    [4,4]
    [5,5]
    

The final sum of this list is `[[[[5,0],[7,4]],[5,5]],[6,6]]`:

    [1,1]
    [2,2]
    [3,3]
    [4,4]
    [5,5]
    [6,6]
    

Here's a slightly larger example:

    [[[0,[4,5]],[0,0]],[[[4,5],[2,6]],[9,5]]]
    [7,[[[3,7],[4,3]],[[6,3],[8,8]]]]
    [[2,[[0,8],[3,4]]],[[[6,7],1],[7,[1,6]]]]
    [[[[2,4],7],[6,[0,5]]],[[[6,8],[2,8]],[[2,1],[4,5]]]]
    [7,[5,[[3,8],[1,4]]]]
    [[2,[2,2]],[8,[8,1]]]
    [2,9]
    [1,[[[9,3],9],[[9,0],[0,7]]]]
    [[[5,[7,4]],7],1]
    [[[[4,2],2],6],[8,7]]
    

The final sum `[[[[8,7],[7,7]],[[8,6],[7,7]]],[[[0,7],[6,6]],[8,7]]]` is found after adding up the above snailfish numbers:

      [[[0,[4,5]],[0,0]],[[[4,5],[2,6]],[9,5]]]
    + [7,[[[3,7],[4,3]],[[6,3],[8,8]]]]
    = [[[[4,0],[5,4]],[[7,7],[6,0]]],[[8,[7,7]],[[7,9],[5,0]]]]
    
      [[[[4,0],[5,4]],[[7,7],[6,0]]],[[8,[7,7]],[[7,9],[5,0]]]]
    + [[2,[[0,8],[3,4]]],[[[6,7],1],[7,[1,6]]]]
    = [[[[6,7],[6,7]],[[7,7],[0,7]]],[[[8,7],[7,7]],[[8,8],[8,0]]]]
    
      [[[[6,7],[6,7]],[[7,7],[0,7]]],[[[8,7],[7,7]],[[8,8],[8,0]]]]
    + [[[[2,4],7],[6,[0,5]]],[[[6,8],[2,8]],[[2,1],[4,5]]]]
    = [[[[7,0],[7,7]],[[7,7],[7,8]]],[[[7,7],[8,8]],[[7,7],[8,7]]]]
    
      [[[[7,0],[7,7]],[[7,7],[7,8]]],[[[7,7],[8,8]],[[7,7],[8,7]]]]
    + [7,[5,[[3,8],[1,4]]]]
    = [[[[7,7],[7,8]],[[9,5],[8,7]]],[[[6,8],[0,8]],[[9,9],[9,0]]]]
    
      [[[[7,7],[7,8]],[[9,5],[8,7]]],[[[6,8],[0,8]],[[9,9],[9,0]]]]
    + [[2,[2,2]],[8,[8,1]]]
    = [[[[6,6],[6,6]],[[6,0],[6,7]]],[[[7,7],[8,9]],[8,[8,1]]]]
    
      [[[[6,6],[6,6]],[[6,0],[6,7]]],[[[7,7],[8,9]],[8,[8,1]]]]
    + [2,9]
    = [[[[6,6],[7,7]],[[0,7],[7,7]]],[[[5,5],[5,6]],9]]
    
      [[[[6,6],[7,7]],[[0,7],[7,7]]],[[[5,5],[5,6]],9]]
    + [1,[[[9,3],9],[[9,0],[0,7]]]]
    = [[[[7,8],[6,7]],[[6,8],[0,8]]],[[[7,7],[5,0]],[[5,5],[5,6]]]]
    
      [[[[7,8],[6,7]],[[6,8],[0,8]]],[[[7,7],[5,0]],[[5,5],[5,6]]]]
    + [[[5,[7,4]],7],1]
    = [[[[7,7],[7,7]],[[8,7],[8,7]]],[[[7,0],[7,7]],9]]
    
      [[[[7,7],[7,7]],[[8,7],[8,7]]],[[[7,0],[7,7]],9]]
    + [[[[4,2],2],6],[8,7]]
    = [[[[8,7],[7,7]],[[8,6],[7,7]]],[[[0,7],[6,6]],[8,7]]]
    

To check whether it's the right answer, the snailfish teacher only checks the _magnitude_ of the final sum. The magnitude of a pair is 3 times the magnitude of its left element plus 2 times the magnitude of its right element. The magnitude of a regular number is just that number.

For example, the magnitude of `[9,1]` is `3*9 + 2*1 = `_`29`_; the magnitude of `[1,9]` is `3*1 + 2*9 = `_`21`_. Magnitude calculations are recursive: the magnitude of `[[9,1],[1,9]]` is `3*29 + 2*21 = `_`129`_.

Here are a few more magnitude examples:

*   `[[1,2],[[3,4],5]]` becomes _`143`_.
*   `[[[[0,7],4],[[7,8],[6,0]]],[8,1]]` becomes _`1384`_.
*   `[[[[1,1],[2,2]],[3,3]],[4,4]]` becomes _`445`_.
*   `[[[[3,0],[5,3]],[4,4]],[5,5]]` becomes _`791`_.
*   `[[[[5,0],[7,4]],[5,5]],[6,6]]` becomes _`1137`_.
*   `[[[[8,7],[7,7]],[[8,6],[7,7]]],[[[0,7],[6,6]],[8,7]]]` becomes _`3488`_.

So, given this example homework assignment:

    [[[0,[5,8]],[[1,7],[9,6]]],[[4,[1,2]],[[1,4],2]]]
    [[[5,[2,8]],4],[5,[[9,9],0]]]
    [6,[[[6,2],[5,6]],[[7,6],[4,7]]]]
    [[[6,[0,7]],[0,9]],[4,[9,[9,0]]]]
    [[[7,[6,4]],[3,[1,3]]],[[[5,5],1],9]]
    [[6,[[7,3],[3,2]]],[[[3,8],[5,7]],4]]
    [[[[5,4],[7,7]],8],[[8,3],8]]
    [[9,3],[[9,9],[6,[4,9]]]]
    [[2,[[7,7],7]],[[5,8],[[9,3],[0,2]]]]
    [[[[5,2],5],[8,[3,7]]],[[5,[7,5]],[4,4]]]
    

The final sum is:

    [[[[6,6],[7,6]],[[7,7],[7,0]]],[[[7,7],[7,7]],[[7,8],[9,9]]]]

The magnitude of this final sum is _`4140`_.

Add up all of the snailfish numbers from the homework assignment in the order they appear. _What is the magnitude of the final sum?_

Your puzzle answer was `4469`.


## Part 2

You notice a second question on the back of the homework assignment:

What is the largest magnitude you can get from adding only two of the snailfish numbers?

Note that snailfish addition is not [commutative](https://en.wikipedia.org/wiki/Commutative_property) - that is, `x + y` and `y + x` can produce different results.

Again considering the last example homework assignment above:

    [[[0,[5,8]],[[1,7],[9,6]]],[[4,[1,2]],[[1,4],2]]]
    [[[5,[2,8]],4],[5,[[9,9],0]]]
    [6,[[[6,2],[5,6]],[[7,6],[4,7]]]]
    [[[6,[0,7]],[0,9]],[4,[9,[9,0]]]]
    [[[7,[6,4]],[3,[1,3]]],[[[5,5],1],9]]
    [[6,[[7,3],[3,2]]],[[[3,8],[5,7]],4]]
    [[[[5,4],[7,7]],8],[[8,3],8]]
    [[9,3],[[9,9],[6,[4,9]]]]
    [[2,[[7,7],7]],[[5,8],[[9,3],[0,2]]]]
    [[[[5,2],5],[8,[3,7]]],[[5,[7,5]],[4,4]]]
    

The largest magnitude of the sum of any two snailfish numbers in this list is _`3993`_. This is the magnitude of `[[2,[[7,7],7]],[[5,8],[[9,3],[0,2]]]]` + `[[[0,[5,8]],[[1,7],[9,6]]],[[4,[1,2]],[[1,4],2]]]`, which reduces to `[[[[7,8],[6,6]],[[6,0],[7,7]]],[[[7,8],[8,8]],[[7,9],[0,6]]]]`.

_What is the largest magnitude of any sum of two different snailfish numbers from the homework assignment?_

Your puzzle answer was `4770`.


## Solution Notes

There's no major pitfalls in this puzzle, except that it's just a tedious and boring ... well, homework. One might be tempted to implement this using nested lists (because that's what they are, right?), but searching for neighboring scalar values across all hierarchy levels as part of the explode operation is a highly complex operation itself, so I just "flattened" the lists with special sentinel values for `[` and `]` and omitting `,`. That works quite well, though I'm not at all sure whether it's the best way to do things. That's especially true for the golf versions.

* Part 1, Python: 560 bytes, ~350 ms
* Part 2, Python: 622 bytes, ~4 s
