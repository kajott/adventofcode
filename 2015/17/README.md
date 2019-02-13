# 2015, Day 17: No Such Thing as Too Much

The elves bought too much eggnog again - `150` liters this time. To fit it all into your refrigerator, you'll need to move it into smaller containers. You take an inventory of the capacities of the available containers.

## Part 1

For example, suppose you have containers of size `20`, `15`, `10`, `5`, and `5` liters. If you need to store `25` liters, there are four ways to do it:

*   `15` and `10`
*   `20` and `5` (the first `5`)
*   `20` and `5` (the second `5`)
*   `15`, `5`, and `5`

Filling all containers entirely, how many different _combinations of containers_ can exactly fit all `150` liters of eggnog?

Your puzzle answer was `654`.

## Part 2

While playing with all the containers in the kitchen, another load of eggnog arrives! The shipping and receiving department is requesting as many containers as you can spare.

Find the minimum number of containers that can exactly fit all `150` liters of eggnog. _How many different ways_ can you fill that number of containers and still hold exactly `150` litres?

In the example above, the minimum number of containers was two. There were three ways to use that many containers, and so the answer there would be `3`.

Your puzzle answer was `57`.


## Solution Notes

An O(2^n)-class puzzle that could have been a major headache if the problem size was large enough. Fortunately, this isn't the case, and brute force (barely) does the job here.

* Part 1, Python: 112 bytes, ~3 s
* Part 2, Python: 166 bytes, ~3 s
