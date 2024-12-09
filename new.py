#!/usr/bin/env python3
"""
Generate a new daily puzzle directory and populate it with template files.
"""
import argparse
import os
import sys
import time

FileTemplates = [
    ("aoc{year}_{day}_part1.py", """
# any numbers in the entire file
import re;N=re.findall(r'\d+',open("input2.txt").read())

# one number per line
N=[*map(int,open("input2.txt"))]

# comma-separated numbers per line (2D array)
N=[[*map(int,l.split(','))]for l in open("input2.txt")]

# every character in a dict, indexed by complex numbers
E=enumerate;M={x+1j*y:c for y,l in E(open("input2.txt"))for x,c in E(l.strip())}

# iterate over lines
for l in open("input2.txt"):
 0
""".lstrip()),
    "aoc{year}_{day}_part2.py",
    ("README.md", """

## Solution Notes

"""),
    "input.txt",
    "input2.txt",
]

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("day", metavar="YYYY/DD|DD", nargs='?',
                        help="day to create [default: auto-detect]")
    parser.add_argument("-f", "--force", action='store_true',
                        help="force overwriting an existing directory")
    args = parser.parse_args()

    try:
        if not args.day:
            year, day = 0, 0
        elif ('-' in args.day) or ('/' in args.day):
            year, day = (int(x, 10) for x in args.day.replace('-', '/').split('/', 1))
        else:
            year, day = 0, int(args.day)
    except ValueError:
        parser.error("invalid number in day specification")

    if not year:
        year = time.localtime().tm_year
    elif year < 2015:
        year += 2015
    year = str(year)
    yeardir = os.path.join(os.path.normpath(os.path.abspath(os.path.dirname(sys.argv[0]))), year)
    if not os.path.isdir(yeardir):
        parser.error(f"year directory ('{yeardir}') doesn't exist")

    autoinc = False
    if not day:
        day, autoinc = 1, True
    while True:
        daydir = os.path.join(yeardir, f"{day:02d}")
        if not(os.path.exists(daydir)) or (not(autoinc) and args.force):
            break
        if autoinc:
            day += 1
        else:
            parser.error(f"day directory ('{daydir}') already exists")
    day = f"{day:02d}"

    print("creating directory:", daydir)
    try:
        os.mkdir(daydir)
    except EnvironmentError as e:
        if not args.force:
            print(f"ERROR: failed to create day directory '{daydir}' - {e}", file=sys.stderr)
            sys.exit(1)
    try:
        os.chdir(daydir)
    except EnvironmentError as e:
        print(f"ERROR: failed to change into day directory '{daydir}' - {e}", file=sys.stderr)
        sys.exit(1)

    files = []
    for filespec in FileTemplates:
        if isinstance(filespec, str):
            filename, contents = filespec, ""
        else:
            filename, contents = filespec
        filename = filename.format(year=year, day=day)
        files.append(filename)
        filename = os.path.join(daydir, filename)
        if contents:
            print("creating file from template:", filename)
        else:
            print("creating empty file:", filename)
        with open(filename, 'w') as f:
            f.write(contents)

    print("done - you may now want to do:")
    print(f"    cd {daydir}")
    print(f"    mv ~/Downloads/input.txt .")
    print( "    code", " ".join(files))
