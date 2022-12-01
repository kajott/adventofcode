print sum(sorted(sum(map(int,E.split()))for E in open("input.txt").read().split("\n\n"))[-3:])
