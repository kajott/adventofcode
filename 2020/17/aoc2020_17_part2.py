S,_,E=set(),range,enumerate
for y,r in E(open("input.txt")):S|={(x,y,0,0)for x,c in E(r)if'#'==c}
N=lambda i,j,k,l:{(x,y,z,w)for x in _(i-1,i+2)for y in _(j-1,j+2)for z in _(k-1,k+2)for w in _(l-1,l+2)if(x,y,z,w)!=(i,j,k,l)}
for t in _(6):
 b=set()
 for p in S:b|=N(*p)
 S={p for p in b-S if len(N(*p)&S)==3}|{p for p in S if 1<len(N(*p)&S)<4}
print len(S)
