import re
G,v,s={},{0},{0}
for n in(map(int,re.findall('\d+',l))for l in open("input.txt")):G[n[0]]=set(n[1:])
while v:x=v.pop();s|={x};v|=G[x]-s
print len(s)
