#!/usr/bin/env python3
import heapq

Part2 = False

if not Part2:
    Maze = """
#############
#89.a.b.c.de#
###0#1#2#3###
  #4#5#6#7#
  #########
    """.strip()
    HallwayStart = 8
if Part2:
    Maze = """
#############
#gh.i.j.k.lm#
###0#1#2#3###
  #4#5#6#7#
  #8#9#a#b#
  #c#d#e#f#
  #########
    """.strip()
    HallwayStart = 16
PositionNames = "0123456789abcde" + ("fghijklm" if Part2 else "")
HallwaySet = set(range(HallwayStart, len(PositionNames)))
HallwayStr = "......."
Goal = "ABCD" * (4 if Part2 else 2) + HallwayStr
CostMul = {'A':1, 'B':10, 'C':100, 'D':1000}

def dump(state):
    print(''.join((state[int(c,24)] if c in PositionNames else c) for c in Maze))
    print()

def cmp(a, b):  # Python2 cmp() emulation
    if a < b: return -1
    if a > b: return +1
    return 0

def generate_distance_matrix():
    global DistMatrix
    m = Maze.split('\n')
    pos = [(m[y].index(c),y) for c,y in ((c,min(y for y,l in enumerate(m) if c in l)) for c in PositionNames)]
    DistMatrix = []
    for x1,y1 in pos:
        DistMatrix.append([])
        for x2,y2 in pos:
            x, y = x1, y1
            path = [0]
            while (x != x2) or (y != y2):
                if x == x2: y += cmp(y2, y)  # move vertically into destination room
                elif y < 2: x += cmp(x2, x)  # move only horizontally in the hallway
                else:       y -= 1           # leave source hallway first
                if m[y][x] in PositionNames:
                    path.append(int(m[y][x], 24))
                path[0] += 1
            DistMatrix[-1].append(path)

def format_distance_matrix_entry(path):
    return ''.join(PositionNames[i] for i in path[1:]) + f"({path[0]})"

def dump_distance_matrix():
    print(Maze)
    for src, row in zip(PositionNames, DistMatrix):
        print(src + ":", ''.join(format_distance_matrix_entry(path).ljust(10) for path in row))


def generate_moves(state):
    for src, src_obj in enumerate(state):
        if src_obj == ".": continue   # not a valid source
        new_state = list(state)
        new_state[src] = '.'  # assume the object has already moved

        # compute valid destinations
        atype = int(src_obj, 24) - 10
        if Part2:
            valid_dest = {atype, atype + 4, atype + 8, atype + 12}
        else:
            valid_dest = {atype, atype + 4} # target room
        if src < HallwayStart:              # if not already in the hallway ...
            valid_dest |= HallwaySet        # ... allow moving there
        valid_dest -= {src}                 # standing still is not a move

        # check valid destinations: is the path free?
        for dest in valid_dest:
            path = DistMatrix[src][dest]
            if all(new_state[pos] == '.' for pos in path[1:]):
                new_state[dest] = src_obj
                yield ''.join(new_state), CostMul[src_obj] * path[0]
                new_state[dest] = '.'


if __name__ == "__main__":
    generate_distance_matrix()
    dump_distance_matrix()

    with open("input.txt") as f:
        initial = ''.join(c for c in f.read() if c in "ABCD") + HallwayStr
    if Part2:
        initial = initial[:4] + "DCBADBAC" + initial[4:]
    print(initial)
    dump(initial)

    # Dijkstra algorithm
    open_states = [(0, initial)]
    cost_cache = {initial: 0}
    i = 0
    while open_states:
        i += 1
        if not(i & 1023):
            print(f"{i} iterations, {len(open_states)} open states, {open_states[0][0]} best score")
        cost, state = heapq.heappop(open_states)
        if state == Goal: break
        if cost > cost_cache.get(state, 1e10):
            continue  # we found a better path here in the meantime
        for new_state, add_cost in generate_moves(state):
            new_cost = cost + add_cost
            if new_cost < cost_cache.get(new_state, 1e10):
                cost_cache[new_state] = new_cost
                heapq.heappush(open_states, (new_cost, new_state))
    print(cost)
