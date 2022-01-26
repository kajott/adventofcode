#!/usr/bin/env python3

if __name__ == "__main__":
    print("def monad_unopt(input):")
    print("    x = y = z = w = 0")

    prog = []
    for line in open("input.txt"):
        line = line.split()
        if len(line) == 3:
            op, a, b = line
            try:
                i = int(b)
                b = None
            except ValueError:
                i = None
        else:
            op, a = line
            b = i = None
        line = " ".join(line)
        prog.append((op, a, b, i, line))

    def fetch_next():
        global next_op, next_a, next_b, next_i, next_line
        if pc < (len(prog) - 1):
            next_op, next_a, next_b, next_i, next_line = prog[pc+1]

    def merge():
        global line
        line += "; " + next_line
        del prog[pc+1]
        fetch_next()

    columns = []
    inpos = 0
    pc = 0
    while pc < len(prog):
        op, a, b, i, line = prog[pc]
        fetch_next()
        if op == "inp":
            print()
            expr = f"{a} = input[{inpos}]"
            inpos += 1
            columns.append([])
        elif op == "add":
            if not(b) and (i < 0):
                expr = f"{a} -= {-i}"
            else:
                expr = f"{a} += {b or i}"
        elif op == "mul":
            if not(b) and not(i):
                if (next_op == "add") and (next_a == a):
                    expr = f"{a} = {next_b or next_i}"
                    merge()
                else:
                    expr = f"{a} = 0"
            else:
                expr = f"{a} *= {b or i}"
        elif op == "div":
            expr = f"{a} = div({a}, {b or i})"
        elif op == "mod":
            expr = f"{a} = {a} % {b or i}"
        elif op == "eql":
            if (next_op == "eql") and (next_a == a) and not(next_b) and not(next_i):
                expr = f"{a} = ({a} != {b or i})"
                merge()
            elif not(b) and not(i):
                expr = f"{a} = not({a})"
            else:
                expr = f"{a} = ({a} == {b or i})"
        else:
            print("    # FATAL: invalid opcode:", line)
            break
        print(f"    {expr:<20} # {line}")
        columns[-1].append(expr)
        pc += 1
    print()
    print("    return z")

    maxl = max(max(map(len, c)) for c in columns)
    for line in zip(*columns):
        print("#", "!!!" if len(set(line)) > 1 else "   ", '  '.join(c.ljust(maxl) for c in line).strip())
