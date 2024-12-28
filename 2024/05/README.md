# 2024, Day 5: Print Queue

Satisfied with their search on Ceres, the squadron of scholars suggests subsequently scanning the stationery stacks of sub-basement 17.

The North Pole printing department is busier than ever this close to Christmas, and while The Historians continue their search of this historically significant facility, an Elf operating a [very familiar printer](../../2017/01) beckons you over.

The Elf must recognize you, because they waste no time explaining that the new _sleigh launch safety manual_ updates won't print correctly. Failure to update the safety manuals would be dire indeed, so you offer your services.

## Part 1

Safety protocols clearly indicate that new pages for the safety manuals must be printed in a _very specific order_. The notation `X|Y` means that if both page number `X` and page number `Y` are to be produced as part of an update, page number `X` _must_ be printed at some point before page number `Y`.

The Elf has for you both the _page ordering rules_ and the _pages to produce in each update_ (your puzzle input), but can't figure out whether each update has the pages in the right order.

For example:

    47|53
    97|13
    97|61
    97|47
    75|29
    61|13
    75|53
    29|13
    97|29
    53|29
    61|53
    97|53
    61|29
    47|13
    75|47
    97|75
    47|61
    75|61
    47|29
    75|13
    53|13
    
    75,47,61,53,29
    97,61,53,29,13
    75,29,13
    75,97,47,61,53
    61,13,29
    97,13,75,29,47

The first section specifies the _page ordering rules_, one per line. The first rule, `47|53`, means that if an update includes both page number 47 and page number 53, then page number 47 _must_ be printed at some point before page number 53. (47 doesn't necessarily need to be _immediately_ before 53; other pages are allowed to be between them.)

The second section specifies the page numbers of each _update_. Because most safety manuals are different, the pages needed in the updates are different too. The first update, `75,47,61,53,29`, means that the update consists of page numbers 75, 47, 61, 53, and 29.

To get the printers going as soon as possible, start by identifying _which updates are already in the right order_.

In the above example, the first update (`75,47,61,53,29`) is in the right order:

*   `75` is correctly first because there are rules that put each other page after it: `75|47`, `75|61`, `75|53`, and `75|29`.
*   `47` is correctly second because 75 must be before it (`75|47`) and every other page must be after it according to `47|61`, `47|53`, and `47|29`.
*   `61` is correctly in the middle because 75 and 47 are before it (`75|61` and `47|61`) and 53 and 29 are after it (`61|53` and `61|29`).
*   `53` is correctly fourth because it is before page number 29 (`53|29`).
*   `29` is the only page left and so is correctly last.

Because the first update does not include some page numbers, the ordering rules involving those missing page numbers are ignored.

The second and third updates are also in the correct order according to the rules. Like the first update, they also do not include every page number, and so only some of the ordering rules apply - within each update, the ordering rules that involve missing page numbers are not used.

The fourth update, `75,97,47,61,53`, is _not_ in the correct order: it would print 75 before 97, which violates the rule `97|75`.

The fifth update, `61,13,29`, is also _not_ in the correct order, since it breaks the rule `29|13`.

The last update, `97,13,75,29,47`, is _not_ in the correct order due to breaking several rules.

For some reason, the Elves also need to know the _middle page number_ of each update being printed. Because you are currently only printing the correctly-ordered updates, you will need to find the middle page number of each correctly-ordered update. In the above example, the correctly-ordered updates are:

    75,47,61,53,29
    97,61,53,29,13
    75,29,13

These have middle page numbers of `61`, `53`, and `29` respectively. Adding these page numbers together gives _`143`_.

Of course, you'll need to be careful: the actual list of _page ordering rules_ is bigger and more complicated than the above example.

Determine which updates are already in the correct order. _What do you get if you add up the middle page number from those correctly-ordered updates?_

Your puzzle answer was `5091`.

## Part 2

While the Elves get to work printing the correctly-ordered updates, you have a little time to fix the rest of them.

For each of the _incorrectly-ordered updates_, use the page ordering rules to put the page numbers in the right order. For the above example, here are the three incorrectly-ordered updates and their correct orderings:

*   `75,97,47,61,53` becomes `97,75,`_`47`_`,61,53`.
*   `61,13,29` becomes `61,`_`29`_`,13`.
*   `97,13,75,29,47` becomes `97,75,`_`47`_`,29,13`.

After taking _only the incorrectly-ordered updates_ and ordering them correctly, their middle page numbers are `47`, `29`, and `47`. Adding these together produces _`123`_.

Find the updates which are not in the correct order. _What do you get if you add up the middle page numbers after correctly ordering just those updates?_

Your puzzle answer was `4681`.

## Solution Notes

The important part of this task is to **not** overthink it: While it might seem like this puzzle is about topological ordering, this approach will lead to some suffering because the rules themselves aren't cycle-free, only the rules exercised by each _update_ are. (Luckily, I did _not_ learn that the hard way; I just heard from other users who fell into this trap.)

The actually recommended way of doing things is as blunt as it gets: For each update, check the list of pages against all the rules. If all checks pass, it's a result for part 1; if they don't, swap the offending elements and repeat the entire checking process until the list stabilizes (which it always does, eventually) to get the result for part 2.

The slightly annoying aspect of this puzzle is indeed input parsing, at least as far as code golf is concerned. The approach that works best for part 1 (in the sense of "least amount of code") isn't really suitable for part 2, so I ended up with completely different ways of handling input between the parts.

* Part 1, Python: 199 bytes, ~150 ms
* Part 2, Python: 283 bytes, ~300 ms
* Parts 1+2, Python: 299 bytes, ~300 ms
