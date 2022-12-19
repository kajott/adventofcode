# 2022, Day 19: Not Enough Minerals

Your scans show that the lava did indeed form obsidian!

The wind has changed direction enough to stop sending lava droplets toward you, so you and the elephants exit the cave. As you do, you notice a collection of [geodes](https://en.wikipedia.org/wiki/Geode) around the pond. Perhaps you could use the obsidian to create some _geode-cracking robots_ and break them open?

To collect the obsidian from the bottom of the pond, you'll need waterproof _obsidian-collecting robots_. Fortunately, there is an abundant amount of clay nearby that you can use to make them waterproof.

In order to harvest the clay, you'll need special-purpose _clay-collecting robots_. To make any type of robot, you'll need _ore_, which is also plentiful but in the opposite direction from the clay.

## Part 1

Collecting ore requires _ore-collecting robots_ with big drills. Fortunately, _you have exactly one ore-collecting robot_ in your pack that you can use to kickstart the whole operation.

Each robot can collect 1 of its resource type per minute. It also takes one minute for the robot factory (also conveniently from your pack) to construct any type of robot, although it consumes the necessary resources available when construction begins.

The robot factory has many _blueprints_ (your puzzle input) you can choose from, but once you've configured it with a blueprint, you can't change it. You'll need to work out which blueprint is best.

For example:

    Blueprint 1:
      Each ore robot costs 4 ore.
      Each clay robot costs 2 ore.
      Each obsidian robot costs 3 ore and 14 clay.
      Each geode robot costs 2 ore and 7 obsidian.
    
    Blueprint 2:
      Each ore robot costs 2 ore.
      Each clay robot costs 3 ore.
      Each obsidian robot costs 3 ore and 8 clay.
      Each geode robot costs 3 ore and 12 obsidian.
    

(Blueprints have been line-wrapped here for legibility. The robot factory's actual assortment of blueprints are provided one blueprint per line.)

The elephants are starting to look hungry, so you shouldn't take too long; you need to figure out which blueprint would maximize the number of opened geodes after _24 minutes_ by figuring out which robots to build and when to build them.

Using blueprint 1 in the example above, the largest number of geodes you could open in 24 minutes is _`9`_. One way to achieve that is:

    == Minute 1 ==
    1 ore-collecting robot collects 1 ore; you now have 1 ore.
    
    == Minute 2 ==
    1 ore-collecting robot collects 1 ore; you now have 2 ore.
    
    == Minute 3 ==
    Spend 2 ore to start building a clay-collecting robot.
    1 ore-collecting robot collects 1 ore; you now have 1 ore.
    The new clay-collecting robot is ready; you now have 1 of them.
    
    == Minute 4 ==
    1 ore-collecting robot collects 1 ore; you now have 2 ore.
    1 clay-collecting robot collects 1 clay; you now have 1 clay.
    
    == Minute 5 ==
    Spend 2 ore to start building a clay-collecting robot.
    1 ore-collecting robot collects 1 ore; you now have 1 ore.
    1 clay-collecting robot collects 1 clay; you now have 2 clay.
    The new clay-collecting robot is ready; you now have 2 of them.
    
    == Minute 6 ==
    1 ore-collecting robot collects 1 ore; you now have 2 ore.
    2 clay-collecting robots collect 2 clay; you now have 4 clay.
    
    == Minute 7 ==
    Spend 2 ore to start building a clay-collecting robot.
    1 ore-collecting robot collects 1 ore; you now have 1 ore.
    2 clay-collecting robots collect 2 clay; you now have 6 clay.
    The new clay-collecting robot is ready; you now have 3 of them.
    
    == Minute 8 ==
    1 ore-collecting robot collects 1 ore; you now have 2 ore.
    3 clay-collecting robots collect 3 clay; you now have 9 clay.
    
    == Minute 9 ==
    1 ore-collecting robot collects 1 ore; you now have 3 ore.
    3 clay-collecting robots collect 3 clay; you now have 12 clay.
    
    == Minute 10 ==
    1 ore-collecting robot collects 1 ore; you now have 4 ore.
    3 clay-collecting robots collect 3 clay; you now have 15 clay.
    
    == Minute 11 ==
    Spend 3 ore and 14 clay to start building an obsidian-collecting robot.
    1 ore-collecting robot collects 1 ore; you now have 2 ore.
    3 clay-collecting robots collect 3 clay; you now have 4 clay.
    The new obsidian-collecting robot is ready; you now have 1 of them.
    
    == Minute 12 ==
    Spend 2 ore to start building a clay-collecting robot.
    1 ore-collecting robot collects 1 ore; you now have 1 ore.
    3 clay-collecting robots collect 3 clay; you now have 7 clay.
    1 obsidian-collecting robot collects 1 obsidian; you now have 1 obsidian.
    The new clay-collecting robot is ready; you now have 4 of them.
    
    == Minute 13 ==
    1 ore-collecting robot collects 1 ore; you now have 2 ore.
    4 clay-collecting robots collect 4 clay; you now have 11 clay.
    1 obsidian-collecting robot collects 1 obsidian; you now have 2 obsidian.
    
    == Minute 14 ==
    1 ore-collecting robot collects 1 ore; you now have 3 ore.
    4 clay-collecting robots collect 4 clay; you now have 15 clay.
    1 obsidian-collecting robot collects 1 obsidian; you now have 3 obsidian.
    
    == Minute 15 ==
    Spend 3 ore and 14 clay to start building an obsidian-collecting robot.
    1 ore-collecting robot collects 1 ore; you now have 1 ore.
    4 clay-collecting robots collect 4 clay; you now have 5 clay.
    1 obsidian-collecting robot collects 1 obsidian; you now have 4 obsidian.
    The new obsidian-collecting robot is ready; you now have 2 of them.
    
    == Minute 16 ==
    1 ore-collecting robot collects 1 ore; you now have 2 ore.
    4 clay-collecting robots collect 4 clay; you now have 9 clay.
    2 obsidian-collecting robots collect 2 obsidian; you now have 6 obsidian.
    
    == Minute 17 ==
    1 ore-collecting robot collects 1 ore; you now have 3 ore.
    4 clay-collecting robots collect 4 clay; you now have 13 clay.
    2 obsidian-collecting robots collect 2 obsidian; you now have 8 obsidian.
    
    == Minute 18 ==
    Spend 2 ore and 7 obsidian to start building a geode-cracking robot.
    1 ore-collecting robot collects 1 ore; you now have 2 ore.
    4 clay-collecting robots collect 4 clay; you now have 17 clay.
    2 obsidian-collecting robots collect 2 obsidian; you now have 3 obsidian.
    The new geode-cracking robot is ready; you now have 1 of them.
    
    == Minute 19 ==
    1 ore-collecting robot collects 1 ore; you now have 3 ore.
    4 clay-collecting robots collect 4 clay; you now have 21 clay.
    2 obsidian-collecting robots collect 2 obsidian; you now have 5 obsidian.
    1 geode-cracking robot cracks 1 geode; you now have 1 open geode.
    
    == Minute 20 ==
    1 ore-collecting robot collects 1 ore; you now have 4 ore.
    4 clay-collecting robots collect 4 clay; you now have 25 clay.
    2 obsidian-collecting robots collect 2 obsidian; you now have 7 obsidian.
    1 geode-cracking robot cracks 1 geode; you now have 2 open geodes.
    
    == Minute 21 ==
    Spend 2 ore and 7 obsidian to start building a geode-cracking robot.
    1 ore-collecting robot collects 1 ore; you now have 3 ore.
    4 clay-collecting robots collect 4 clay; you now have 29 clay.
    2 obsidian-collecting robots collect 2 obsidian; you now have 2 obsidian.
    1 geode-cracking robot cracks 1 geode; you now have 3 open geodes.
    The new geode-cracking robot is ready; you now have 2 of them.
    
    == Minute 22 ==
    1 ore-collecting robot collects 1 ore; you now have 4 ore.
    4 clay-collecting robots collect 4 clay; you now have 33 clay.
    2 obsidian-collecting robots collect 2 obsidian; you now have 4 obsidian.
    2 geode-cracking robots crack 2 geodes; you now have 5 open geodes.
    
    == Minute 23 ==
    1 ore-collecting robot collects 1 ore; you now have 5 ore.
    4 clay-collecting robots collect 4 clay; you now have 37 clay.
    2 obsidian-collecting robots collect 2 obsidian; you now have 6 obsidian.
    2 geode-cracking robots crack 2 geodes; you now have 7 open geodes.
    
    == Minute 24 ==
    1 ore-collecting robot collects 1 ore; you now have 6 ore.
    4 clay-collecting robots collect 4 clay; you now have 41 clay.
    2 obsidian-collecting robots collect 2 obsidian; you now have 8 obsidian.
    2 geode-cracking robots crack 2 geodes; you now have 9 open geodes.
    

However, by using blueprint 2 in the example above, you could do even better: the largest number of geodes you could open in 24 minutes is _`12`_.

Determine the _quality level_ of each blueprint by _multiplying that blueprint's ID number_ with the largest number of geodes that can be opened in 24 minutes using that blueprint. In this example, the first blueprint has ID 1 and can open 9 geodes, so its quality level is _`9`_. The second blueprint has ID 2 and can open 12 geodes, so its quality level is _`24`_. Finally, if you _add up the quality levels_ of all of the blueprints in the list, you get _`33`_.

Determine the quality level of each blueprint using the largest number of geodes it could produce in 24 minutes. _What do you get if you add up the quality level of all of the blueprints in your list?_

Your puzzle answer was `1599`.

## Part 2

While you were choosing the best blueprint, the elephants found some food on their own, so you're not in as much of a hurry; you figure you probably have _32 minutes_ before the wind changes direction again and you'll need to get out of range of the erupting volcano.

Unfortunately, one of the elephants _ate most of your blueprint list_! Now, only the first three blueprints in your list are intact.

In 32 minutes, the largest number of geodes blueprint 1 (from the example above) can open is _`56`_. One way to achieve that is:

    == Minute 1 ==
    1 ore-collecting robot collects 1 ore; you now have 1 ore.
    
    == Minute 2 ==
    1 ore-collecting robot collects 1 ore; you now have 2 ore.
    
    == Minute 3 ==
    1 ore-collecting robot collects 1 ore; you now have 3 ore.
    
    == Minute 4 ==
    1 ore-collecting robot collects 1 ore; you now have 4 ore.
    
    == Minute 5 ==
    Spend 4 ore to start building an ore-collecting robot.
    1 ore-collecting robot collects 1 ore; you now have 1 ore.
    The new ore-collecting robot is ready; you now have 2 of them.
    
    == Minute 6 ==
    2 ore-collecting robots collect 2 ore; you now have 3 ore.
    
    == Minute 7 ==
    Spend 2 ore to start building a clay-collecting robot.
    2 ore-collecting robots collect 2 ore; you now have 3 ore.
    The new clay-collecting robot is ready; you now have 1 of them.
    
    == Minute 8 ==
    Spend 2 ore to start building a clay-collecting robot.
    2 ore-collecting robots collect 2 ore; you now have 3 ore.
    1 clay-collecting robot collects 1 clay; you now have 1 clay.
    The new clay-collecting robot is ready; you now have 2 of them.
    
    == Minute 9 ==
    Spend 2 ore to start building a clay-collecting robot.
    2 ore-collecting robots collect 2 ore; you now have 3 ore.
    2 clay-collecting robots collect 2 clay; you now have 3 clay.
    The new clay-collecting robot is ready; you now have 3 of them.
    
    == Minute 10 ==
    Spend 2 ore to start building a clay-collecting robot.
    2 ore-collecting robots collect 2 ore; you now have 3 ore.
    3 clay-collecting robots collect 3 clay; you now have 6 clay.
    The new clay-collecting robot is ready; you now have 4 of them.
    
    == Minute 11 ==
    Spend 2 ore to start building a clay-collecting robot.
    2 ore-collecting robots collect 2 ore; you now have 3 ore.
    4 clay-collecting robots collect 4 clay; you now have 10 clay.
    The new clay-collecting robot is ready; you now have 5 of them.
    
    == Minute 12 ==
    Spend 2 ore to start building a clay-collecting robot.
    2 ore-collecting robots collect 2 ore; you now have 3 ore.
    5 clay-collecting robots collect 5 clay; you now have 15 clay.
    The new clay-collecting robot is ready; you now have 6 of them.
    
    == Minute 13 ==
    Spend 2 ore to start building a clay-collecting robot.
    2 ore-collecting robots collect 2 ore; you now have 3 ore.
    6 clay-collecting robots collect 6 clay; you now have 21 clay.
    The new clay-collecting robot is ready; you now have 7 of them.
    
    == Minute 14 ==
    Spend 3 ore and 14 clay to start building an obsidian-collecting robot.
    2 ore-collecting robots collect 2 ore; you now have 2 ore.
    7 clay-collecting robots collect 7 clay; you now have 14 clay.
    The new obsidian-collecting robot is ready; you now have 1 of them.
    
    == Minute 15 ==
    2 ore-collecting robots collect 2 ore; you now have 4 ore.
    7 clay-collecting robots collect 7 clay; you now have 21 clay.
    1 obsidian-collecting robot collects 1 obsidian; you now have 1 obsidian.
    
    == Minute 16 ==
    Spend 3 ore and 14 clay to start building an obsidian-collecting robot.
    2 ore-collecting robots collect 2 ore; you now have 3 ore.
    7 clay-collecting robots collect 7 clay; you now have 14 clay.
    1 obsidian-collecting robot collects 1 obsidian; you now have 2 obsidian.
    The new obsidian-collecting robot is ready; you now have 2 of them.
    
    == Minute 17 ==
    Spend 3 ore and 14 clay to start building an obsidian-collecting robot.
    2 ore-collecting robots collect 2 ore; you now have 2 ore.
    7 clay-collecting robots collect 7 clay; you now have 7 clay.
    2 obsidian-collecting robots collect 2 obsidian; you now have 4 obsidian.
    The new obsidian-collecting robot is ready; you now have 3 of them.
    
    == Minute 18 ==
    2 ore-collecting robots collect 2 ore; you now have 4 ore.
    7 clay-collecting robots collect 7 clay; you now have 14 clay.
    3 obsidian-collecting robots collect 3 obsidian; you now have 7 obsidian.
    
    == Minute 19 ==
    Spend 3 ore and 14 clay to start building an obsidian-collecting robot.
    2 ore-collecting robots collect 2 ore; you now have 3 ore.
    7 clay-collecting robots collect 7 clay; you now have 7 clay.
    3 obsidian-collecting robots collect 3 obsidian; you now have 10 obsidian.
    The new obsidian-collecting robot is ready; you now have 4 of them.
    
    == Minute 20 ==
    Spend 2 ore and 7 obsidian to start building a geode-cracking robot.
    2 ore-collecting robots collect 2 ore; you now have 3 ore.
    7 clay-collecting robots collect 7 clay; you now have 14 clay.
    4 obsidian-collecting robots collect 4 obsidian; you now have 7 obsidian.
    The new geode-cracking robot is ready; you now have 1 of them.
    
    == Minute 21 ==
    Spend 3 ore and 14 clay to start building an obsidian-collecting robot.
    2 ore-collecting robots collect 2 ore; you now have 2 ore.
    7 clay-collecting robots collect 7 clay; you now have 7 clay.
    4 obsidian-collecting robots collect 4 obsidian; you now have 11 obsidian.
    1 geode-cracking robot cracks 1 geode; you now have 1 open geode.
    The new obsidian-collecting robot is ready; you now have 5 of them.
    
    == Minute 22 ==
    Spend 2 ore and 7 obsidian to start building a geode-cracking robot.
    2 ore-collecting robots collect 2 ore; you now have 2 ore.
    7 clay-collecting robots collect 7 clay; you now have 14 clay.
    5 obsidian-collecting robots collect 5 obsidian; you now have 9 obsidian.
    1 geode-cracking robot cracks 1 geode; you now have 2 open geodes.
    The new geode-cracking robot is ready; you now have 2 of them.
    
    == Minute 23 ==
    Spend 2 ore and 7 obsidian to start building a geode-cracking robot.
    2 ore-collecting robots collect 2 ore; you now have 2 ore.
    7 clay-collecting robots collect 7 clay; you now have 21 clay.
    5 obsidian-collecting robots collect 5 obsidian; you now have 7 obsidian.
    2 geode-cracking robots crack 2 geodes; you now have 4 open geodes.
    The new geode-cracking robot is ready; you now have 3 of them.
    
    == Minute 24 ==
    Spend 2 ore and 7 obsidian to start building a geode-cracking robot.
    2 ore-collecting robots collect 2 ore; you now have 2 ore.
    7 clay-collecting robots collect 7 clay; you now have 28 clay.
    5 obsidian-collecting robots collect 5 obsidian; you now have 5 obsidian.
    3 geode-cracking robots crack 3 geodes; you now have 7 open geodes.
    The new geode-cracking robot is ready; you now have 4 of them.
    
    == Minute 25 ==
    2 ore-collecting robots collect 2 ore; you now have 4 ore.
    7 clay-collecting robots collect 7 clay; you now have 35 clay.
    5 obsidian-collecting robots collect 5 obsidian; you now have 10 obsidian.
    4 geode-cracking robots crack 4 geodes; you now have 11 open geodes.
    
    == Minute 26 ==
    Spend 2 ore and 7 obsidian to start building a geode-cracking robot.
    2 ore-collecting robots collect 2 ore; you now have 4 ore.
    7 clay-collecting robots collect 7 clay; you now have 42 clay.
    5 obsidian-collecting robots collect 5 obsidian; you now have 8 obsidian.
    4 geode-cracking robots crack 4 geodes; you now have 15 open geodes.
    The new geode-cracking robot is ready; you now have 5 of them.
    
    == Minute 27 ==
    Spend 2 ore and 7 obsidian to start building a geode-cracking robot.
    2 ore-collecting robots collect 2 ore; you now have 4 ore.
    7 clay-collecting robots collect 7 clay; you now have 49 clay.
    5 obsidian-collecting robots collect 5 obsidian; you now have 6 obsidian.
    5 geode-cracking robots crack 5 geodes; you now have 20 open geodes.
    The new geode-cracking robot is ready; you now have 6 of them.
    
    == Minute 28 ==
    2 ore-collecting robots collect 2 ore; you now have 6 ore.
    7 clay-collecting robots collect 7 clay; you now have 56 clay.
    5 obsidian-collecting robots collect 5 obsidian; you now have 11 obsidian.
    6 geode-cracking robots crack 6 geodes; you now have 26 open geodes.
    
    == Minute 29 ==
    Spend 2 ore and 7 obsidian to start building a geode-cracking robot.
    2 ore-collecting robots collect 2 ore; you now have 6 ore.
    7 clay-collecting robots collect 7 clay; you now have 63 clay.
    5 obsidian-collecting robots collect 5 obsidian; you now have 9 obsidian.
    6 geode-cracking robots crack 6 geodes; you now have 32 open geodes.
    The new geode-cracking robot is ready; you now have 7 of them.
    
    == Minute 30 ==
    Spend 2 ore and 7 obsidian to start building a geode-cracking robot.
    2 ore-collecting robots collect 2 ore; you now have 6 ore.
    7 clay-collecting robots collect 7 clay; you now have 70 clay.
    5 obsidian-collecting robots collect 5 obsidian; you now have 7 obsidian.
    7 geode-cracking robots crack 7 geodes; you now have 39 open geodes.
    The new geode-cracking robot is ready; you now have 8 of them.
    
    == Minute 31 ==
    Spend 2 ore and 7 obsidian to start building a geode-cracking robot.
    2 ore-collecting robots collect 2 ore; you now have 6 ore.
    7 clay-collecting robots collect 7 clay; you now have 77 clay.
    5 obsidian-collecting robots collect 5 obsidian; you now have 5 obsidian.
    8 geode-cracking robots crack 8 geodes; you now have 47 open geodes.
    The new geode-cracking robot is ready; you now have 9 of them.
    
    == Minute 32 ==
    2 ore-collecting robots collect 2 ore; you now have 8 ore.
    7 clay-collecting robots collect 7 clay; you now have 84 clay.
    5 obsidian-collecting robots collect 5 obsidian; you now have 10 obsidian.
    9 geode-cracking robots crack 9 geodes; you now have 56 open geodes.
    

However, blueprint 2 from the example above is still better; using it, the largest number of geodes you could open in 32 minutes is _`62`_.

You _no longer have enough blueprints to worry about quality levels_. Instead, for each of the first three blueprints, determine the largest number of geodes you could open; then, multiply these three values together.

Don't worry about quality levels; instead, just determine the largest number of geodes you could open using each of the first three blueprints. _What do you get if you multiply these numbers together?_

Your puzzle answer was `14112`.

## Solution Notes

This is another graph search puzzle with very peculiar rules. I initially tried to solve this with DFS and memoization, but it's too slow on its own. Eventually, I switched over to BFS, which is not inherently faster, but allows for a few nice optimizations. And this is essentially what this puzzle is all about: Finding shortcuts to prune the search tree. The ones I used in the end are these:
- It's not needed to have a node for every minute of the simulation. Instead, it's possible to choose which robot to build next and advance the time by as many minutes as it takes to gather all the required resources with the current production capabilities.
- The only thing that consumes resources is building more robots, but only one robot can be built per time unit. So it doesn't make sense to have more mining robots for a specific resource than what's needed to built the most resource-consuming other robot. The mined material would just be wasted.
- Even under ideal circumstances, only one additional geode robot can be built per time unit, so for each examined state, there's an upper bound of geodes that can possibly be mined at the end of the simulation. If that number isn't higher than the current global maximum, it doesn't make sense to explore this state further.

With these implemented, I get to a large, but (just barely) acceptably fast solution. Parts 1 and 2 only differ in how the evualuation is performed, hence the code is very similar.

During golfing, a few sacrifices had to be made; the non-golf version is around 1.5x to 2x faster as a result. Out of curiosity, I also tried my hand at a C++ version (albeit using DFS, for simplicity reasons), and that's "only" 5x faster than the non-golf BFS version and requires 80 instead of 300 MB of RAM.

* Part 1, Python: 510 bytes, ~7 s
* Part 2, Python: 511 bytes, ~30 s
* Parts 1+2, C++ (non-golf): ~3.5 s
