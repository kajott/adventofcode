print sum(2*(a+b)+a*b*c for a,b,c in(sorted(map(int,l.split('x')))for l in open("input.txt")))
