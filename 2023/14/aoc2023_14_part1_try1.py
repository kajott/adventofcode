R,O,M,E=0,[],{},enumerate
for L,r in E(open("input.txt")):
 for x,c in E(r):M[(x,L)]=c in"O.";O+=[(x,L)]*('A'<c)
for(x,y)in O:
 while M.get((x,y-1)):y-=1
 M[(x,y)]=0;R+=L+1-y
print(R)
