import re, sys

PART = 1

INPUT = """
The first floor contains a hydrogen-compatible microchip and a lithium-compatible microchip.
The second floor contains a hydrogen generator.
The third floor contains a lithium generator.
The fourth floor contains nothing relevant.
""".strip('\n').split('\n')
INPUT = open("input.txt")

MAXDEPTH = 0

elements = {}
def get_element_id(name):
    elements[name] = e = elements.get(name, len(elements) * 2)
    return e
objlist = []
for floor, line in enumerate(INPUT):
    objlist += [(get_element_id(elem) + (objtype < '-'), 3-floor)
                for elem, objtype in re.findall(r'(\w+)(-| g)', line)]
assert [o for o,f in sorted(objlist)] == range(len(objlist))
state = tuple([f for o,f in sorted(objlist)] + [3] * (1 if PART == 1 else 5))
objcount = len(state) - 1

print objcount, "objects"

current = {state}
moves = set()
depth = 0
visited = set()
while current or moves:
    if not current:
        current = moves
        moves = set()
        depth += 1
        print "depth %d: %d moves" % (depth, len(current))
        if MAXDEPTH and (depth > MAXDEPTH):
            break
    state = current.pop()
    pos = state[-1]

    for obj1 in [i for i in range(objcount) if state[i] == pos]:
        for obj2 in [i for i in range(obj1, objcount) if state[i] == pos]:
            for newpos in range(pos-1 if pos else pos+1, min(4, pos+3), 2):
                newstate = list(state)
                newstate[obj1] = newstate[obj2] = newstate[-1] = newpos
                newstate = tuple(newstate)

                if not sum(newstate):
                    print depth + 1
                    sys.exit(0)
                
                if newstate in visited:
                    continue
                
                gens  = {i for i,f in enumerate(newstate[1:-1:2]) if f == newpos}
                chips = {i for i,f in enumerate(newstate[0:-1:2]) if f == newpos}
                if gens and (chips - gens):
                    continue

                moves.add(newstate)
                visited.add(newstate)

print "no solution found :("
