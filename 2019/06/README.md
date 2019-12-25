# Day 6: Universal Orbit Map

You've landed at the Universal Orbit Map facility on Mercury. Because navigation in space often involves transferring between orbits, the orbit maps here are useful for finding efficient routes between, for example, you and Santa. You download a map of the local orbits (your puzzle input).

## Part 1

Except for the universal Center of Mass (`COM`), every object in space is in orbit around exactly one other object. An [orbit](https://en.wikipedia.org/wiki/Orbit) looks roughly like this:

                      \
                       \
                        |
                        |
    AAA--> o            o <--BBB
                        |
                        |
                       /
                      /
    

In this diagram, the object `BBB` is in orbit around `AAA`. The path that `BBB` takes around `AAA` (drawn with lines) is only partly shown. In the map data, this orbital relationship is written `AAA)BBB`, which means "`BBB` is in orbit around `AAA`".

Before you use your map data to plot a course, you need to make sure it wasn't corrupted during the download. To verify maps, the Universal Orbit Map facility uses _orbit count checksums_ - the total number of _direct orbits_ (like the one shown above) and _indirect orbits_.

Whenever `A` orbits `B` and `B` orbits `C`, then `A` _indirectly orbits_ `C`. This chain can be any number of objects long: if `A` orbits `B`, `B` orbits `C`, and `C` orbits `D`, then `A` indirectly orbits `D`.

For example, suppose you have the following map:

    COM)B
    B)C
    C)D
    D)E
    E)F
    B)G
    G)H
    D)I
    E)J
    J)K
    K)L
    

Visually, the above map of orbits looks like this:

            G - H       J - K - L
           /           /
    COM - B - C - D - E - F
                   \
                    I
    

In this visual representation, when two objects are connected by a line, the one on the right directly orbits the one on the left.

Here, we can count the total number of orbits as follows:

*   `D` directly orbits `C` and indirectly orbits `B` and `COM`, a total of `3` orbits.
*   `L` directly orbits `K` and indirectly orbits `J`, `E`, `D`, `C`, `B`, and `COM`, a total of `7` orbits.
*   `COM` orbits nothing.

The total number of direct and indirect orbits in this example is `_42_`.

_What is the total number of direct and indirect orbits_ in your map data?

Your puzzle answer was `402879`.

## Part 2

Now, you just need to figure out how many _orbital transfers_ you (`YOU`) need to take to get to Santa (`SAN`).

You start at the object `YOU` are orbiting; your destination is the object `SAN` is orbiting. An orbital transfer lets you move from any object to an object orbiting or orbited by that object.

For example, suppose you have the following map:

    COM)B
    B)C
    C)D
    D)E
    E)F
    B)G
    G)H
    D)I
    E)J
    J)K
    K)L
    K)YOU
    I)SAN
    

Visually, the above map of orbits looks like this:

                              YOU
                             /
            G - H       J - K - L
           /           /
    COM - B - C - D - E - F
                   \
                    I - SAN
    

In this example, `YOU` are in orbit around `K`, and `SAN` is in orbit around `I`. To move from `K` to `I`, a minimum of `4` orbital transfers are required:

*   `K` to `J`
*   `J` to `E`
*   `E` to `D`
*   `D` to `I`

Afterward, the map of orbits looks like this:

            G - H       J - K - L
           /           /
    COM - B - C - D - E - F
                   \
                    I - SAN
                     \
                      YOU
    

_What is the minimum number of orbital transfers required_ to move from the object `YOU` are orbiting to the object `SAN` is orbiting? (Between the objects they are orbiting - _not_ between `YOU` and `SAN`.)

Your puzzle answer was `484`.


## Solution Notes

Some classic operations on a directed acyclic graph (DAG), a.k.a. a tree. The important trick for the second part is to find the "common ancestor" of the `YOU` and `SAN` nodes and then just add the subgraph depths together.

* Part 1, Python: 113 bytes, <100 ms
* Part 2, Python: 165 bytes, <100 ms
