import re
n,m=map(int,re.findall('\d+',open("input.txt").read()))
t,p,s=[0],0,n*[0]
for i in range(1,m+1):
 l=len(t);p=(p+2)%l
 if i%23:t.insert(p,i)
 else:p=(p+l-9)%l;s[(i-1)%n]+=i+t.pop(p)
print max(s)
