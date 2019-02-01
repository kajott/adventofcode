import re
print sum(int(s)*(c==''.join(x for f,x in sorted((-r.count(x),x)for x in set(r)-{'-'})[:5])) for r,s,c in re.findall('([a-z-]+)(\d+)\[(\w+)',open("input.txt").read()))
