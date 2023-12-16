D,U,E,L=1j,-1j,enumerate,-1
M={y*1j+x:c for y,r in E(open("input.txt"))for x,c in E(r)}
A,N=0,int(len(M)**.5)-1
for x in range(N+1):
 for b in[{(x,D)},{(x*D,1)},{(N+x*D,L)},{(N*D+x,U)}]:
  v=set()
  while b:
   p,d=b.pop();n={'.':[{1},{L},{D},{U}],'|':[{U,D},{U,D},{D},{U}],'-':[{1},{L},{1,L},{1,L}],'/':[{U},{D},{L},{1}],'\\':[{D},{U},{1},{L}]}.get(M.get(p))
   if n:v|={(p,d)};b|={(p+d,d)for d in n[(1,L,D,U).index(d)]}-v
  A=max(A,len({p for p,d in v}))
print(A)
