s="1321131112"
for i in range(50):
 l,n,r=s[0],1,""
 for c in s[1:]+"x":
  if c==l:n+=1
  else:r+=str(n)+l;l=c;n=1
 s=r
print len(s)
