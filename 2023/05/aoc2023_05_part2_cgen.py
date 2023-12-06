#!/usr/bin/env python3
import subprocess
import time
import re
import os

CFile = "a.c"

if __name__ == "__main__":
    map_names = []
    maps = []
    with open("input.txt") as f:
        seeds = list(map(int, f.readline().split()[1:]))
        for line in f:
            if not line.strip(): continue
            if "map" in line:
                map_names.append(line.split()[0])
                maps.append([])
            else:
                maps[-1].append(list(map(int, line.split())))

    with open(CFile, "w") as c:
        c.write('''// auto-generated
#include <stdint.h>
#include <stdio.h>

uint64_t run(uint64_t min, uint64_t start, uint64_t length) {
    uint64_t end = start + length;
    printf("%010ld...%010ld (%010ld) ", start, end, length); fflush(stdout);
    for (uint64_t initial = start;  initial < end;  ++initial) {
        uint64_t n = initial;
''')

        for name, ranges in zip(map_names, maps):
            c.write(f'\n        // {name} map\n')
            marker = "end_" + name.replace('-', '_')
            for dest, src, length in ranges:
                c.write(f'        if ((n >= {src}ul) && (n < {src + length}ul)) {{ n = n - {src}ul + {dest}ul; goto {marker}; }}\n')
            c.write(f'{marker}:\n')

        c.write('''
        if (n < min) { min = n; }
    }
    printf("-> min=%ld\\n", min);
    return min;
}

int main() {
    uint64_t min = 99999999999ul;
''')
        for start, length in zip(seeds[0::2], seeds[1::2]):
            c.write(f'    min = run(min, {start}ul, {length}ul);\n')
        c.write('    return 0;\n}\n')

    subprocess.run([os.getenv("CC", "cc"), "-O3", "-march=native", CFile])
    t0 = time.time()
    subprocess.run(["./a.out"])
    dt = time.time() - t0

    total = sum(seeds[1::2])
    print(f"total time taken: {dt:.2f} seconds")
    print("total iterations:", total)
    print(f"time per iteration: {dt*1E9/total:.1f} ns")
    try:
        res = subprocess.run(["lscpu"], capture_output=True)
        mhz = float(re.search(r'max mhz\s*:\s*([0-9.,]+)', res.stdout.decode(errors='ignore'), flags=re.I).group(1).replace(',', '.'))
        print(f"CPU nominal clock speed: {mhz:.0f} MHz")
        print(f"avg clocks per iteration: {dt*mhz*1E6/total:.1f}")
    except (EnvironmentError, ValueError, AttributeError):
        pass
