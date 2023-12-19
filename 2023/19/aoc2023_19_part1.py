R,A,S={},0,str.split
for l in open("input.txt"):
 if'`'<l[0]<'{':
  n,r=l.split('{');e=R[n]=[]
  for r in S(S(r,'}')[0],','):
   if':'in r:r,t=S(r,':');g='>'in r;v,c=S(r,"<>"[g]);e+=[(v,g,int(c),t)]
   else:e+=[('x',1,0,r)]
 if'z'<l[0]:
  p={k:int(v)for k,v in(S(v,'=')for v in S(S(l[1:],'}')[0],','))};r,i="in",0
  while(r in"AR")-1:v,g,c,t=R[r][i];r,i=(c<p[v]if g else p[v]<c)and(t,0)or(r,i+1)
  if'B'>r:A+=sum(p.values())
print(A)
