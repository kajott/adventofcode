H={}
for r in open("input.txt"):
 r=r.split()
 if not"no"in(r or["no"]):
  H[r[0]+r[1]]=[(int(r[i-1]),r[i]+r[i+1])for i in range(5,len(r),4)]
G=lambda x:1+sum(f*G(y)for f,y in H.get(x,[]))
print G("shinygold")-1
