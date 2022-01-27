E,S,t,_=set(),set(),0,enumerate
for y,l in _(open("input.txt")):E|={(x,y)for x,c in _(l)if'>'==c};S|={(x,y)for x,c in _(l)if'a'<c}
h=y+1;w=max(E)[0]+1;U=V={0}
while(E!=U)+(V!=S):U,V=E,S;t+=1;E={p if q in(E|S)else q for p,q in(((x,y),((x+1)%w,y))for x,y in E)};S={p if q in(E|S)else q for p,q in(((x,y),(x,(y+1)%h))for x,y in S)}
print t
