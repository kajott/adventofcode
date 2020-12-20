H={}
for r in open("input.txt"):
 r=r.split()
 for i in range(5,len(r),4):x=r[i]+r[i+1];H[x]=H.get(x,[])+[r[0]+r[1]]
def G(x):
 r={x}
 for y in H.get(x,[]):r|=G(y)
 return r
print len(G("shinygold"))-1
