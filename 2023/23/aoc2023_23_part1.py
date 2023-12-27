S,E,N,F={},enumerate,(1,-1,1j,-1j),{1-1j:0}
for y,l in E(open("input.txt")):
 for x,c in E(l.strip()):p=y*1j+x;F[p]='#'!=c;S[p]=dict(zip("><v^",N)).get(c,0)
G=p-1;F[G+1j]=0
def D(p,v,r=0):
 while r<1:
  v|={p}
  if p==G:r=len(v)-1
  if S[p]:p+=S[p];r=p in v
  else:
   d=[d for d in N if(1-(p+d in v))*F[p+d]]
   if len(d)>1:r=max(D(p+d,set(v))for d in d)+1
   elif d:p+=d[0]
   else:r+=1
 return r-1
print(D(1,{1}))
