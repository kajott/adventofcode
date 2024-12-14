E=enumerate;M={x+1j*y:c for y,l in E(open("input.txt"))for x,c in E(l.strip())}
D=[1,-1,1j,-1j]
def C(r):
 while r:
  i,*o=r;a={i}
  while a!=o:o,a=a,{p+d for p in a for d in[0]+D}&r
  r-=a;yield a
print(sum(len(a)*sum(len([*C({p+d for p in a}-a)])for d in D)for c in range(26)for a in C({p for p in M if M[p]==chr(c+65)})))
