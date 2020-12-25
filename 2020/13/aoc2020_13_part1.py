import re
N=map(int,re.findall('\d+',open("input.txt").read()))
S=N.pop(0)
a,b=min(((n-S%n)%n,n)for n in N)
print a*b
