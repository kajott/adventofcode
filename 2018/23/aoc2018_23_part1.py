import re
b=[map(int,re.findall('-?\d+',x))[::-1]for x in open("input.txt")]
r,u,v,w=max(b)
print sum(abs(x-u)+abs(y-v)+abs(z-w)<=r for d,x,y,z in b)
