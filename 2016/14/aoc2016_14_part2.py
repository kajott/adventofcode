import re,hashlib as H
c={}
def K(i):
 if i in c:return c[i]
 h="ihaygndm"+str(i)
 for k in range(2017):h=H.md5(h).hexdigest()
 c[i]=h;return h
n,i=64,0
while n:
 i+=1;m=re.search(r'(.)\1\1',K(i))
 if m and any(5*m.group(1)in K(j)for j in range(i+1,i+1001)):n-=1
print i
