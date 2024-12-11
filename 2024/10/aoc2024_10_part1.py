E=enumerate;M={x+1j*y:int(c)for y,l in E(open("input.txt"))for x,c in E(l.strip())}
S=lambda p,h:set()if M.get(p,-1)!=h else{p}if h>8 else S(p+1j,h+1)|S(p-1j,h+1)|S(p+1,h+1)|S(p-1,h+1)
print(sum(len(S(p,0))for p in M))
