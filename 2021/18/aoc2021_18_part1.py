s=0
for l in open("input.txt"):
 l=[{'[':-1,']':-2}.get(x)or int(x)for x in l.strip().replace(',','')]
 s=[-1]+s+l+[-2]if s else l
 while 1:
  a=b=n=g=l=-1
  for i,x in enumerate(s):
   l+={-1:1,-2:-1}.get(x,0)
   if(x<0)*(l>3)*(n<0):n=i
   if(x>9)*(g<0):g=i
   if x>=0:
    if n<0:a=i
    elif i>n+2:b=i;break
  if n>=0:
   if a>=0:s[a]+=s[n+1]
   if b>=0:s[b]+=s[n+2]
   s[n:n+4]=[0]
  elif g>=0:x=s[g];s[g:g+1]=[-1,x/2,x-x/2,-2]
  else:break
while len(s)>1:
 i=3
 while i<len(s):
  if(s[i-3]==-1)*(s[i]==-2):s[i-3:i+1]=[3*s[i-2]+2*s[i-1]]
  i+=1
print s[0]
