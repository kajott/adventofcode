DEBUG = 1
# 0 = silent operation
# 1 = show movements on continuously updated map
# 2 = print map for each round
# 3 = detailed unit debugging
# 4 = detailed unit debugging with map after every turn
# 5 = detailed unit debugging with A* distance maps
# 6 = detailed unit debugging with A* distance maps and target list

STOP_AT_ROUND = 0  # 0 = don't stop


XXX = 999
DIST_VIS_MAP = "0123456789abcdefghijklmnopqrstuvwxyz" + 100 * '+'

class Unit(object):
    def __init__(self, x,y):
        self.x, self.y = x,y
        self.team = world[y][x]
        self.hp = 200

    def move(self, x,y):
        global world
        assert world[y][x] == '.'
        assert max(abs(self.x - x), abs(self.y - y)) == 1
        world[self.y][self.x] = '.'
        self.x, self.y = x,y
        world[self.y][self.x] = self.team

    def __cmp__(self, other):
        return cmp(self.y, other.y) or cmp(self.x, other.x)

    def __str__(self):
        return "%s(%d)@%d,%d" % (self.team, self.hp, self.x, self.y)
    def __repr__(self):
        return "<%s>" % str(self)


def neighbors(x, y):
    for dx, dy in ((0,-1),(-1,0),(1,0),(0,1)):
        yield (x + dx, y + dy)


def astar(x,y):
    dist = [[XXX]*width for r in world]
    todo = set([(x,y)])
    next = set()
    first = True
    while todo or next:
        if not todo:
            todo = next
            next = set()
        x,y = todo.pop()
        dmin = XXX
        for nx, ny in neighbors(x,y):
            w = world[ny][nx]
            d = dist[ny][nx]
            if (w == '.') and (d == XXX):
                next.add((nx,ny))
            dmin = min(dmin, d)
        if first and dmin==XXX: dmin = -1
        if dmin < XXX:
            dist[y][x] = dmin + 1
        first = False
    return dist


def show_world(dist=None):
    if DEBUG < 1:
        return
    if DEBUG == 1:
        print "\x1b[1;1d"

    if index < len(units):
        print "during round %d, elf strength %d, unit %d/%d: %s" % (round, elf_strength, index + 1, len(units), units[index]),
    else:
        print "end of round %d, elf strength %d" % (round, elf_strength),
        if DEBUG > 2:
            print 60 * '=',

    if DEBUG == 1:
        print "\x1b[K"
    else:
        print

    for y in xrange(height):
        if dist:
            print ''.join((DIST_VIS_MAP[d] if d<XXX else w) for w,d in zip(world[y], dist[y])),
        else:
            print ''.join(world[y]),
        print ", ".join("%s(%d)" % (u.team, u.hp) for u in sorted(u for u in units if u.y == y)),
        if DEBUG == 1:
            print "\x1b[K"
        else:
            print
    print


def simulate(data=None, elf_strength_=3, expected_result=None):
    global world, units, width, height, round, index, elf_strength
    elf_strength = elf_strength_
    print "running simulation with elf_strength=%d" % elf_strength
    
    world = [list(x.strip()) for x in
             (data.strip().split('\n') if data else open("input.txt"))]
    height = len(world)
    width = len(world[0])

    units = []
    for y, row in enumerate(world):
        for x, cell in enumerate(row):
            if world[y][x] in "EG":
                units.append(Unit(x,y))

    round = 0
    index = 0
    elf_deaths = 0

    show_world()

    if DEBUG == 1:
        print "\x1b[2J"
    
    while True:
        # finish current / begin next round
        if index >= len(units):
            round += 1
            show_world()
            if STOP_AT_ROUND and (round >= STOP_AT_ROUND):
                break
            index = 0
            units.sort()

        # check exit condition
        if len(set(u.team for u in units)) < 2:
            if index:
                index = len(units)
                show_world()
            break

        current = units[index]
        if DEBUG > 2:
            print "BEGIN turn of", current

        # search target point: build distance table, select nearest neighbor 
        dist = astar(current.x, current.y)
        if DEBUG > 4:
            show_world(dist)
        targets = []
        for u in units:
            if u.team != current.team:
                targets.extend((dist[ny][nx], ny, nx, u) for nx, ny in neighbors(u.x, u.y))
        if targets and (DEBUG > 5):
            print "target list for %s:", current
            for td, ty, tx, tu in sorted(targets):
                print "  - dist %3d: %2d %2d towards %s" % (td, tx, ty, tu)
        td, ty, tx, tu = min(targets) if targets else (XXX, 0, 0)

        # move unit (if possible): build reverse distance table to select direction
        if (td > 0) and (td < XXX):
            if DEBUG > 2:
                print current, "selects move target:", tx, ty
            dist = astar(tx, ty)
            if DEBUG > 4:
                show_world(dist)
            md, my, mx = min((dist[my][mx], my, mx) for mx, my in neighbors(current.x, current.y))
            assert md < XXX
            if DEBUG > 2:
                print current, "moves to", mx, my
            current.move(mx, my)

        # select attackable unit
        n = set(neighbors(current.x, current.y))
        try:
            dummy, enemy, index2 = min((u.hp, u, i) for i,u in enumerate(units) if ((u.x, u.y) in n) and (u.team != current.team))
        except ValueError:
            enemy = None
        if enemy:
            if DEBUG > 2:
                print current, "attacks", enemy
            enemy.hp -= elf_strength if current.team=='E' else 3
            if enemy.hp <= 0:
                if DEBUG > 2:
                    print enemy, "dies"
                if enemy.team == 'E':
                    elf_deaths += 1
                    if elf_strength != 3:
                        print "stop after Elf death in round", round
                        return 'X', 1
                world[enemy.y][enemy.x] = '.'
                del units[index2]
                if index2 < index:
                    index -= 1

        if DEBUG > 2:
            print "END turn of", current
        if (DEBUG == 1) or (DEBUG > 3):
            show_world()
        index += 1

    total_hp = sum(u.hp for u in units)
    teams_left = ','.join(sorted(set(u.team for u in units)))
    print "stop: round %d, %d units, %d HPs, teams %s, %d Elf deaths" % \
          (round, len(units), total_hp, teams_left, elf_deaths)
    result = round * total_hp
    print "result:", result,
    if not(expected_result) or STOP_AT_ROUND:
        print
    elif result == expected_result:
        print "-- correct!"
    else:
        print "-- INCORRECT! (expected %d)" % expected_result
        return None, elf_deaths
    return teams_left, elf_deaths


def simulate_full(data=None, expected_result_3=None, expected_result_N=None, expected_elf_strength=None):
    elf_strength = 3
    while True:
        res, elf_deaths = simulate(data=data, elf_strength_=elf_strength,
                          expected_result={3:expected_result_3, expected_elf_strength:expected_result_N}.get(elf_strength))
        if not(res) or not(elf_deaths):
            break
        elf_strength += 1
    if expected_elf_strength:
        if elf_strength == expected_elf_strength:
            print "Final elf strength of", elf_strength, "is correct."
        else:
            print "INCORRECT elf strength: expected", expected_elf_strength, "but got", elf_strength
            res = None
    return res


if __name__ == "__main__":
    old_debug = DEBUG
    if 1:
        print "starting regression test ..."
        DEBUG = 0
        import time
        t = time.time()
        for test in [
("""
#######
#.G...#
#...EG#
#.#.#G#
#..G#E#
#.....#
#######
""", 27730, 4988, 15),
("""
#######
#G..#E#
#E#E.E#
#G.##.#
#...#E#
#...E.#
#######
""", 36334, None, None),
("""
#######
#E..EG#
#.#G.E#
#E.##E#
#G..#.#
#..E#.#
#######
""", 39514, 31284, 4),
("""
#######
#E.G#.#
#.#G..#
#G.#.G#
#G..#.#
#...E.#
#######
""", 27755, 3478, 15),
("""
#######
#.E...#
#.#..G#
#.###.#
#E#G#G#
#...#G#
#######
""", 28944, 6474, 12),
("""
#########
#G......#
#.E.#...#
#..##..G#
#...##..#
#...#...#
#.G...G.#
#.....G.#
#########
""", 18740, 1140, 34),
        ]:
            if simulate_full(*test):
                print "--"
            else:
                print "Regression test FAILED."
                break
        else:
            print "Regression test passed in", time.time() - t, "seconds."
        print

    DEBUG = old_debug
    simulate_full()
