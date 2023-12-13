def S(p,r,i=0):
 s=k=a=0;o,l=[],len(p)
 if i>=l:
  for j in range(l):
   if(p[j]<1)*s:
    if j>s:o+=[j-s]
    k+=1;s=0
   elif(s<1)*p[j]:s=j
  a=(r==o)
 elif p[i]>1:p[i]=0;a=S(p,r,i+1);p[i]=1;a+=S(p,r,i+1);p[i]=2
 else:a=S(p,r,i+1)
 return a
print(sum(S([0]+[".#?".index(c)for c in p]+[0],[*map(int,r.split(','))])for p,r in(l.split()for l in open("input.txt"))))
