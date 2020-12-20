import re
print sum((p[int(a)-1]==l)^(p[int(b)-1]==l)for a,b,l,p in(re.match(r'(\d+)-(\d+) (\w): (\w+)',x).groups()for x in open("input.txt")))
