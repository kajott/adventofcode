import re

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

ip = 0
regs = 6*[0]
prog = []

#regs[0] = 1

for l in open("input.txt"):
    n=map(int,re.findall('\d+',l))
    l=l.split()[0]
    if l=='#ip': ip=n[0]
    else: prog.append([l, OPS[l]] + n)

t = 0
while 0 <= regs[ip] < len(prog):
    o,f,a,b,d = prog[regs[ip]]
    if d == 0:
        print "%8d ip=%2d" % (t, regs[ip]), "[%s]" % ', '.join("%5d"%x for x in regs), "%s %2d %2d %2d" % (o, a, b, d),
    regs[d] = f(regs, a, b)
    if d == 0:
        print "[%s]" % ', '.join("%5d"%x for x in regs)
    regs[ip] += 1
    t += 1

print "TERMINATED: ticks=%d, ip=%r, regs=%r" % (t, regs[ip], regs)
