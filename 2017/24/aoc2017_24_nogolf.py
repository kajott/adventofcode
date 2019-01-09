import collections

INPUT="""
0/2
2/2
2/3
3/4
3/5
0/1
10/1
9/10
""".strip('\n').split('\n')
INPUT = open("input.txt")

bridges = [map(int, line.strip().split('/')) for line in INPUT]
strengths = map(sum, bridges)

index = collections.defaultdict(set)
for i, b in enumerate(bridges):
    index[b[0]].add(i)
    index[b[1]].add(i)

def other(bridge_id, pins):
    res = bridges[bridge_id][:]
    res.remove(pins)
    return res[0]
    
lengths = collections.defaultdict(set)

def max_strength(strength, pins, visited, path=[]):
    maxsubstrength = strength
    lengths[len(path)].add(strength)
    can_visit = index[pins] - visited
#    print strength, path
    for b in sorted(can_visit, key=lambda b: -strengths[b]):
        maxsubstrength = max(maxsubstrength, max_strength(strength + strengths[b], other(b, pins), visited | {b}, path + [bridges[b]]))
    return maxsubstrength

print max_strength(0, 0, set())
print max(max(lengths.items())[1])
