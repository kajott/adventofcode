import re

wires = {}
cache = {}

for line in open("input.txt"):
    a, o, b, d = re.match(r'([a-z0-9]+ )?([A-Z]+ )?([a-z0-9]+) -> ([a-z]+)', line).groups()
    wires[d] = (o and o.strip(), a and a.strip(), b)

def get(name):
    if name.isdigit():
        return int(name)
    try:
        return cache[name]
    except KeyError:
        pass
    o, a, b = wires[name]
    if not o:           v =            get(b)
    elif o == "AND":    v =  get(a) &  get(b)
    elif o == "OR":     v =  get(a) |  get(b)
    elif o == "RSHIFT": v =  get(a) >> get(b)
    elif o == "LSHIFT": v = (get(a) << get(b)) & 0xFFFF
    elif o == "NOT":    v =            get(b)  ^ 0xFFFF
    else: print o, "?!"
    cache[name] = v
    return v

part1 = get("a")
print part1
cache = { "b": part1 }
print get("a")
