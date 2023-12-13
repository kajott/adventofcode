D,S=[],sorted
for l in open("input.txt"):
 h,b=l.split();h=["23456789TJQKA".index(c)for c in h];f={}
 for c in h:f[c]=f.get(c,0)+1
 D+=[([[1,1,1,1,1],[1,1,1,2],[1,2,2],[1,1,3],[2,3],[1,4],[5]].index(S(f.values())),h,int(b))]
print(sum((r+1)*x[2]for r,x in enumerate(S(D))))
