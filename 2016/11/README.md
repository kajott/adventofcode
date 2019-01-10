# 2016, Day 11: Radioisotope Thermoelectric Generators

You come upon a column of four floors that have been entirely sealed off from the rest of the building except for a small dedicated lobby. There are some radiation warnings and a big sign which reads "Radioisotope Testing Facility".

According to the project status board, this facility is currently being used to experiment with [Radioisotope Thermoelectric Generators](https://en.wikipedia.org/wiki/Radioisotope_thermoelectric_generator) (RTGs, or simply "generators") that are designed to be paired with specially-constructed microchips. Basically, an RTG is a highly radioactive rock that generates electricity through heat.

The experimental RTGs have poor radiation containment, so they're dangerously radioactive. The chips are prototypes and don't have normal radiation shielding, but they do have the ability to _generate an electromagnetic radiation shield when powered_. Unfortunately, they can _only_ be powered by their corresponding RTG. An RTG powering a microchip is still dangerous to other microchips.

In other words, if a chip is ever left in the same area as another RTG, and it's not connected to its own RTG, the chip will be _fried_. Therefore, it is assumed that you will follow procedure and keep chips connected to their corresponding RTG when they're in the same room, and away from other RTGs otherwise.

These microchips sound very interesting and useful to your current activities, and you'd like to try to retrieve them. The fourth floor of the facility has an assembling machine which can make a self-contained, shielded computer for you to take with you - that is, if you can bring it all of the RTGs and microchips.

Within the radiation-shielded part of the facility (in which it's safe to have these pre-assembly RTGs), there is an elevator that can move between the four floors. Its capacity rating means it can carry at most yourself and two RTGs or microchips in any combination. (They're rigged to some heavy diagnostic equipment - the assembling machine will detach it for you.) As a security measure, the elevator will only function if it contains at least one RTG or microchip. The elevator always stops on each floor to recharge, and this takes long enough that the items within it and the items on that floor can irradiate each other. (You can prevent this if a Microchip and its Generator end up on the same floor in this way, as they can be connected while the elevator is recharging.)

## Part 1

You make some notes of the locations of each component of interest (your puzzle input). Before you don a hazmat suit and start moving things around, you'd like to have an idea of what you need to do.

When you enter the containment area, you and the elevator will start on the first floor.

For example, suppose the isolated area has the following arrangement:

    The first floor contains a hydrogen-compatible microchip and a lithium-compatible microchip.
    The second floor contains a hydrogen generator.
    The third floor contains a lithium generator.
    The fourth floor contains nothing relevant.
    

As a diagram (`F#` for a Floor number, `E` for Elevator, `H` for Hydrogen, `L` for Lithium, `M` for Microchip, and `G` for Generator), the initial state looks like this:

    F4 .  .  .  .  .  
    F3 .  .  .  LG .  
    F2 .  HG .  .  .  
    F1 E  .  HM .  LM 
    

Then, to get everything up to the assembling machine on the fourth floor, the following steps could be taken:

*   Bring the Hydrogen-compatible Microchip to the second floor, which is safe because it can get power from the Hydrogen Generator:
    
        F4 .  .  .  .  .  
        F3 .  .  .  LG .  
        F2 E  HG HM .  .  
        F1 .  .  .  .  LM 
        
    
*   Bring both Hydrogen-related items to the third floor, which is safe because the Hydrogen-compatible microchip is getting power from its generator:
    
        F4 .  .  .  .  .  
        F3 E  HG HM LG .  
        F2 .  .  .  .  .  
        F1 .  .  .  .  LM 
        
    
*   Leave the Hydrogen Generator on floor three, but bring the Hydrogen-compatible Microchip back down with you so you can still use the elevator:
    
        F4 .  .  .  .  .  
        F3 .  HG .  LG .  
        F2 E  .  HM .  .  
        F1 .  .  .  .  LM 
        
    
*   At the first floor, grab the Lithium-compatible Microchip, which is safe because Microchips don't affect each other:
    
        F4 .  .  .  .  .  
        F3 .  HG .  LG .  
        F2 .  .  .  .  .  
        F1 E  .  HM .  LM 
        
    
*   Bring both Microchips up one floor, where there is nothing to fry them:
    
        F4 .  .  .  .  .  
        F3 .  HG .  LG .  
        F2 E  .  HM .  LM 
        F1 .  .  .  .  .  
        
    
*   Bring both Microchips up again to floor three, where they can be temporarily connected to their corresponding generators while the elevator recharges, preventing either of them from being fried:
    
        F4 .  .  .  .  .  
        F3 E  HG HM LG LM 
        F2 .  .  .  .  .  
        F1 .  .  .  .  .  
        
    
*   Bring both Microchips to the fourth floor:
    
        F4 E  .  HM .  LM 
        F3 .  HG .  LG .  
        F2 .  .  .  .  .  
        F1 .  .  .  .  .  
        
    
*   Leave the Lithium-compatible microchip on the fourth floor, but bring the Hydrogen-compatible one so you can still use the elevator; this is safe because although the Lithium Generator is on the destination floor, you can connect Hydrogen-compatible microchip to the Hydrogen Generator there:
    
        F4 .  .  .  .  LM 
        F3 E  HG HM LG .  
        F2 .  .  .  .  .  
        F1 .  .  .  .  .  
        
    
*   Bring both Generators up to the fourth floor, which is safe because you can connect the Lithium-compatible Microchip to the Lithium Generator upon arrival:
    
        F4 E  HG .  LG LM 
        F3 .  .  HM .  .  
        F2 .  .  .  .  .  
        F1 .  .  .  .  .  
        
    
*   Bring the Lithium Microchip with you to the third floor so you can use the elevator:
    
        F4 .  HG .  LG .  
        F3 E  .  HM .  LM 
        F2 .  .  .  .  .  
        F1 .  .  .  .  .  
        
    
*   Bring both Microchips to the fourth floor:
    
        F4 E  HG HM LG LM 
        F3 .  .  .  .  .  
        F2 .  .  .  .  .  
        F1 .  .  .  .  .  
        
    

In this arrangement, it takes `11` steps to collect all of the objects at the fourth floor for assembly. (Each elevator stop counts as one step, even if nothing is added to or removed from it.)

In your situation, what is the _minimum number of steps_ required to bring all of the objects to the fourth floor?

Your puzzle answer was `31`.

## Part 2

You step into the cleanroom separating the lobby from the isolated area and put on the hazmat suit.

Upon entering the isolated containment area, however, you notice some extra parts on the first floor that weren't listed on the record outside:

*   An elerium generator.
*   An elerium-compatible microchip.
*   A dilithium generator.
*   A dilithium-compatible microchip.

These work just like the other generators and microchips. You'll have to get them up to assembly as well.

What is the _minimum number of steps_ required to bring all of the objects, including these four new ones, to the fourth floor?

Your puzzle answer was `55`.


## Solution Notes

It's pretty obvious that the task of the puzzle is to implement a breadth-first search on the tree of possible moves; the complicated part is how to make it fast enough to be bearable. The bare minimum is recognition of already visited states to avoid cycles. With that, the Python solution runs in a barely acceptable timeframe for part 1, but part 2 with its 256-fold increase in problem size becomes unfeasible. So I turned to C, shoved the whole state into 32-bit words, used a full bitmap for tracking visited states, and arrived at a barely acceptable runtime for part 2.

But there's more. Reading the discussions at Reddit, I noticed that I missed another very important optimization: The order of the elements doesn't matter. In the example, the names of hydrogen and lithium could be swapped at any point without changing the outcome. As a result, if a state has been visited, the states with all permutations of element names also count as visited. In my solution, I implemented this by bringing every new state into a canonical order by sorting the generator-chip pairs by floor numbers. With that, the Python code for part 2 comfortably outperforms the C code (which doesn't use canonicalization).

* Part 1, Python (without canonicalization): 640 bytes, ~15 s
* Part 1, C (non-golf, without canonicalization): ~300 ms
* Part 2, C (non-golf, without canonicalization): ~25 s
* Part 2, Python (with canonicalization): 701 bytes, ~6 s
