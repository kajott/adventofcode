#!/usr/bin/env python3

AllColors = "#d95f02 #1b9e77 #7570b3 #e6ab02 #66a61e #e7298a".split()
Scale = 8
LineWidth = 1

if __name__ == "__main__":
    grid = {x+y*1j:c for y,l in enumerate(open("input.txt")) for x,c in enumerate(l.strip())}
    width  = int(max(p.real for p in grid)) + 1
    height = int(max(p.imag for p in grid)) + 1
    colors = {}

    remain = set(grid)
    while remain:
        # find a region and get its extents
        seed = remain.pop()
        letter = grid[seed]
        region = {seed}
        prev = None
        while region != prev:
            prev = region
            region = {p+d for p in region for d in (0, 1, -1, 1j, -1j)
                      if grid.get(p+d) == letter}
        remain -= region

        # get colors of neighbor regions, and choose an unused one
        neighbor = {p+d for p in region for d in (1, -1, 1j, -1j, -1-1j, 1-1j, -1+1j, 1+1j)} - region
        neighbor_colors = {colors[p] for p in neighbor if p in colors}
        avail_colors = [c for c in AllColors if not(c in neighbor_colors)]
        assert avail_colors
        for p in region:
            colors[p] = avail_colors[0]

    with open("aoc2024_12_vis.svg", "w") as f:
        f.write('<?xml version="1.0" ?>\n')
        f.write(f'<svg xmlns="http://www.w3.org/2000/svg" width="{(width+2)*Scale}" height="{(height+2)*Scale}">\n')
        f.write(f'<style>line {{ stroke:black; stroke-width:{LineWidth}; stroke-linecap:square; }}</style>\n')
        for p,c in colors.items():
            x,y = map(int, (p.real, p.imag))
            f.write(f'<rect x="{(x+1)*Scale-LineWidth*.375-.5}" y="{(y+1)*Scale-LineWidth*.375-.5}" width="{Scale+LineWidth*.75}" height="{Scale+LineWidth*.75}" fill="{c}" />\n')
        for y in range(height + 1):
            for x in range(width + 1):
                p = x+y*1j
                letter = grid.get(p)
                px = (x + 1) * Scale - 0.5
                py = (y + 1) * Scale - 0.5
                if letter != grid.get(p - 1):
                    f.write(f'<line x1="{px}" y1="{py}" x2="{px}" y2="{py+Scale}" />\n')
                if letter != grid.get(p - 1j):
                    f.write(f'<line x1="{px}" y1="{py}" x2="{px+Scale}" y2="{py}" />\n')
        f.write('</svg>\n')
