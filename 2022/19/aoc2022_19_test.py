#!/usr/bin/env python2
"""scratchpad for my AoC 2022/19 solution"""
import re,sys

RTypes = ["ore", "clay", "obsidian", "geode"]
BPs = []
for line in open("input.txt"):
    BP = 4 * [None]
    for rt, c1, r1, dummy, c2, r2 in re.findall(r'each (\w+) robot costs (\d+) (\w+)( and (\d+) (\w+))?', line, flags=re.I):
        rt = RTypes.index(rt)
        cost = [0,0,0,0]
        cost[RTypes.index(r1)] = int(c1)
        if dummy:
            cost[RTypes.index(r2)] = int(c2)
        BP[rt] = tuple(cost)
    BPs.append(tuple(BP))

def DFS_main(cache, BP, *state):
    global gbest, nstates
    time, robots, materials = state
    if time < 1:
        nstates = max(nstates, len(cache))
        return materials[-1]
    if state in cache: return cache[state]
    best = materials[-1] + robots[-1] * time
    if (best + (time*time + time + 1) / 2) <= gbest:
        cache[state] = 0
        return
    #print (T-time)*".", time, robots, materials,'->',best,'|',len(cache),hits
    rt_to_check = (3,2,1,0)
    #rt_to_check = [int(raw_input("next RT: "))]
    for rt in rt_to_check:
        if robots[rt] >= max_robots[rt]:
            continue  # don't mine more resources than we can possibly spend on robots
        time_req = [((((need - have) + rate - 1) / rate) if rate else ((need - have) * 9999)) for need, have, rate in zip(BP[rt], materials, robots)]
        time_req = max(0, max(time_req)) + 1
        if time_req >= time: continue
        best = max(best, DFS_main(cache, BP, time - time_req,
            tuple(robots[i] + (i == rt) for i in (0,1,2,3)),
            tuple(have + time_req * rate - need for have, rate, need in zip(materials, robots, BP[rt]))))
    cache[state] = best
    if best > gbest:
        gbest = best
        #print "new best:",gbest, len(cache)
    return best
def DFS(BP, total_time):
    return DFS_main({}, BP, total_time, (1,0,0,0), (0,0,0,0))

def BFS(BP, total_time):
    best = 0
    queue = {(total_time, 1, 0, 0, 0, 0, 0, 0, 0)}
    visited = set()
    round = 0
    mr_prune_count = pc_prune_count = 0
    while queue:
        round += 1
        #print "BFS round", round
        next = set()
        visited |= queue
        for state in queue:
            time = state[0]
            robots = state[1:5]
            materials = state[5:]
            res = materials[-1] + robots[-1] * time
            if res > best:
                best = res
                #print "new best:", best, round, len(visited), "mr", mr_prune_count, "pc", pc_prune_count
            if (res + (time*time + time + 1) / 2) <= best:
                pc_prune_count += 1
                continue  # we can't produce more geode than our current best from here (even if we'd produce one geode robot per cycle), no need to try
            for rt in (3,2,1,0):
                if robots[rt] >= max_robots[rt]:
                    mr_prune_count += 1
                    continue  # don't mine more resources than we can possibly spend on robots
                time_req = [((((need - have) + rate - 1) / rate) if rate else ((need - have) * 9999)) for need, have, rate in zip(BP[rt], materials, robots)]
                time_req = max(0, max(time_req)) + 1
                if not(time_req < time): continue
                next.add(tuple([time - time_req] +
                               [robots[i] + (i == rt) for i in (0,1,2,3)] +
                               [have + time_req * rate - need for have, rate, need in zip(materials, robots, BP[rt])]))
        queue = next - visited
    global gbest, nstates
    nstates = len(visited)
    gbest = best
    return best

def solve(solver, bp_idx, t):
    global T, max_robots, gbest, nstates
    gbest = nstates = 0
    T = t
    bp = BPs[bp_idx - 1]
    max_robots = [max(r[rt] for r in bp) for rt in range(3)] + [99]
    #print "trying BP", bp_idx, "..."
    res = solver(bp, t)
    print "BP", bp_idx, "T", t, "result", res, "|", nstates, "states"
    return res

bpfilter = map(int, sys.argv[1:])
bp_range = [i for i in range(1, len(BPs)+1) if not(bpfilter) or (i in bpfilter)]

solver = BFS

if 0:  # test
    print solve(solver, 1, 24)

if 1:  # part 1
    print sum(i * solve(solver, i, 24) for i in bp_range)

if 1:  # part 2
    m = 1
    for i in bp_range[:3]:
        m *= solve(solver, i, 32)
    print m
