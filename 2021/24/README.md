# 2021, Day 24: Arithmetic Logic Unit


## Solution Notes

A reverse engineering puzzle that is made extra complicated by the complete lack of test vectors to check it against. It requires a multi-step solution process **_(spoilers ahead!)_**:

* The MONAD algorithm consists of 14 repetitions of identical code. The individual "rounds" only differ in three numerical constants. 

* In each round, the `z` value is modified in two ways:
  * Exactly half of the rounds divide it by 26. (This is controlled by one of the aforementioned per-round constants.)
  * Unless the round's input value matches a certain value, `z` is multiplied by 26 again and a small number is added.
  
* Since the goal is to get `z` down to zero, it is imperative that the condition that prevents the multiplication and addition from happening is fulfilled as often as possible. Unfortunately, this can't be done for every round, because the value the input is compared against has a somewhat larger range than just 1 to 9 (in my input, it's -14 to 39).

* In particular, if it's not possible to pick an input value that prevents multiplication in a round that has division enabled, this would make the division useless. If that happens, the result of `z=0` can't be reached.

* For the 7 rounds where no division occurs, the input digits can be chosen freely, unless they cause a division in a later round to be counteracted.

I stopped further research at this point; there may be some more ways to constrain the search space, but 9^7 = 4.8 million combinations already are quite feasible.

* Part 1, Python: 281 bytes, ~10 s
* Part 2, Python: 278 bytes, ~1 s
