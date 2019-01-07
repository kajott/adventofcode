DEBUG = False  # if True, show all intermediate patterns

ruledata = """
../.# => ##./#../...
.#./..#/### => #..#/..../..../#..#
""".strip('\n').split('\n')
ruledata = open("input.txt")

def parse_pattern(pat):
    return tuple(tuple(int(c=='#') for c in row) for row in pat.strip().split('/'))

def flip(pat):
    return tuple(pat[::-1])

def rotate(pat):
    return flip(zip(*pat))

def dump(pat):
    for row in pat:
        print ''.join(".#"[c] for c in row)
    print

def rotations(pat):
    for r in range(4):
        yield pat
        yield flip(pat)
        pat = rotate(pat)

def enhance(image, block_in, block_out):
    output = []
    for y in range(0, len(image), block_in):
        rows = [[] for i in range(block_out)]
        for x in range(0, len(image[y]), block_in):
            block = tuple(tuple(image[y+i][x:x+block_in]) for i in range(block_in))
            block = rules[block]
            for i in range(block_out):
                rows[i] += list(block[i])
        output += rows
    return output

if __name__ == "__main__":
    # load rules
    rules = {}
    for line in ruledata:
        old, new = line.split("=>")
        rules[parse_pattern(old)] = parse_pattern(new)

    # add rotated and flipped rules
    for old, new in rules.items():
        for rot in rotations(old):
            if not rot in rules:
                rules[rot] = new

    image = ((0,1,0), (0,0,1), (1,1,1))

    if DEBUG:
        dump(image)
    for i in range(18):
        block = 3 if (len(image) & 1) else 2
        image = enhance(image, block, block + 1)
        if i+1 in (5,18):
            print sum(map(sum, image))
        if DEBUG:
            dump(image)
