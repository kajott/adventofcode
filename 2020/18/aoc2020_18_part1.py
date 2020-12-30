import re
T=0
for x in open("input.txt"):
 s=[[1,'*']]
 for t in re.findall('\d+|[+*()]',x):
  if')'==t:t=str(s.pop()[0])
  if')'>t:s+=[[0,'+']]
  elif'0'>t:u+=[t]
  else:
   u=s[-1];t=int(t)
   if'*'<u[1]:u[0]+=t
   else:u[0]*=t
   del u[1]
 T+=s[-1][0]
print T
