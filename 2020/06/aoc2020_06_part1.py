print sum(len(set(x)-{"\n"})for x in open("input.txt").read().split("\n\n"))
