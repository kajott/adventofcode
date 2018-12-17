import re
c=[]
for d,f,a,b in (re.match('([xy])=(\d+).*?(\d+)..(\d+)',x).groups()for x in open("input.txt")):f=int(f);c+=[(x,f)if d>'x'else(f,x)for x in range(int(a),int(b)+1)]
x,y=(min(z[i]for z in c)for i in(0,1))
w,h=(max(z[i]for z in c)-(x,y)[i]for i in(0,1))
m=[[0]*(w+2)for i in range(h+1)]
for a,b in c:m[b-y][a-x]=1
def L(x,y,d):
 while m[y][x+d]&1<1and m[y+1][x]&1:x+=d;m[y][x]=2
 return x,m[y+1][x]&1
def D(x,y):
 if m[y][x]&1:return
 s=y;m[y][x]=2
 while y<h and m[y+1][x]&1<1:y+=1;m[y][x]=2
 while h>y>=s and m[y+1][x]&1:
  l,a=L(x,y,-1);r,b=L(x,y,1)
  if a+b>1:
   for f in range(l,r+1):m[y][f]=3
  a or D(l,y);b or D(r,y);y-=1
D(500-x,0);print sum(sum(x/2for x in r)for r in m),sum(sum(x>2for x in r)for r in m)
