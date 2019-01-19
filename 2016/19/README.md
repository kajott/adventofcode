# 2016, Day 19: An Elephant Named Joseph

The Elves contact you over a highly secure emergency channel. Back at the North Pole, the Elves are busy misunderstanding [White Elephant parties](https://en.wikipedia.org/wiki/White_elephant_gift_exchange).

## Part 1

Each Elf brings a present. They all sit in a circle, numbered starting with position `1`. Then, starting with the first Elf, they take turns stealing all the presents from the Elf to their left. An Elf with no presents is removed from the circle and does not take turns.

For example, with five Elves (numbered `1` to `5`):

      1
    5   2
     4 3
    

*   Elf `1` takes Elf `2`'s present.
*   Elf `2` has no presents and is skipped.
*   Elf `3` takes Elf `4`'s present.
*   Elf `4` has no presents and is also skipped.
*   Elf `5` takes Elf `1`'s two presents.
*   Neither Elf `1` nor Elf `2` have any presents, so both are skipped.
*   Elf `3` takes Elf `5`'s three presents.

So, with _five_ Elves, the Elf that sits starting in position `3` gets all the presents.

With the number of Elves given in your puzzle input, _which Elf gets all the presents?_

Your puzzle answer was `1834903`.

## Part 2

Realizing the folly of their present-exchange rules, the Elves agree to instead steal presents from the Elf _directly across the circle_. If two Elves are across the circle, the one on the left (from the perspective of the stealer) is stolen from. The other rules remain unchanged: Elves with no presents are removed from the circle entirely, and the other elves move in slightly to keep the circle evenly spaced.

For example, with five Elves (again numbered `1` to `5`):

*   The Elves sit in a circle; Elf `1` goes first:
    
          1
        5   2
         4 3
        
    
*   Elves `3` and `4` are across the circle; Elf `3`'s present is stolen, being the one to the left. Elf `3` leaves the circle, and the rest of the Elves move in:
    
          1           1
        5   2  -->  5   2
         4 -          4
        
    
*   Elf `2` steals from the Elf directly across the circle, Elf `5`:
    
          1         1 
        -   2  -->     2
          4         4 
        
    
*   Next is Elf `4` who, choosing between Elves `1` and `2`, steals from Elf `1`:
    
         -          2  
            2  -->
         4          4
        
    
*   Finally, Elf `2` steals from Elf `4`:
    
         2
            -->  2  
         -
        
    

So, with _five_ Elves, the Elf that sits starting in position `2` gets all the presents.

With the number of Elves given in your puzzle input, _which Elf now gets all the presents?_

Your puzzle answer was `1420280`.


## Solution Notes

Part 2 is constructed in such a way that naive solutions fall apart in terms of runtime performance. Regardless of whether an array or a list is used, complexity is always O(n²) -- you just get to choose whether item deletion or list pointer advancement kills you. A C implementation doesn't help much either.

The salvaging trick is to use a list and keep the half-way pointer around: Move it with deletions, and on every second turn, move it an additional element. This makes a C implementation near-instantaneous (so much so that there's no discernible difference between using optimization or not; at least not when compile times are factored in) and a Python implementation bearable.

* Part 1, Python: 131 bytes, ~1.5 s
* Part 2, Python: 166 bytes, ~8 s
* Part 2, C: 276 bytes, ~100 ms
