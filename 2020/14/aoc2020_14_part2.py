_=range
M={}
for k,v in(map(str.strip,r.split('='))for r in open("input.txt")):
 if"me"<k:
  a=int(k[4:-1])&A|O
  for c in _(1<<B):M[a+sum(F[b]for b in _(B)if(c>>b)&1)]=int(v)
 else:O=int(v.replace('X','0'),2);F=[1<<i for i in _(len(v))if'A'<v[35-i]];B=len(F);A=~sum(F)
print sum(M.values())
