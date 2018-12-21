_=range
n=[[0]+[".|#".index(c)for c in r.strip()]+[0]for r in open("input.txt")]
w,h=len(n[0]),len(n)
n[:0]=[[0]*w];n+=[[0]*w]
H,k,t={},0,0
while not k in H:
 H[k]=t;o=[r[:]for r in n];t+=1
 for y in _(1,h+1):
  for x in _(1,w-1):
   c=o[y][x];s=3*[0];s[c]-=1
   for v in _(y-1,y+2):
    for u in _(x-1,x+2):s[o[v][u]]+=1
   if c<1and s[1]>2:c=1
   elif c==1and s[2]>2:c=2
   elif c>1and s[1]*s[2]<1:c=0
   n[y][x]=c
 k=''.join(''.join(chr(48+x)for x in r)for r in n)
s=H[k];s+=(1000000000-s)%(t-s)
for m,t in H.items():
 if t==s:print m.count('1')*m.count('2')
