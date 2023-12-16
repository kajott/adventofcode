import re
B,E=[[]for _ in range(256)],enumerate
for n,o,f in re.findall('(\w+)([=-])(\d*)',open("input.txt").read()):
 h=i=0
 for c in n:h=(h+ord(c))*17&255
 t=B[h]
 while i<len(t)and t[i][0]!=n:i+=1
 t[i:i+1]=[(n,int("0"+f))]*(o>'-')
print(sum(i*j*z[1]for i,t in E(B,1)for j,z in E(t,1)))
