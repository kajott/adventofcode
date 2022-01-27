# 2021, Day 25: Sea Cucumber

This is it: the bottom of the ocean trench, the last place the sleigh keys could be. Your submarine's experimental antenna _still isn't boosted enough_ to detect the keys, but they _must_ be here. All you need to do is _reach the seafloor_ and find them.

At least, you'd touch down on the seafloor if you could; unfortunately, it's completely covered by two large herds of [sea cucumbers](https://en.wikipedia.org/wiki/Sea_cucumber), and there isn't an open space large enough for your submarine.

You suspect that the Elves must have done this before, because just then you discover the phone number of a deep-sea marine biologist on a handwritten note taped to the wall of the submarine's cockpit.

"Sea cucumbers? Yeah, they're probably hunting for food. But don't worry, they're predictable critters: they move in perfectly straight lines, only moving forward when there's space to do so. They're actually quite polite!"

You explain that you'd like to predict when you could land your submarine.

"Oh that's easy, they'll eventually pile up and leave enough space for-- wait, did you say submarine? And the only place with that many sea cucumbers would be at the very bottom of the Mariana--" You hang up the phone.

## Part 1

There are two herds of sea cucumbers sharing the same region; one always moves _east_ (`>`), while the other always moves _south_ (`v`). Each location can contain at most one sea cucumber; the remaining locations are _empty_ (`.`). The submarine helpfully generates a map of the situation (your puzzle input). For example:

    v...>>.vv>
    .vv>>.vv..
    >>.>v>...v
    >>v>>.>.v.
    v>v.vv.v..
    >.>>..v...
    .vv..>.>v.
    v.v..>>v.v
    ....v..v.>
    

Every _step_, the sea cucumbers in the east-facing herd attempt to move forward one location, then the sea cucumbers in the south-facing herd attempt to move forward one location. When a herd moves forward, every sea cucumber in the herd first simultaneously considers whether there is a sea cucumber in the adjacent location it's facing (even another sea cucumber facing the same direction), and then every sea cucumber facing an empty location simultaneously moves into that location.

So, in a situation like this:

    ...>>>>>...

After one step, only the rightmost sea cucumber would have moved:

    ...>>>>.>..

After the next step, two sea cucumbers move:

    ...>>>.>.>.

During a single step, the east-facing herd moves first, then the south-facing herd moves. So, given this situation:

    ..........
    .>v....v..
    .......>..
    ..........
    

After a single step, of the sea cucumbers on the left, only the south-facing sea cucumber has moved (as it wasn't out of the way in time for the east-facing cucumber on the left to move), but both sea cucumbers on the right have moved (as the east-facing sea cucumber moved out of the way of the south-facing sea cucumber):

    ..........
    .>........
    ..v....v>.
    ..........
    

Due to _strong water currents_ in the area, sea cucumbers that move off the right edge of the map appear on the left edge, and sea cucumbers that move off the bottom edge of the map appear on the top edge. Sea cucumbers always check whether their destination location is empty before moving, even if that destination is on the opposite side of the map:

    Initial state:
    ...>...
    .......
    ......>
    v.....>
    ......>
    .......
    ..vvv..
    
    After 1 step:
    ..vv>..
    .......
    >......
    v.....>
    >......
    .......
    ....v..
    
    After 2 steps:
    ....v>.
    ..vv...
    .>.....
    ......>
    v>.....
    .......
    .......
    
    After 3 steps:
    ......>
    ..v.v..
    ..>v...
    >......
    ..>....
    v......
    .......
    
    After 4 steps:
    >......
    ..v....
    ..>.v..
    .>.v...
    ...>...
    .......
    v......
    

To find a safe place to land your submarine, the sea cucumbers need to stop moving. Again consider the first example:

    Initial state:
    v...>>.vv>
    .vv>>.vv..
    >>.>v>...v
    >>v>>.>.v.
    v>v.vv.v..
    >.>>..v...
    .vv..>.>v.
    v.v..>>v.v
    ....v..v.>
    
    After 1 step:
    ....>.>v.>
    v.v>.>v.v.
    >v>>..>v..
    >>v>v>.>.v
    .>v.v...v.
    v>>.>vvv..
    ..v...>>..
    vv...>>vv.
    >.v.v..v.v
    
    After 2 steps:
    >.v.v>>..v
    v.v.>>vv..
    >v>.>.>.v.
    >>v>v.>v>.
    .>..v....v
    .>v>>.v.v.
    v....v>v>.
    .vv..>>v..
    v>.....vv.
    
    After 3 steps:
    v>v.v>.>v.
    v...>>.v.v
    >vv>.>v>..
    >>v>v.>.v>
    ..>....v..
    .>.>v>v..v
    ..v..v>vv>
    v.v..>>v..
    .v>....v..
    
    After 4 steps:
    v>..v.>>..
    v.v.>.>.v.
    >vv.>>.v>v
    >>.>..v>.>
    ..v>v...v.
    ..>>.>vv..
    >.v.vv>v.v
    .....>>vv.
    vvv>...v..
    
    After 5 steps:
    vv>...>v>.
    v.v.v>.>v.
    >.v.>.>.>v
    >v>.>..v>>
    ..v>v.v...
    ..>.>>vvv.
    .>...v>v..
    ..v.v>>v.v
    v.v.>...v.
    
    ...
    
    After 10 steps:
    ..>..>>vv.
    v.....>>.v
    ..v.v>>>v>
    v>.>v.>>>.
    ..v>v.vv.v
    .v.>>>.v..
    v.v..>v>..
    ..v...>v.>
    .vv..v>vv.
    
    ...
    
    After 20 steps:
    v>.....>>.
    >vv>.....v
    .>v>v.vv>>
    v>>>v.>v.>
    ....vv>v..
    .v.>>>vvv.
    ..v..>>vv.
    v.v...>>.v
    ..v.....v>
    
    ...
    
    After 30 steps:
    .vv.v..>>>
    v>...v...>
    >.v>.>vv.>
    >v>.>.>v.>
    .>..v.vv..
    ..v>..>>v.
    ....v>..>v
    v.v...>vv>
    v.v...>vvv
    
    ...
    
    After 40 steps:
    >>v>v..v..
    ..>>v..vv.
    ..>>>v.>.v
    ..>>>>vvv>
    v.....>...
    v.v...>v>>
    >vv.....v>
    .>v...v.>v
    vvv.v..v.>
    
    ...
    
    After 50 steps:
    ..>>v>vv.v
    ..v.>>vv..
    v.>>v>>v..
    ..>>>>>vv.
    vvv....>vv
    ..v....>>>
    v>.......>
    .vv>....v>
    .>v.vv.v..
    
    ...
    
    After 55 steps:
    ..>>v>vv..
    ..v.>>vv..
    ..>>v>>vv.
    ..>>>>>vv.
    v......>vv
    v>v....>>v
    vvv...>..>
    >vv.....>.
    .>v.vv.v..
    
    After 56 steps:
    ..>>v>vv..
    ..v.>>vv..
    ..>>v>>vv.
    ..>>>>>vv.
    v......>vv
    v>v....>>v
    vvv....>.>
    >vv......>
    .>v.vv.v..
    
    After 57 steps:
    ..>>v>vv..
    ..v.>>vv..
    ..>>v>>vv.
    ..>>>>>vv.
    v......>vv
    v>v....>>v
    vvv.....>>
    >vv......>
    .>v.vv.v..
    
    After 58 steps:
    ..>>v>vv..
    ..v.>>vv..
    ..>>v>>vv.
    ..>>>>>vv.
    v......>vv
    v>v....>>v
    vvv.....>>
    >vv......>
    .>v.vv.v..
    

In this example, the sea cucumbers stop moving after _`58`_ steps.

Find somewhere safe to land your submarine. _What is the first step on which no sea cucumbers move?_

Your puzzle answer was `308`.

## Part 2

Suddenly, the experimental antenna control console lights up:

    Sleigh keys detected!

According to the console, the keys are _directly under the submarine_. You landed right on them! Using a robotic arm on the submarine, you move the sleigh keys into the airlock.

Now, you just need to get them to Santa in time to save Christmas! You check your clock - it _is_ Christmas. There's no way you can get them back to the surface in time.

Just as you start to lose hope, you notice a button on the sleigh keys: _remote start_. You can start the sleigh from the bottom of the ocean! You just need some way to _boost the signal_ from the keys so it actually reaches the sleigh. Good thing the submarine has that experimental antenna! You'll definitely need _50 stars_ to boost it that far, though.

The experimental antenna control console lights up again:

    Energy source detected.
    Integrating energy source from device "sleigh keys"...done.
    Installing device drivers...done.
    Recalibrating experimental antenna...done.
    Boost strength due to matching signal phase: 1 star

Only _49 stars_ to go.


## Solution Notes

This puzzle is technically a cellular automaton, or rather two of them, because each step is carried out in two phases with slightly different rules.

My first idea was to use sets to represent the object positions, which makes for a nice, albeit repetitive, implementation. That, however, turned out to be far too slow for the actual input, going far beyond the 1 minute mark.

So "conventional" 2D arrays it was, then. The specific rules for repetitions are quite delicate: avoiding double substitutions (i.e. moving an object that has already been moved in the same round) isn't as easy as it seems. I don't think for a second that my array-based solution is optimal in anyway, but it gets the job done.

That, however, made me think: What's a good way to apply these motion rules without having to worry about double substitutions? `str.replace` is! The vertical direction can easily be implemented by transposing, applying the rules horizontally, and transposing back. This approach worked perfectly, and is the smallest, fastest and most elegant I came up with.

* Part 1, Python (sets): 337 bytes, ~20 min
* Part 1, Python (2D array): 361 bytes, ~3 s
* Part 1, Python (strings): 181 bytes, ~350 ms
