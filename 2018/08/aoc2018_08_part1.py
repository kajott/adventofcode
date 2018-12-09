d,s=map(int, open("input.txt").read().strip().split())[::-1],0
def v():
 n,m=d.pop(),d.pop()
 return sum(v() for i in range(n))+sum(d.pop() for i in range(m))
print v()
