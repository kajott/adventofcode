S,_,E=set(),range,enumerate
for y,r in E(open("input.txt")):S|={(x,y,0)for x,c in E(r)if'#'==c}
N=lambda u,v,w:{(x,y,z)for x in _(u-1,u+2)for y in _(v-1,v+2)for z in _(w-1,w+2)if(x,y,z)!=(u,v,w)}
for t in _(6):
 b=set()
 for p in S:b|=N(*p)
 S={p for p in b-S if len(N(*p)&S)==3}|{p for p in S if 1<len(N(*p)&S)<4}
print len(S)
