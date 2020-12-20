import re
print sum(int(a)<=p.count(l)<=int(b)for a,b,l,p in(re.match(r'(\d+)-(\d+) (\w): (\w+)',x).groups()for x in open("input.txt")))
