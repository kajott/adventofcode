import re
G,s={},set()
for n in(map(int,re.findall('\d+',l))for l in open("input.txt")):G[n[0]]=set(n[1:])
r,n=set(G),0
while r:
 v={r.pop()}
 while v:x=v.pop();s|={x};v|=G[x]-s
 r-=s;n+=1
print n
