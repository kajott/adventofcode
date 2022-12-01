# 2022, Day 1: Calorie Counting

Santa's reindeer typically eat regular reindeer food, but they need a lot of [magical energy](../../2018/25) to deliver presents on Christmas. For that, their favorite snack is a special type of _star_ fruit that only grows deep in the jungle. The Elves have brought you on their annual expedition to the grove where the fruit grows.

To supply enough magical energy, the expedition needs to retrieve a minimum of _fifty stars_ by December 25th. Although the Elves assure you that the grove has plenty of fruit, you decide to grab any fruit you see along the way, just in case.

Collect stars by solving puzzles. Two puzzles will be made available on each day in the Advent calendar; the second puzzle is unlocked when you complete the first. Each puzzle grants _one star_. Good luck!

## Part 1

The jungle must be too overgrown and difficult to navigate in vehicles or access from the air; the Elves' expedition traditionally goes on foot. As your boats approach land, the Elves begin taking inventory of their supplies. One important consideration is food - in particular, the number of _Calories_ each Elf is carrying (your puzzle input).

The Elves take turns writing down the number of Calories contained by the various meals, snacks, rations, etc. that they've brought with them, one item per line. Each Elf separates their own inventory from the previous Elf's inventory (if any) by a blank line.

For example, suppose the Elves finish writing their items' Calories and end up with the following list:

    1000
    2000
    3000
    
    4000
    
    5000
    6000
    
    7000
    8000
    9000
    
    10000
    

This list represents the Calories of the food carried by five Elves:

*   The first Elf is carrying food with `1000`, `2000`, and `3000` Calories, a total of _`6000`_ Calories.
*   The second Elf is carrying one food item with _`4000`_ Calories.
*   The third Elf is carrying food with `5000` and `6000` Calories, a total of _`11000`_ Calories.
*   The fourth Elf is carrying food with `7000`, `8000`, and `9000` Calories, a total of _`24000`_ Calories.
*   The fifth Elf is carrying one food item with _`10000`_ Calories.

In case the Elves get hungry and need extra snacks, they need to know which Elf to ask: they'd like to know how many Calories are being carried by the Elf carrying the _most_ Calories. In the example above, this is _`24000`_ (carried by the fourth Elf).

Find the Elf carrying the most Calories. _How many total Calories is that Elf carrying?_

Your puzzle answer was `72240`.

## Part 2

By the time you calculate the answer to the Elves' question, they've already realized that the Elf carrying the most Calories of food might eventually _run out of snacks_.

To avoid this unacceptable situation, the Elves would instead like to know the total Calories carried by the _top three_ Elves carrying the most Calories. That way, even if one of those Elves runs out of snacks, they still have two backups.

In the example above, the top three Elves are the fourth Elf (with `24000` Calories), then the third Elf (with `11000` Calories), then the fifth Elf (with `10000` Calories). The sum of the Calories carried by these three elves is _`45000`_.

Find the top three Elves carrying the most Calories. _How many Calories are those Elves carrying in total?_

Your puzzle answer was `210957`.

## Solution Notes

A nice and simple starter. The highest hurdle here is splitting the list into several sub-lists.

Just for fun, I also implemented a pure 16-bit DOS version, meant to run on the original IBM 5150 PC (albeit with at least 128k of RAM and DOS 2.0). The result is a 256-byte .COM-format program that reads `input.txt` and solves both parts in no time. On an emulated 5150, I measured around 2 seconds, _including_ the time it takes to load the program and data from floppy disk (which is very likely by far the largest part). <br>
The largest technical struggle in this implementation is the fact that everything requires 32-bit arithmetic, which needs to be performed in two halves on the 16-bit 8086/8088 CPU.

* Part 1, Python: 82 bytes, <100 ms
* Part 2, Python: 95 bytes, <100 ms
* Parts 1+2, 16-bit DOS Assembler: 256 bytes (compiled), ~2 s
