#!/usr/bin/env python2
import sys, os, re, argparse, subprocess

CFILE = "a.c"
EXEFILE = "./a.out"

COMPILE = ["cc", "-O9", CFILE, "-o", EXEFILE]

OPS = {
    "addr": "rA + rB",
    "addi": "rA + B",
    "mulr": "rA * rB",
    "muli": "rA * B",
    "banr": "rA & rB",
    "bani": "rA & B",
    "borr": "rA | rB",
    "bori": "rA | B",
    "setr": "rA",
    "seti": "A",
    "gtir": "A > rB",
    "gtri": "rA > B",
    "gtrr": "rA > rB",
    "eqir": "A == rB",
    "eqri": "rA == B",
    "eqrr": "rA == rB",
}

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("infile", default="input.txt", nargs='?',
                        help="input program file name")
    parser.add_argument("-v", "--r0", metavar="N", type=int, default=0,
                        help="set initial value of r0 [default: %(default)s]")
    parser.add_argument("-k", "--keep", action='store_true',
                        help="keep C output (%s)" % CFILE)
    args = parser.parse_args()

    c = open("a.c", 'w')
    print >>c, "#include <stdio.h>"
    print >>c, "int r0 = %d, r1, r2, r3, r4, r5;" % args.r0
    print >>c, "int main(void) {"
    print >>c, "  for (;;) {"

    addr = 0
    for line in open(args.infile):
        n = map(int, re.findall('\d+', line))
        op = line.split()[0]
        if op == "#ip":
            ip = "r%d" % n[0]
            print >>c, "    switch (%s) {" % ip
        else:
            print >>c, "      case %d: r%d = %s; break;" % (addr, n[2], OPS[op].replace('A', str(n[0])).replace('B', str(n[1])))
            addr += 1 

    print >>c, "      default: printf(\"%d\\n\", r0); return 0;"
    print >>c, "    }"
    print >>c, "    %s++;" % ip
    print >>c, "  }"
    print >>c, "}"
    c.close()

    res = subprocess.call(COMPILE)
    if res:
        sys.exit(res)
    if not args.keep:
        os.unlink(CFILE)

    sys.exit(subprocess.call([EXEFILE]))
