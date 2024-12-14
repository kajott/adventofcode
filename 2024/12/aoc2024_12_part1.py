E=enumerate;M={x+1j*y:c for y,l in E(open("input.txt"))for x,c in E(l.strip())}
D,r,s=[1,-1,1j,-1j],{*M},0
while r:
 o=i=r.pop();a={i}
 while a!=o:o,a=a,{p+d for p in a for d in[0]+D if M.get(p+d)==M[i]}
 s+=len(a)*sum(len({p+d for p in a}-a)for d in D);r-=a
print(s)
