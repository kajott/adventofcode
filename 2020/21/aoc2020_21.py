F,L,X={},[],{}
for l in open("input.txt"):
 i,a=map(str.split,l.strip()[:-1].replace(',','').split("(contains"));L+=i
 for a in a:X[a]=X.get(a,set(i))&set(i)
while X:
 for a,i in X.items():
  if len(i)==1:
   i=i.pop();F[i]=a;del X[a]
   for j in X.values():j-={i}
print sum(not(i in F)for i in L)
print','.join(sorted(F,key=lambda x:F[x]))
