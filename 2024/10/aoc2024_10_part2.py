E=enumerate;M={x+1j*y:int(c)for y,l in E(open("input.txt"))for x,c in E(l.strip())}
S=lambda p,h:0 if M.get(p,-1)!=h else 1 if h>8 else sum(S(p+d,h+1)for d in(-1,1,-1j,1j))
print(sum(S(p,0)for p in M))
