_,S=int,sorted
import re
t,A,B,w=2,[],0,0
for l in open("input.txt"):
 if':'in l:t-=1
 m=re.match(r'(\d+) u.*h (\d+) h.*s( \((.*)\))? w.*s (\d+) (.*) d.*ve (\d+)',l)
 if m:
  m=m.groups();g=[-_(m[6]),t,_(m[0]),_(m[1]),{},m[5],_(m[4])];A+=[g]
  if m[3]:
   for m in map(str.strip,m[3].split(';')):
    for a in m[8+(m[0]<'w'):].split(','):g[4][a.strip()]=2*(m[0]>'i')
while w<1:
 G,m=[g[:6]+[g[6]+B*g[1]]+[0,1]for g in A],1
 while m:
  w,m=set(g[1]for g in G),0
  if len(w)<2:break
  for g in S(G,key=lambda g:(-g[2]*g[6],g[0])):
   t=S((-g[2]*g[6]*t[4].get(g[5],1),-t[2]*t[6],t[0],t)for t in G if(t[1]-g[1])*t[8])
   if t and t[0][0]:t=t[0];g[7]=t[3];g[7][8]=0;m=1
  for g in S(G):
   if g[7]:t=g[7];t[2]=max(0,t[2]-g[2]*g[6]*t[4].get(g[5],1)/t[3])
  G=[g[:7]+[0,1]for g in G if g[2]>0]
 w=w=={1};B+=1
 if(B<2)+w:print sum(g[2]for g in G)
