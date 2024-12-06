E=enumerate;M={1j*x-y:c for y,l in E(open("input.txt"))for x,c in E(l.strip())}
s,q,l=[p for p in M if'Z'<M[p]][0],{(9,0)},set()
while q:
 o,_=q.pop();m=dict(M);m[o]='#';v,p,n=set(),s,s+1;c=d=1
 while(((p,d)in v)-1)*c:
  v|={(p,d)}
  if'.'>m[n]:d*=1j
  else:p=n
  n=p+d;c=n in m
 l|={*[o]*c}
 if o==9:q=v;print(len({p for p,d in v})+1)
print(len(l))
