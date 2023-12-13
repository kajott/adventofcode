#!/usr/bin/env python3
import functools

@functools.cache
def permutations(pattern, runs, current_run=0):
    if (runs and (current_run > runs[0])) or (current_run and not(runs)):
        # current run length exceeds template -> impossible
        return 0
    if not(pattern):
        # pattern finished!
        result = ((len(runs) == 1) and (runs[0] == current_run)) if current_run else not(runs)
        return int(result)
    result = 0
    if pattern[0] != '.':  # -> '#' or '?'
        # start or continue run
        result += permutations(pattern[1:], runs, current_run+1)
    if pattern[0] != '#':  # -> '.' or '?'
        if not current_run:
            # continuation of empty run (a.k.a. "another dot")
            result += permutations(pattern[1:], runs, 0)
        elif current_run == runs[0]:
            # end of run, continue with next
            result += permutations(pattern[1:], runs[1:], 0)
        # else: end of run, but run mismatch
    return result

def run_part(multiply):
    result = 0
    for line in open("input.txt"):
        pattern, runs = line.split()
        runs = [*map(int, runs.split(','))] * multiply
        pattern = '?'.join([pattern] * multiply)
        result += permutations(pattern, tuple(runs))
    print(result)

if __name__ == "__main__":
    run_part(1)
    run_part(5)
