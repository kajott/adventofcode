# 2019, Day 18: Many-Worlds Interpretation

As you approach Neptune, a planetary security system detects you and activates a giant [tractor beam](https://en.wikipedia.org/wiki/Tractor_beam) on [Triton](https://en.wikipedia.org/wiki/Triton_(moon))! You have no choice but to land.

A scan of the local area reveals only one interesting feature: a massive underground vault. You generate a map of the tunnels (your puzzle input). The tunnels are too narrow to move diagonally.

## Part 1

Only one _entrance_ (marked `@`) is present among the _open passages_ (marked `.`) and _stone walls_ (`#`), but you also detect an assortment of _keys_ (shown as lowercase letters) and _doors_ (shown as uppercase letters). Keys of a given letter open the door of the same letter: `a` opens `A`, `b` opens `B`, and so on. You aren't sure which key you need to disable the tractor beam, so you'll need to _collect all of them_.

For example, suppose you have the following map:

    #########
    #b.A.@.a#
    #########
    

Starting from the entrance (`@`), you can only access a large door (`A`) and a key (`a`). Moving toward the door doesn't help you, but you can move `2` steps to collect the key, unlocking `A` in the process:

    #########
    #b.....@#
    #########
    

Then, you can move `6` steps to collect the only other key, `b`:

    #########
    #@......#
    #########
    

So, collecting every key took a total of _`8`_ steps.

Here is a larger example:

    ########################
    #f.D.E.e.C.b.A.@.a.B.c.#
    ######################.#
    #d.....................#
    ########################
    

The only reasonable move is to take key `a` and unlock door `A`:

    ########################
    #f.D.E.e.C.b.....@.B.c.#
    ######################.#
    #d.....................#
    ########################
    

Then, do the same with key `b`:

    ########################
    #f.D.E.e.C.@.........c.#
    ######################.#
    #d.....................#
    ########################
    

...and the same with key `c`:

    ########################
    #f.D.E.e.............@.#
    ######################.#
    #d.....................#
    ########################
    

Now, you have a choice between keys `d` and `e`. While key `e` is closer, collecting it now would be slower in the long run than collecting key `d` first, so that's the best choice:

    ########################
    #f...E.e...............#
    ######################.#
    #@.....................#
    ########################
    

Finally, collect key `e` to unlock door `E`, then collect key `f`, taking a grand total of _`86`_ steps.

Here are a few more examples:

*       ########################
        #...............b.C.D.f#
        #.######################
        #.....@.a.B.c.d.A.e.F.g#
        ########################
        
    
    Shortest path is `132` steps: `b`, `a`, `c`, `d`, `f`, `e`, `g`
    
*       #################
        #i.G..c...e..H.p#
        ########.########
        #j.A..b...f..D.o#
        ########@########
        #k.E..a...g..B.n#
        ########.########
        #l.F..d...h..C.m#
        #################
        
    
    Shortest paths are `136` steps;  
    one is: `a`, `f`, `b`, `j`, `g`, `n`, `h`, `d`, `l`, `o`, `e`, `p`, `c`, `i`, `k`, `m`
    
*       ########################
        #@..............ac.GI.b#
        ###d#e#f################
        ###A#B#C################
        ###g#h#i################
        ########################
        
    
    Shortest paths are `81` steps; one is: `a`, `c`, `f`, `i`, `d`, `g`, `b`, `e`, `h`
    

_How many steps is the shortest path that collects all of the keys?_

Your puzzle answer was `3764`.

## Part 2

You arrive at the vault only to discover that there is not one vault, but _four_ - each with its own entrance.

On your map, find the area in the middle that looks like this:

    ...
    .@.
    ...
    

Update your map to instead use the correct data:

    @#@
    ###
    @#@
    

This change will split your map into four separate sections, each with its own entrance:

    #######       #######
    #a.#Cd#       #a.#Cd#
    ##...##       ##@#@##
    ##.@.##  -->  #######
    ##...##       ##@#@##
    #cB#Ab#       #cB#Ab#
    #######       #######
    

Because some of the keys are for doors in other vaults, it would take much too long to collect all of the keys by yourself. Instead, you deploy four remote-controlled robots. Each starts at one of the entrances (`@`).

Your goal is still to _collect all of the keys in the fewest steps_, but now, each robot has its own position and can move independently. You can only remotely control a single robot at a time. Collecting a key instantly unlocks any corresponding doors, regardless of the vault in which the key or door is found.

For example, in the map above, the top-left robot first collects key `a`, unlocking door `A` in the bottom-right vault:

    #######
    #@.#Cd#
    ##.#@##
    #######
    ##@#@##
    #cB#.b#
    #######
    

Then, the bottom-right robot collects key `b`, unlocking door `B` in the bottom-left vault:

    #######
    #@.#Cd#
    ##.#@##
    #######
    ##@#.##
    #c.#.@#
    #######
    

Then, the bottom-left robot collects key `c`:

    #######
    #@.#.d#
    ##.#@##
    #######
    ##.#.##
    #@.#.@#
    #######
    

Finally, the top-right robot collects key `d`:

    #######
    #@.#.@#
    ##.#.##
    #######
    ##.#.##
    #@.#.@#
    #######
    

In this example, it only took _`8`_ steps to collect all of the keys.

Sometimes, multiple robots might have keys available, or a robot might have to wait for multiple keys to be collected:

    ###############
    #d.ABC.#.....a#
    ######@#@######
    ###############
    ######@#@######
    #b.....#.....c#
    ###############
    

First, the top-right, bottom-left, and bottom-right robots take turns collecting keys `a`, `b`, and `c`, a total of `6 + 6 + 6 = 18` steps. Then, the top-left robot can access key `d`, spending another `6` steps; collecting all of the keys here takes a minimum of _`24`_ steps.

Here's a more complex example:

    #############
    #DcBa.#.GhKl#
    #.###@#@#I###
    #e#d#####j#k#
    ###C#@#@###J#
    #fEbA.#.FgHi#
    #############
    

*   Top-left robot collects key `a`.
*   Bottom-left robot collects key `b`.
*   Top-left robot collects key `c`.
*   Bottom-left robot collects key `d`.
*   Top-left robot collects key `e`.
*   Bottom-left robot collects key `f`.
*   Bottom-right robot collects key `g`.
*   Top-right robot collects key `h`.
*   Bottom-right robot collects key `i`.
*   Top-right robot collects key `j`.
*   Bottom-right robot collects key `k`.
*   Top-right robot collects key `l`.

In the above example, the fewest steps to collect all of the keys is _`32`_.

Here's an example with more choices:

    #############
    #g#f.D#..h#l#
    #F###e#E###.#
    #dCba@#@BcIJ#
    #############
    #nK.L@#@G...#
    #M###N#H###.#
    #o#m..#i#jk.#
    #############
    

One solution with the fewest steps is:

*   Top-left robot collects key `e`.
*   Top-right robot collects key `h`.
*   Bottom-right robot collects key `i`.
*   Top-left robot collects key `a`.
*   Top-left robot collects key `b`.
*   Top-right robot collects key `c`.
*   Top-left robot collects key `d`.
*   Top-left robot collects key `f`.
*   Top-left robot collects key `g`.
*   Bottom-right robot collects key `k`.
*   Bottom-right robot collects key `j`.
*   Top-right robot collects key `l`.
*   Bottom-left robot collects key `n`.
*   Bottom-left robot collects key `m`.
*   Bottom-left robot collects key `o`.

This example requires at least _`72`_ steps to collect all keys.

After updating your map and using the remote-controlled robots, _what is the fewest steps necessary to collect all of the keys?_

Your puzzle answer was `1738`.


## Solution Notes

I used a multi-step approach to solve these: First, build a full distance matrix between keys, plus metadata which other keys and doors are encountered along the path(s). Then, use that information to find the shortest way that gets all keys.

The first step is what took longest to get right. A straight BFS is not sufficient because of the doors: I don't just need the key-to-key distances, but also which keys are on the path between any two keys. If there's another door somewhere else in the maze that's not on the path between the two keys, I'm not interested in it, even if it might be located right next to the starting key. This is typically the domain of a DFS, but that's to slow on the (rather large) maze. In the end, I used a BFS variant that stores the "come-from" direction of every explored free field and use that to backtrack from every destination key, collecting doors and extra keys along the way.

The second step is classical DFS, but with a naive implementation, the runtime for more than approx. 10 keys is far too long. Caching already explored states helped to get the runtime down comfortably into the sub-second zone.

Based on that framework, part 2 of the puzzle isn't much of a problem. Step 1 doesn't change at all, and step 2 simply needs to track four current locations instead of just one.

* Part 1, Python: 666 bytes, ~300 ms
* Part 2, Python: 842 bytes, ~700 ms
