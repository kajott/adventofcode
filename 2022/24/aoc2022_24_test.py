#!/usr/bin/env python3
"""scratchpad for my AoC 2022/24 solution"""

W=set()
B=set()
for y, line in enumerate(open("input.txt")):
    for x, c in enumerate(line):
        if c=='#': W.add((x-1,y-1))
        if c=='>': B.add((x-1,y-1,+1,0))
        if c=='<': B.add((x-1,y-1,-1,0))
        if c=='^': B.add((x-1,y-1,0,-1))
        if c=='v': B.add((x-1,y-1,0,+1))
X = max(x for x,y in W)
Y = max(y for x,y in W)
print(f"maze size: {X}x{Y}, {len(W)} walls, {len(B)} blizzards")
# add some walls on the top and bottom, otherwise the player escapes the maze
W |= { (x,-2) for x in range(-1,3) }
W |= { (x,Y+1) for x in range(X-3,X+2) }
start = (0, -1)
exit = (X-1, Y)

t = 0
q = {start}
goals = [exit, start, exit]
while goals:
    t += 1
    b = {((px+t*dx)%X, (py+t*dy)%Y) for px,py,dx,dy in B}
    n = {(px+dx, py+dy) for dx,dy in ((1,0),(0,1),(-1,0),(0,-1),(0,0)) for px,py in q}
    q = n - b - W
    #print(t, len(q), goals[0])
    if goals[0] in q:
        print(f"goal {goals[0]} reached after {t} steps (queue size: {len(q)})")
        q = {goals.pop(0)}
