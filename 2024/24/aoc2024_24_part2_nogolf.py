#!/usr/bin/env python3
import subprocess

class Gate:
    def __init__(self, line):
        self.a, self.op, self.b, arrow, self.dest = line.split()
        self.a, self.b = min(self.a, self.b), max(self.a, self.b)
        assert arrow == "->"

    def __repr__(self):
        return f"Gate('{self.a} {self.op} {self.b} -> {self.dest}')"

class Circuit:
    def __init__(self):
        self.gates = []
        self.source = {}
        self.refs = {}

    def add(self, line):
        if "->" in line:
            g = Gate(line)
            self.gates.append(g)
            self.source[g.dest] = g
            self.refs[g.dest] = self.refs.get(g.dest, set())
            self.refs[g.a] = self.refs.get(g.a, set()) | {g}
            self.refs[g.b] = self.refs.get(g.b, set()) | {g}

    def draw(self, filename="aoc2024.dot"):
        wires = sorted(self.refs, key=lambda w:
            (w.startswith('z') - w.startswith('y') - w.startswith('x'), w))
        dotfile = filename.rsplit('.',1)[0] + ".dot"
        with open(dotfile, 'w') as f:
            f.write('digraph {\n')
            for w in wires:
                f.write(f'    {w}[shape=box];\n')
            for n, g in enumerate(self.gates):
                n = g.op + str(n)
                f.write(f'    {n}[shape=ellipse,label="{g.op}"];\n')
                f.write(f'    {g.a}, {g.b} -> {n}; {n} -> {g.dest};\n')
            f.write('}\n')
        ext = filename.lower().rsplit('.', 1)[-1]
        if ext != 'dot':
            subprocess.run(["dot", "-T" + ext, "-o" + filename, dotfile], check=True)

    def opstats(self):
        stats = {}
        for g in self.gates:
            stats[g.op] = stats.get(g.op, 0) + 1
        return sorted(stats.items())

def make_adder(bits):
    adder = Circuit()
    adder.add("x00 XOR y00 -> z00")
    adder.add("x00 AND y00 -> c00")
    for bit in range(1, bits+1):
        c_out = f"z{bits+1:02d}" if (bit == bits) else f"c{bit:02d}"
        adder.add(f"x{bit:02d} XOR y{bit:02d} -> hr{bit:02d}")
        adder.add(f"x{bit:02d} AND y{bit:02d} -> hc{bit:02d}")
        adder.add(f"c{bit-1:02d} XOR hr{bit:02d} -> z{bit:02d}")
        adder.add(f"c{bit-1:02d} AND hr{bit:02d} -> fc{bit:02d}")
        adder.add(f"hc{bit:02d} OR fc{bit:02d} -> {c_out}")
    return adder

def check_adder(adder):
    suspicious = set()
    for g in adder.gates:
        ref_ops = {rg.op for rg in adder.refs[g.dest]}
        ins = {g.a, g.b}
        if (g.op == "AND") and (ref_ops != {"OR"}) and not(ins == {"x00", "y00"}):
            suspicious.add(g.dest)
            print(f"{g.dest}: comes from AND gate, doesn't end in OR gate")
        if (g.op == "XOR") and not(g.dest.startswith("z")) and not(ref_ops == {"AND", "XOR"}):
            suspicious.add(g.dest)
            print(f"{g.dest}: comes from XOR gate, doesn't end in AND/XOR combo or zNN output")
        if (g.op == "OR") and g.dest.startswith("z") and any((wire > g.dest) for wire in adder.refs):
            suspicious.add(g.dest)
            print(f"{g.dest}: comes from OR gate, ends in non-MSB output")
        if (g.op == "XOR") and all(i.startswith(("x","y")) for i in ins):
            for c in adder.refs[g.dest]:
                if (c.op == "XOR") and not(c.dest.startswith("z")):
                    suspicious.add(c.dest)
                    print(f"{c.dest}: comes from XOR gate of second half-adder, doesn't end in zNN output")
    return suspicious

if __name__ == "__main__":
    broken = Circuit()
    for line in open("input.txt"):
        broken.add(line)
    broken.draw("aoc2024_24_vis.svg")
    print("broken    adder:", broken.opstats())

    ref = make_adder(44)
    #ref.draw("aoc2024_24_ref.svg")
    print("reference adder:", ref.opstats())

    res = check_adder(broken)
    print("found", len(res), "suspicious outputs:")
    print(','.join(sorted(res)))
