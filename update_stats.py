#!/usr/bin/env python3
"""
collect statistics from all README.md's to produce STATS.md
"""
import glob
import math
import os
import re
import sys

BarWidth = 5

class Entry:
    def __init__(self, year, day, desc, size=None, runtime=None, order=0):
        self.year = year
        self.day = day
        self.order = order
        self.desc = desc
        self.size = size
        self.time_s = runtime or "&mdash;"
        self.time_t = 0
        if runtime:
            if m := re.search(r'([~<])?\s*([0-9.]+)\s*(s|sec|secs|seconds|ms|m|min|mins|minutes|h|hr|hrs|hours)', runtime):
                t = float(m.group(2))
                unit = m.group(3)
                if   unit == "ms":         unit = 1
                elif unit.startswith('s'): unit = 1000
                elif unit.startswith('m'): unit = 60000
                elif unit.startswith('h'): unit = 3600000
                else: assert 0
                self.time_t = round(t * unit) - (m.group(1) == '<')
                self.time_s = m.group(0).strip()
            else:
                print(f"WARNING: no valid runtime for {self.year}/{self.day:02d}: '{runtime}'", file=sys.stderr)
        self.md = f"[{self.year}, Day {self.day:02d}]({self.year}/{self.day:02d}), {self.desc}"

    def md_line(self, with_year=True):
        if with_year:
            return f"[{self.year}, Day {self.day:02d}]({self.year}/{self.day:02d}), {self.desc}"
        else:
            return f"[Day {self.day:02d}]({self.day:02d}), {self.desc}"

    def __lt__(self, other):
        return (self.year, self.day, self.order) < (other.year, other.day, other.order)
    def size_desc_key(self):
        return (-self.size, self.year, self.day, self.order)
    def runtime_desc_key(self):
        return (-self.time_t, self.year, self.day, self.order)

    def __str__(self):
        return f"[Y{self.year} D{self.day:02d} {self.desc} s={self.size} t={self.time_t}: {self.time_s}]"


def make_bar(value, vmin, vmax, log=False):
    if log:
        value, vmin, vmax = map(math.log, (value, vmin, vmax))
    rel = round((value - vmin) / (vmax - vmin) * (BarWidth * 8 - 1) + 1)
    return " | " + ''.join((' ' if (rel <= c) else chr(0x2590 - min(rel - c, 8))) for c in range(0, BarWidth*8, 8)) + " "


def write_table(f, title, data, year=False, size=0, time=0):
    f.write(f'\n\n## {title}\n\n')
    l1 = l2 = '|'
    if size:
        l1 += '       Size | ' + ' ' * BarWidth + ' |'
        l2 += '-----------:|:' + '-' * BarWidth + '-|'
    if time:
        l1 += ' Runtime | ' + ' ' * BarWidth + ' |'
        l2 += '--------:|:' + '-' * BarWidth + '-|'
    end = "Year, " if year else ""
    end += "Day, Part, Solution"
    l1 += ' ' + end
    l2 += ':' + '-' * len(end)
    f.write(f'{l1}\n{l2}\n')
    for e in data:
        line = ''
        if size:
            if not e.size: continue
            line += f'| {e.size:4d} bytes' + make_bar(e.size, 0, size)
        if time:
            if not e.time_t: continue
            line += f'| {e.time_s:>7s}' + make_bar(e.time_t, 99, time, log=True)
        f.write(f'{line}| {e.md_line(not(year))}\n')


def write_stats(data, year=None):
    if year:
        data = [e for e in data if e.year == year]
    max_size = max(e.size for e in data)
    max_time = max(e.time_t for e in data)
    subdir = f"{year}/" if year else ""
    with open(subdir + "STATS.md", 'w', encoding='utf-8') as f:
        y = f" for {year}" if year else ""
        f.write(f'# Solution Statistics{y}\n')
        f.write('<!-- automatically generated file, do not edit! -->\n')
        f.write('**Table of Contents:**\n')
        f.write('- [All Solutions](#all-solutions)\n')
        f.write('- [Solutions by Size](#solutions-by-size)\n')
        f.write('- [Solutions by Runtime](#solutions-by-runtime)\n')
        write_table(f, "All Solutions", sorted(data), year, size=max_size, time=max_time)
        write_table(f, "Solutions by Size", sorted(data, key=Entry.size_desc_key), year, size=max_size)
        write_table(f, "Solutions by Runtime", sorted(data, key=Entry.runtime_desc_key), year, time=max_time)

if __name__ == "__main__":
    os.chdir(os.path.dirname(sys.argv[0]))
    data = []

    for srcname in glob.glob("20*/*/README.md"):
        in_sol_notes = False
        year, day = map(int, srcname.split('/', 2)[:2])
        with open(srcname, encoding='utf-8', errors='replace') as f:
            for lineno, line in enumerate(f):
                if line.startswith('#') and (line.strip('#').strip().lower() == "solution notes"):
                    in_sol_notes = True
                if in_sol_notes and (m := re.match(r'\s*[*-]\s*(part [12],.*?):\s*(\d+)\s+bytes(.*)', line, flags=re.I)):
                    data.append(Entry(year, day, m.group(1), int(m.group(2)), m.group(3).strip(',').strip(), order=lineno))
    data.sort()

    write_stats(data)
    for year in sorted(set(e.year for e in data)):
        write_stats(data, year)
