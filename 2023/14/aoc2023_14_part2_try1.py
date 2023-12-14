H,O,M,E=[],[],{},enumerate
for L,r in E(open("input.txt")):
 for x,c in E(r):M[(x,L)]=c in"O.";O+=[(x,L)]*('A'<c)
def R(u,v):
 O.sort(key=lambda k:-k[0]*u-k[1]*v);f=dict(M)
 for i,(x,y)in E(O):
  while f.get((x+u,y+v)):x+=u;y+=v
  O[i]=(x,y);f[(x,y)]=0
while(O in H)-1:H+=[O[:]];R(0,-1);R(-1,0);R(0,1);R(1,0)
t=len(H);p=t-H.index(O);print(sum(L+1-y for x,y in H[(int(1E9)-t)%p-p]))
