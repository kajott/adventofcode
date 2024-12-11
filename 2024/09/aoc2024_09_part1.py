M=[]
for i,s in enumerate(map(int,open("input.txt").read().strip())):M+=[-1 if i&1 else i//2]*s
i=s=0;j=len(M)-1
while i<=j:
 while M[j]<0:j-=1
 if M[i]<0:M[i]=M[j];j-=1
 s+=M[i]*i;i+=1
print(s)
