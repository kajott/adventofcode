#!/usr/bin/env python3

TOP, RIGHT, BOTTOM, LEFT = range(4)

MonsterPattern = """
                  # 
#    ##    ##    ###
 #  #  #  #  #  #   
"""
Monster = set()
for y, row in zip((-1,0,1), MonsterPattern.strip("\r\n").split("\n")):
    Monster |= { 1j*y + x for x,c in enumerate(row) if c == '#' }
#print(sorted(Monster, key=lambda p:(p.real,-p.imag)));stop


def multidump(tileid, *tiles):
    print(f"Tile {tileid}:")
    ecs = list(map(make_edgecodes, tiles))
    width = len(tiles[0][0])
    nwidth = len(str(1<<width))
    for rows in zip(*tiles):
        print(' | '.join(''.join(".#"[c] for c in row) for row in rows))
    print(' | '.join(str(e[0]).rjust(nwidth).center(width) for e in ecs))
    print(' | '.join(str(e[3]).rjust(nwidth) + " "*(width - nwidth*2) + str(e[1]).rjust(nwidth) for e in ecs))
    print(' | '.join(str(e[2]).rjust(nwidth).center(width) for e in ecs))
    s = set()
    for e in ecs: s |= set(e)
    print(s)
    print()

def transpose(tile):
    return [[row[x] for row in tile] for x in range(len(tile[0]))]
def hflip(tile):
    return [row[::-1] for row in tile]
def vflip(tile):
    return [row[:] for row in tile[::-1]]

def edge2code(edge):
    return sum(1<<b for b,x in enumerate(edge) if x)

def make_edgecodes(tile):
    return tuple(map(edge2code, [
        tile[0],                    # TOP
        [row[-1] for row in tile],  # RIGHT
        tile[-1],                   # BOTTOM
        [row[0] for row in tile],   # LEFT
    ]))


def edgecode_set(edgecodes):
    ec_set = set()
    for ec in edgecodes:
        ec_set |= set(ec)
    return sorted(ec_set)


def find_tile(edgecodes, assigned, ref_tile_and_variant, ref_edge, search_edge, success_func):
    ref_tile, ref_variant = ref_tile_and_variant
    search_code = edgecodes[ref_tile][ref_variant][ref_edge]
    assigned.add(ref_tile)
    for t, ecs in edgecodes.items():
        if t in assigned:
            continue
        for v, sub_ecs in enumerate(ecs):
            if sub_ecs[search_edge] == search_code:
                success_func((t,v))
                assigned.add(t)
                return True


def make_puzzle(edgecodes, start_tile, start_variant):
    puzzle = [[(start_tile, start_variant)]]
    assigned = set()
    while find_tile(edgecodes, assigned, puzzle[-1][-1], RIGHT, LEFT, lambda x: puzzle[-1].append(x)):
        pass
    while find_tile(edgecodes, assigned, puzzle[-1][0], BOTTOM, TOP, lambda x: puzzle.append([x])):
        while find_tile(edgecodes, assigned, puzzle[-1][-1], RIGHT, LEFT, lambda x: puzzle[-1].append(x)):
            t0,v0 = puzzle[-2][len(puzzle[-1])-1]
            t1,v1 = puzzle[-1][-1]
            assert edgecodes[t0][v0][BOTTOM] == edgecodes[t1][v1][TOP]
    if set(edgecodes) > assigned:
        return
    return puzzle


def dump_seamap(seamap, marked=set()):
    xx = sorted(int(p.real) for p in seamap)
    yy = sorted(int(p.imag) for p in seamap)
    monster_map = set()
    for y in range(yy[0], yy[-1]+1):
        print(''.join(".#?O"[(x+1j*y in seamap) + 2*(x+1j*y in marked)] for x in range(xx[0], xx[-1]+1)))


def get_monster(p0):
    return { p+p0 for p in Monster }


def search_monsters(seamap):
    res = set()
    for p in seamap:
        m = get_monster(p)
        if m <= seamap:
            res |= m
    return res


if __name__ == "__main__":
    tiles = {}
    edgecodes = {}
    ec_ref = {}

    for tiledata in open("input2.txt").read().strip().split("\n\n"):
        tiledata = tiledata.split('\n')
        tileid = int(tiledata[0][5:-1])
        t_base = [[int(c<'.') for c in r] for r in tiledata[1:]]
        t_trans = [[r[x] for r in t_base] for x in range(len(t_base[0]))]
        variants = [
                        t_base,
            vflip(      t_base ),
                  hflip(t_base),
            vflip(hflip(t_base)),
                        t_trans,
            vflip(      t_trans ),
                  hflip(t_trans),
            vflip(hflip(t_trans)),
        ]
        tiles[tileid] = variants
        ecs = tuple(map(make_edgecodes, variants))
        edgecodes[tileid] = ecs

        for ec in edgecode_set(ecs):
            ec_ref[ec] = ec_ref.get(ec, set()) | {tileid}
        
        tile_height = len(t_base)
        tile_width = len(t_trans)
        assert tile_width == tile_height
    print(len(tiles), "tiles total")
    print(len(ec_ref), "edge codes total")
    print("tile size:", tile_width, "x", tile_height)

    # find edge codes only referenced once
    single_ec_refs = {}
    for tileids in ec_ref.values():
        if len(tileids) == 1:
            t = list(tileids)[0]
            single_ec_refs[t] = single_ec_refs.get(t,0) + 1
    assert min(single_ec_refs.values()) == 2
    assert max(single_ec_refs.values()) == 4
    edge_tiles = {t for t,f in single_ec_refs.items() if f==4}
    border_tiles = {t for t,f in single_ec_refs.items() if f==2}
    inner_tiles = set(tiles) - edge_tiles - border_tiles
    print("edge tiles:", sorted(edge_tiles))
    print("border tiles:", sorted(border_tiles))
    print("inner tiles:", sorted(inner_tiles))

    # compute part 1's solution
    edge_mul = 1
    for t in edge_tiles: edge_mul *= t
    print("part 1 solution:", edge_mul)

    # assemble the puzzle
    print("assembling puzzle ...")
    for v in range(8):
        puzzle = make_puzzle(edgecodes, min(edge_tiles), v)
        if puzzle: break
    for row in puzzle:
        print("    " + "  ".join(f"{t}.{v}" for t,v in row))

    # create a set of marked locations
    seamap = set()
    for y0, p_row in enumerate(puzzle):
        for x0, (t,v) in enumerate(p_row):
            p0 = x0 * (tile_width-2) +1j * y0 * (tile_height-2)
            for y, row in enumerate(tiles[t][v][1:-1]):
                seamap |= { p0 +1j*y + x for x, c in enumerate(row[1:-1]) if c }

    # create alternate seamaps
    seamaps = [seamap, {p.conjugate() for p in seamap}]
    for x in range(6):
        seamaps.append({p*1j for p in seamaps[-2]})

    for i in range(8):
        seamap = seamaps[i]
        monsters = search_monsters(seamap)
        if not monsters:
            continue
        print()
        print("===== seamap orientation", i, "=====")
        dump_seamap(seamap, monsters)
        print("monsters:", len(monsters) / len(Monster))
        print("part 2 solution:", len(seamap - monsters))
