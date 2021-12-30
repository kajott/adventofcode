G,T=set(),lambda g,a:{(y,x)for x,y in g}if'x'<a[-1]else g
for l in open("input.txt"):
 if','in l:G|={tuple(map(int,l.split(',')))}
 if'='in l:a,p=l.split('=');p=int(p);G=T({(x if x<p else 2*p-x,y)for x,y in T(G,a)},a);break
print len(G)
