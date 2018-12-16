import re, collections

OPS = {
    "addr": lambda r,a,b: r[a] + r[b],
    "addi": lambda r,a,b: r[a] + b,
    "mulr": lambda r,a,b: r[a] * r[b],
    "muli": lambda r,a,b: r[a] * b,
    "banr": lambda r,a,b: r[a] & r[b],
    "bani": lambda r,a,b: r[a] & b,
    "borr": lambda r,a,b: r[a] | r[b],
    "bori": lambda r,a,b: r[a] | b,
    "setr": lambda r,a,b: r[a],
    "seti": lambda r,a,b: a,
    "gtir": lambda r,a,b: a > r[b],
    "gtri": lambda r,a,b: r[a] > b,
    "gtrr": lambda r,a,b: r[a] > r[b],
    "eqir": lambda r,a,b: a == r[b],
    "eqri": lambda r,a,b: r[a] == b,
    "eqrr": lambda r,a,b: r[a] == r[b],
}

possible_opcode_map = collections.defaultdict(lambda: set(OPS))
final_opcode_map = {}

def check_instruction(before, after, op, a, b, d):
    r = before[:]
    r[d] = op(r, a, b)
    return (r == after)

def decode_instruction(before, after, opcode, a, b, d):
    maybe = set(name for name, op in OPS.iteritems() \
                if check_instruction(before, after, op, a, b, d))
    assert maybe
    possible_opcode_map[opcode].intersection_update(maybe)
    assert possible_opcode_map[opcode]
    return len(maybe)

def finalize_opcode_map():
    global final_opcode_map
    assigned_instr = set()
    while len(final_opcode_map) < len(possible_opcode_map):
        for opcode, possible in possible_opcode_map.iteritems():
            possible = possible - assigned_instr
            if len(possible) == 1:
                name = possible.pop()
                assigned_instr.add(name)
                final_opcode_map[opcode] = OPS[name]

if __name__ == "__main__":
    before = None
    instr = None
    final_map = False
    part1_result = 0
    regs = [0,0,0,0]
    for line in (re.findall('(.*?)(\d+) (\d) (\d) (\d)', x.replace(',','')) for x in open("input.txt")):
        if not line: continue
        line = line[0]
        numbers = map(int, line[1:])
        if line[0].startswith('B'):
            before = numbers
        elif line[0].startswith('A'):
            part1_result += (decode_instruction(before, numbers, *instr) >= 3)
            before = None
        elif before:
            instr = numbers
        else:
            if not final_opcode_map:
                finalize_opcode_map()
            op, a, b, d = numbers
            regs[d] = final_opcode_map[op](regs, a, b)
    print part1_result
    print regs[0]
