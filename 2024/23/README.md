# 2024, Day 23: LAN Party

As The Historians wander around a secure area at Easter Bunny HQ, you come across posters for a [LAN party](https://en.wikipedia.org/wiki/LAN_party) scheduled for today! Maybe you can find it; you connect to a nearby [datalink port](../../2016/09) and download a map of the local network (your puzzle input).

## Part 1

The network map provides a list of every _connection between two computers_. For example:

    kh-tc
    qp-kh
    de-cg
    ka-co
    yn-aq
    qp-ub
    cg-tb
    vc-aq
    tb-ka
    wh-tc
    yn-cg
    kh-ub
    ta-co
    de-co
    tc-td
    tb-wq
    wh-td
    ta-ka
    td-qp
    aq-cg
    wq-ub
    ub-vc
    de-ta
    wq-aq
    wq-vc
    wh-yn
    ka-de
    kh-ta
    co-tc
    wh-qp
    tb-vc
    td-yn

Each line of text in the network map represents a single connection; the line `kh-tc` represents a connection between the computer named `kh` and the computer named `tc`. Connections aren't directional; `tc-kh` would mean exactly the same thing.

LAN parties typically involve multiplayer games, so maybe you can locate it by finding groups of connected computers. Start by looking for _sets of three computers_ where each computer in the set is connected to the other two computers.

In this example, there are `12` such sets of three inter-connected computers:

    aq,cg,yn
    aq,vc,wq
    co,de,ka
    co,de,ta
    co,ka,ta
    de,ka,ta
    kh,qp,ub
    qp,td,wh
    tb,vc,wq
    tc,td,wh
    td,wh,yn
    ub,vc,wq

If the Chief Historian is here, _and_ he's at the LAN party, it would be best to know that right away. You're pretty sure his computer's name starts with `t`, so consider only sets of three computers where at least one computer's name starts with `t`. That narrows the list down to _`7`_ sets of three inter-connected computers:

    co,de,ta
    co,ka,ta
    de,ka,ta
    qp,td,wh
    tb,vc,wq
    tc,td,wh
    td,wh,yn

Find all the sets of three inter-connected computers. _How many contain at least one computer with a name that starts with `t`?_

Your puzzle answer was `1437`.

## Part 2

There are still way too many results to go through them all. You'll have to find the LAN party another way and go there yourself.

Since it doesn't seem like any employees are around, you figure they must all be at the LAN party. If that's true, the LAN party will be the _largest set of computers that are all connected to each other_. That is, for each computer at the LAN party, that computer will have a connection to every other computer at the LAN party.

In the above example, the largest set of computers that are all connected to each other is made up of `co`, `de`, `ka`, and `ta`. Each computer in this set has a connection to every other computer in the set:

    ka-co
    ta-co
    de-co
    ta-ka
    de-ta
    ka-de

The LAN party posters say that the _password_ to get into the LAN party is the name of every computer at the LAN party, sorted alphabetically, then joined together with commas. (The people running the LAN party are clearly a bunch of nerds.) In this example, the password would be _`co,de,ka,ta`_.

_What is the password to get into the LAN party?_

Your puzzle answer was `da,do,gx,ly,mb,ns,nt,pz,sc,si,tp,ul,vl`.

## Solution Notes

A nice graph problem. I fell intro a trap early in part 1 in that I counted also indirectly connected nodes (i.e. if there's `A-B` and `B-C`, I assumed `A-C` too), resulting in much more triples than there actually were.

Part 2 is technically the [maximum clique problem](https://en.wikipedia.org/wiki/Clique_problem), which is NP-complete and hence sounds very scary. But in fact, it isn't at all, at least not for the inputs we've been given: For each node, consider this node part of a clique, and then add that node's adjacent nodes to the clique iff they are also adjacent to all existing nodes in the clique. This gives the answer in no time and with even less code than part 1.

* Part 1, Python: 257 bytes, <100 ms
* Part 2, Python: 241 bytes, <100 ms
