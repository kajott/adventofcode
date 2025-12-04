E,t=enumerate,0;a=M={x+1j*y for y,l in E(open("input.txt"))for x,c in E(l.strip())if'.'<c}
while a:t+=len(a:={p for p in M if sum((p+d)in M for d in(-1j-1,-1j,1-1j,-1,+1,1j-1,1j,1j+1))<4});M-=a
print(t)
