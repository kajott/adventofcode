R,E,N={0},enumerate,26501365
for M,l in E(open("input.txt")):
 for x,c in E(l.strip()):
  if'.'>c:R|={(x,M)}
  if'A'<c:e={(x,M)}
M+=1;t,h,c=0,[],[set(),set()]
while t<M*3:t+=1;q=c[t&1];e={(x+u,y+v)for x,y in e for u,v in((1,0),(-1,0),(0,1),(0,-1))if(((x+u)%M,(y+v)%M)in R)-1}-q;q|=e;h+=[len(q)]*(t%M==N%M)
a,b,c=h;N//=M
print(a+N*(4*b-3*a-c+N*(c-2*b+a))//2)
