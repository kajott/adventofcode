#!/usr/bin/env python2
import sys, os, re, argparse, subprocess

CFILE = "a.c"
EXEFILE = "./a.out"

COMPILE = ["cc", "-O9", CFILE, "-o", EXEFILE]

OPS = {
    "set": "A = B",
    "sub": "A -= B",
    "mul": "A *= B",
    "jnz": "if (A) ip += B - 1",
}

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("infile", default="input.txt", nargs='?',
                        help="input program file name")
    parser.add_argument("-v", "--r0", metavar="N", type=int, default=0,
                        help="set initial value of a [default: %(default)s]")
    parser.add_argument("-k", "--keep", action='store_true',
                        help="keep C output (%s)" % CFILE)
    args = parser.parse_args()

    c = open("a.c", 'w')
    print >>c, "#include <stdio.h>"
    print >>c, "int ip, a = %d, b, c, d, e, f, g, h;" % args.r0
    print >>c, "int main(void) {"
    print >>c, "  for (;;) {"
    print >>c, "    switch(ip) {"

    addr = 0
    for line in open(args.infile):
        op, a, b = line.strip().split()
        print >>c, "      case %d: %s; break;" % (addr, OPS[op].replace('A', a).replace('B', b))
        addr += 1 

    print >>c, "      default: printf(\"%d\\n\", h); return 0;"
    print >>c, "    }"
    print >>c, "    ip++;"
    print >>c, "  }"
    print >>c, "}"
    c.close()

    res = subprocess.call(COMPILE)
    if res:
        sys.exit(res)
    if not args.keep:
        os.unlink(CFILE)

    sys.exit(subprocess.call([EXEFILE]))
