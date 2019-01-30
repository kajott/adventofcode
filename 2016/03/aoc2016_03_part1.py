print sum(a+b>c for a,b,c in(sorted(map(int,l.split()))for l in open("input.txt")))
