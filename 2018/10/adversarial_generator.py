import sys, random

gen = random.randrange(7000, 15000)
gen = 6502
print >>sys.stderr, gen
noise = 4

image = """
.....##.........
....#..#........
....#..#........
....#..#........
.....#..#.......
.....#...#......
..#####...#.....
.#.....#...#....
.#.....#...##...
.######....#.###
#......#...#.###
#......#...#.###
.######....#.###
.#.....#...#.###
..#...#...###...
...#######......
""".strip().split('\n')
x0 = -len(image[0]) / 2
y0 = -len(image) / 2



stars = set()

def gen_star(x, y, noise=False):
    while True:
        vx = random.randrange(1, 10) * (1 - 2 * random.randrange(2))
        vy = random.randrange(1, 10) * (1 - 2 * random.randrange(2))
        px = x - vx * gen
        py = y - vy * gen
        if noise:
            vx += random.randrange(1, 10) * (1 - 2 * random.randrange(2))
            vy += random.randrange(1, 10) * (1 - 2 * random.randrange(2))
            px += random.randrange(-gen/2, gen/2)
            py += random.randrange(-gen/2, gen/2)
        star = (px, py, vx, vy)
        if vx and vy and abs(vx)<=9 and abs(vy)<=9 and abs(px)<=99999 and abs(py)<=99999 and not(star in stars):
            return stars.add(star)
    

for ry, row in enumerate(image):
    y = y0 + ry
    for rx, cell in enumerate(row):
        if cell != '#':
            continue
        x = x0 + rx
        for n in xrange(noise + 1):
            gen_star(x, y, n)

stars = list(stars)
random.shuffle(stars)
for star in stars:
    print "position=<%6d, %6d> velocity=<%2d, %2d>" % star
s = len(stars) / (noise + 1)
print >>sys.stderr, "%d stars (%d noise, %s real)" % (len(stars), s * noise, s)
