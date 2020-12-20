_=range
N=map(int,open("input.txt"))
for i in _(25,len(N)):
 p=N[i-25:i];v={-1};k=N[i]
 for a in p:v|={a+b for b in p if a!=b}
 if not k in v:break
for a in _(i):
 for b in _(a,i):
  r=N[a:b]
  if sum(r)==k:print min(r)+max(r)
