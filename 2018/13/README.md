# 2018, Day 13: Mine Cart Madness

A crop of this size requires significant logistics to transport produce, soil, fertilizer, and so on. The Elves are very busy pushing things around in _carts_ on some kind of rudimentary system of tracks they've come up with.

Seeing as how cart-and-track systems don't appear in recorded history for another 1000 years, the Elves seem to be making this up as they go along. They haven't even figured out how to avoid collisions yet.

## Part 1

You map out the tracks (your puzzle input) and see where you can help.

Tracks consist of straight paths (`|` and `-`), curves (`/` and `\`), and intersections (`+`). Curves connect exactly two perpendicular pieces of track; for example, this is a closed loop:

    /----\
    |    |
    |    |
    \----/
    

Intersections occur when two perpendicular paths cross. At an intersection, a cart is capable of turning left, turning right, or continuing straight. Here are two loops connected by two intersections:

    /-----\
    |     |
    |  /--+--\
    |  |  |  |
    \--+--/  |
       |     |
       \-----/
    

Several _carts_ are also on the tracks. Carts always face either up (`^`), down (`v`), left (`<`), or right (`>`). (On your initial map, the track under each cart is a straight path matching the direction the cart is facing.)

Each time a cart has the option to turn (by arriving at any intersection), it turns _left_ the first time, goes _straight_ the second time, turns _right_ the third time, and then repeats those directions starting again with _left_ the fourth time, _straight_ the fifth time, and so on. This process is independent of the particular intersection at which the cart has arrived - that is, the cart has no per-intersection memory.

Carts all move at the same speed; they take turns moving a single step at a time. They do this based on their _current location_: carts on the top row move first (acting from left to right), then carts on the second row move (again from left to right), then carts on the third row, and so on. Once each cart has moved one step, the process repeats; each of these loops is called a _tick_.

For example, suppose there are two carts on a straight track:

    |  |  |  |  |
    v  |  |  |  |
    |  v  v  |  |
    |  |  |  v  X
    |  |  ^  ^  |
    ^  ^  |  |  |
    |  |  |  |  |
    

First, the top cart moves. It is facing down (`v`), so it moves down one square. Second, the bottom cart moves. It is facing up (`^`), so it moves up one square. Because all carts have moved, the first tick ends. Then, the process repeats, starting with the first cart. The first cart moves down, then the second cart moves up - right into the first cart, colliding with it! (The location of the crash is marked with an `X`.) This ends the second and last tick.

Here is a longer example:

    /->-\        
    |   |  /----\
    | /-+--+-\  |
    | | |  | v  |
    \-+-/  \-+--/
      \------/   
    
    /-->\        
    |   |  /----\
    | /-+--+-\  |
    | | |  | |  |
    \-+-/  \->--/
      \------/   
    
    /---v        
    |   |  /----\
    | /-+--+-\  |
    | | |  | |  |
    \-+-/  \-+>-/
      \------/   
    
    /---\        
    |   v  /----\
    | /-+--+-\  |
    | | |  | |  |
    \-+-/  \-+->/
      \------/   
    
    /---\        
    |   |  /----\
    | /->--+-\  |
    | | |  | |  |
    \-+-/  \-+--^
      \------/   
    
    /---\        
    |   |  /----\
    | /-+>-+-\  |
    | | |  | |  ^
    \-+-/  \-+--/
      \------/   
    
    /---\        
    |   |  /----\
    | /-+->+-\  ^
    | | |  | |  |
    \-+-/  \-+--/
      \------/   
    
    /---\        
    |   |  /----<
    | /-+-->-\  |
    | | |  | |  |
    \-+-/  \-+--/
      \------/   
    
    /---\        
    |   |  /---<\
    | /-+--+>\  |
    | | |  | |  |
    \-+-/  \-+--/
      \------/   
    
    /---\        
    |   |  /--<-\
    | /-+--+-v  |
    | | |  | |  |
    \-+-/  \-+--/
      \------/   
    
    /---\        
    |   |  /-<--\
    | /-+--+-\  |
    | | |  | v  |
    \-+-/  \-+--/
      \------/   
    
    /---\        
    |   |  /<---\
    | /-+--+-\  |
    | | |  | |  |
    \-+-/  \-<--/
      \------/   
    
    /---\        
    |   |  v----\
    | /-+--+-\  |
    | | |  | |  |
    \-+-/  \<+--/
      \------/   
    
    /---\        
    |   |  /----\
    | /-+--v-\  |
    | | |  | |  |
    \-+-/  ^-+--/
      \------/   
    
    /---\        
    |   |  /----\
    | /-+--+-\  |
    | | |  X |  |
    \-+-/  \-+--/
      \------/   
    

After following their respective paths for a while, the carts eventually crash. To help prevent crashes, you'd like to know _the location of the first crash_. Locations are given in `X,Y` coordinates, where the furthest left column is `X=0` and the furthest top row is `Y=0`:

               111
     0123456789012
    0/---\        
    1|   |  /----\
    2| /-+--+-\  |
    3| | |  X |  |
    4\-+-/  \-+--/
    5  \------/   
    

In this example, the location of the first crash is _`7,3`_.

Your puzzle answer was `48,20`.

## Part 2

There isn't much you can do to prevent crashes in this ridiculous system. However, by predicting the crashes, the Elves know where to be in advance and _instantly remove the two crashing carts_ the moment any crash occurs.

They can proceed like this for a while, but eventually, they're going to run out of carts. It could be useful to figure out where the last cart that _hasn't_ crashed will end up.

For example:

    />-<\  
    |   |  
    | /<+-\
    | | | v
    \>+</ |
      |   ^
      \<->/
    
    /---\  
    |   |  
    | v-+-\
    | | | |
    \-+-/ |
      |   |
      ^---^
    
    /---\  
    |   |  
    | /-+-\
    | v | |
    \-+-/ |
      ^   ^
      \---/
    
    /---\  
    |   |  
    | /-+-\
    | | | |
    \-+-/ ^
      |   |
      \---/
    

After four very expensive crashes, a tick ends with only one cart remaining; its final location is _`6,4`_.

_What is the location of the last cart_ at the end of the first tick where it is the only cart left?

Your puzzle answer was `59,64`.


## Solution Notes

This puzzle is rather frustrating because bugs creep in far too easy and if they do, you don't have any idea what exactly went wrong -- you just get an incorrect result, and that's it. For example, I was stuck for a while because my crashed cart removal code was buggy: it sometimes removed the wrong carts, but that only happened on the real input, not in the examples :(

* Part 1, Python: 483 bytes, <100 ms
* Part 2, Python: 572 bytes, ~100 ms
