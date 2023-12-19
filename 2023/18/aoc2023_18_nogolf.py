#!/usr/bin/env python3

InputFile = "input.txt"
Part = 2

if __name__ == "__main__":
    # step 1: decode polygon, mark X/Y coordinates
    px, py = 0, 0
    usedX, usedY = {0}, {0}
    polygon = [(0,0)]
    for line in open(InputFile):
        line = line.split()
        if Part == 1:
            dircode, length, dummy = line
            length = int(length)
        elif Part == 2:
            line = ''.join(c for c in line[-1] if c.isdigit() or c.isalpha())
            length = int(line[:-1], 16)
            dircode = "RDLU"[int(line[-1])]
        if   dircode == 'R': px += length
        elif dircode == 'D': py += length
        elif dircode == 'L': px -= length
        elif dircode == 'U': py -= length
        else: assert None
        polygon.append((px, py))
        usedX.add(px)
        usedY.add(py)
    print(len(polygon), "points")
    assert polygon[-1] == (0,0)

    # step 2: map coordinates
    def cmap(used, coord):
        used = sorted(used)
        print(len(used), "distinct", coord, "coordinates")
        last = used[0]
        mapC = {last: 0}
        sizeC = [1]
        pos = 0
        for c in used[1:]:
            pos += 2
            sizeC += [c - last - 1, 1]
            mapC[c] = pos
            last = c
        #print(coord, "map:", mapC)
        #print(coord, "sizes:", sizeC)
        return mapC, sizeC, len(sizeC)
    mapX, sizeX, maxX = cmap(usedX, 'X')
    mapY, sizeY, maxY = cmap(usedY, 'Y')
    print("effective grid size:", maxX, "x", maxY)

    # step 3: draw polygon with reduced coordinates
    cells, left, right = set(), set(), set()
    for (x0, y0), (x1, y1) in zip(polygon, polygon[1:]):
        x0 = mapX[x0]
        y0 = mapY[y0]
        x1 = mapX[x1]
        y1 = mapY[y1]
        length = abs(x0 - x1) + abs(y0 - y1) + 1
        dx = (x1 > x0) - (x1 < x0)
        dy = (y1 > y0) - (y1 < y0)
        for _ in range(length):
            cells.add((x0, y0))
            left.add((x0-dy, y0+dx))
            right.add((x0+dy, y0-dx))
            x0 += dx
            y0 += dy

    # grow left/right traces
    for edge in (right, left):
        edge = edge - cells
        trace = set()
        while edge and not((-1,-1) in edge):
            trace |= edge
            edge = {(x+dx, y+dy) for x,y in edge for dx,dy in ((0,1),(0,-1),(1,0),(-1,0))} - cells - trace
        if not edge: break

    # evaluate final area
    cells |= trace
    print(sum(sizeX[x] * sizeY[y] for x,y in cells))


    # BONUS: direct computation via shoelace formula and Pick's law
    area = 0
    circumference = 0
    for (x0, y0), (x1, y1) in zip(polygon, polygon[1:]):
        area += x0*y1 - y0*x1
        circumference += abs(x0-x1) + abs(y0-y1)
    print((abs(area) + circumference) // 2 + 1)
