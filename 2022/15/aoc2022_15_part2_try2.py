import re;A=abs
S=[(x,y,A(x-u)+A(y-v)+1)for x,y,u,v in(map(int,re.findall('-?\d+',l))for l in open("input.txt"))]
B,P={0},{a for a in S for b in S if A(a[0]-b[0])+A(a[1]-b[1])==a[2]+b[2]}
X,Y=(sum(s[c]for s in P)/4for c in(0,1))
for x,y,d in P:u=1-2*(X<x);v=1-2*(Y<y);b={(x+i*u)*4000000+y+v*(d-i)for i in range(d)};B=B&b or b
print B.pop()
