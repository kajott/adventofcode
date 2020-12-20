# 2020, Day 6: Custom Customs

As your flight approaches the regional airport where you'll switch to a much larger plane, [customs declaration forms](https://en.wikipedia.org/wiki/Customs_declaration) are distributed to the passengers.

## Part 1

The form asks a series of 26 yes-or-no questions marked `a` through `z`. All you need to do is identify the questions for which _anyone in your group_ answers "yes". Since your group is just you, this doesn't take very long.

However, the person sitting next to you seems to be experiencing a language barrier and asks if you can help. For each of the people in their group, you write down the questions for which they answer "yes", one per line. For example:

    abcx
    abcy
    abcz
    

In this group, there are _`6`_ questions to which anyone answered "yes": `a`, `b`, `c`, `x`, `y`, and `z`. (Duplicate answers to the same question don't count extra; each question counts at most once.)

Another group asks for your help, then another, and eventually you've collected answers from every group on the plane (your puzzle input). Each group's answers are separated by a blank line, and within each group, each person's answers are on a single line. For example:

    abc
    
    a
    b
    c
    
    ab
    ac
    
    a
    a
    a
    a
    
    b
    

This list represents answers from five groups:

*   The first group contains one person who answered "yes" to _`3`_ questions: `a`, `b`, and `c`.
*   The second group contains three people; combined, they answered "yes" to _`3`_ questions: `a`, `b`, and `c`.
*   The third group contains two people; combined, they answered "yes" to _`3`_ questions: `a`, `b`, and `c`.
*   The fourth group contains four people; combined, they answered "yes" to only _`1`_ question, `a`.
*   The last group contains one person who answered "yes" to only _`1`_ question, `b`.

In this example, the sum of these counts is `3 + 3 + 3 + 1 + 1` = _`11`_.

For each group, count the number of questions to which anyone answered "yes". _What is the sum of those counts?_

Your puzzle answer was `6930`.

## Part 2

As you finish the last group's customs declaration, you notice that you misread one word in the instructions:

You don't need to identify the questions to which _anyone_ answered "yes"; you need to identify the questions to which _everyone_ answered "yes"!

Using the same example as above:

    abc
    
    a
    b
    c
    
    ab
    ac
    
    a
    a
    a
    a
    
    b
    

This list represents answers from five groups:

*   In the first group, everyone (all 1 person) answered "yes" to _`3`_ questions: `a`, `b`, and `c`.
*   In the second group, there is _no_ question to which everyone answered "yes".
*   In the third group, everyone answered yes to only _`1`_ question, `a`. Since some people did not answer "yes" to `b` or `c`, they don't count.
*   In the fourth group, everyone answered yes to only _`1`_ question, `a`.
*   In the fifth group, everyone (all 1 person) answered "yes" to _`1`_ question, `b`.

In this example, the sum of these counts is `3 + 0 + 1 + 1 + 1` = _`6`_.

For each group, count the number of questions to which _everyone_ answered "yes". _What is the sum of those counts?_

Your puzzle answer was `3585`.


## Solution Notes

One of the cases where you can see exactly what part 2 is going to be while working on part 1.

Again, parsing is the most involved aspect of the task, everything else is just set unions and intersections. A nice optimization for part 1 is that it's not even required to split the answers into individual persons -- the union can simply be done across all letters in a group, only discarding the newline characters.

* Part 1, Python: 77 bytes, <100 ms
* Part 2, Python: 133 bytes, <100 ms
