_=range
d,s=map(int,open("input.txt").read().strip().split())[::-1],0
def v():n,m=d.pop(),d.pop();return sum(v()for i in _(n))+sum(d.pop()for i in _(m))
print v()
