print(sum(abs(a-b)for a,b in zip(*map(sorted,zip(*(map(int,l.split())for l in open("input.txt")))))))
