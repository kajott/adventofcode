print sum(3*a*b+2*b*c+2*a*c for a,b,c in(sorted(map(int,l.split('x')))for l in open("input.txt")))
