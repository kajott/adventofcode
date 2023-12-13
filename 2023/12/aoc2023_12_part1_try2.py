M={}
def S(p,r,c=0):
 p,i,k,a=p[1:],p[:1],(p,r,c),0
 if k in M:a=M[k]
 elif c>r[0]:0
 elif'!'>i:a=(r[0]==c)*(sum(r[1:])<1)
 else:
  if'.'!=i:a=S(p,r,c+1)
  if'#'!=i:a+=S(p,r)if c<1 else(c==r[0])*S(p,r[1:])
 M[k]=a;return a
print(sum(S(p,tuple([*map(int,r.split(','))]+[0]))for p,r in(l.split()for l in open("input.txt"))))
