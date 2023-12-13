D,S=[],sorted
def G(p,h,i):
 if i>4:p+=[h]
 elif h[i]:G(p,h,i+1)
 else:
  for c in{*h}:G(p,h[:i]+[c]+h[i+1:],i+1)
for l in open("input.txt"):
 h,b=l.split();h,r,p=["J23456789TQKA".index(c)for c in h],0,[];G(p,h,0)
 for d in p:
  f={}
  for c in d:f[c]=f.get(c,0)+1
  r=max(r,[[1,1,1,1,1],[1,1,1,2],[1,2,2],[1,1,3],[2,3],[1,4],[5]].index(S(f.values())))
 D+=[(r,h,int(b))]
print(sum((r+1)*x[2]for r,x in enumerate(S(D))))
