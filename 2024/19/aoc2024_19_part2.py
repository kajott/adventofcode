import functools as F
@F.cache
def D(x):return sum(D(x[len(z):])for z in P if x[:len(z)]==z)if x else 1
S,n=str.strip,-1
for l in open("input.txt"):
 if','in l:P=[*map(S,l.split(','))]
 n+=D(S(l))
print(n)
