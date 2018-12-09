d=map(int, open("input.txt").read().strip().split())[::-1]
def b():
 n,m=d.pop(),d.pop()
 return ([b() for i in range(n)], [d.pop() for i in range(m)])
def v(c,m):
 if c:return sum(v(*c[i-1]) for i in m if i and i<=len(c))
 return sum(m)
print v(*b())
