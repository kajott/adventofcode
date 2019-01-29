import re,hashlib as H
K=lambda i:H.md5("ihaygndm"+str(i)).hexdigest()
n,i=64,0
while n:
 i+=1;m=re.search(r'(.)\1\1',K(i))
 if m and any(5*m.group(1)in K(j)for j in range(i+1,i+1001)):n-=1
print i
