E=enumerate
F={1j*y+x:c for y,l in E(open("input.txt"))for x,c in E(l.strip())if'.'!=c}
D=lambda p:F.get(p,'').isdigit()
def V(p):
 s='0'
 while D(p)*D(p-1):p-=1
 while D(p):s+=F[p];p+=1
 return(p,int(s))
print(sum(b for a,b in{V(p+u+v)for p in F for u in(-1,0,1)for v in(-1j,0,1j)if D(p)-1}))
