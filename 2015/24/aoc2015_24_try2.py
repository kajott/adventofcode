N=map(int,open("input.txt"))
c={}
def K(i,w):
 if w<1or i<0:return(0,-1,-1)
 if(i,w)in c:return c[(i,w)]
 v=N[i];r=K(i-1,w)
 if v<=w:s,n,q=K(i-1,w-v);r=max(r,(s+v,n-1,q*v))
 c[(i,w)]=r;return r
for d in(3,4):print-K(len(N)-1,sum(N)/d)[2]
