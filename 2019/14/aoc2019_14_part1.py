R=dict((r[-1][1],(r[-1][0],r[:-1]))for r in([(int(i),c)for i,c in map(str.split,l.replace('=>',',').split(','))]for l in open("input.txt")))
h,l={'FUEL':1},1
while l:
 l=[(c,i)for c,i in h.items()if'ORE'!=c and i>0]
 for c,i in l:
  q,r=R[c];s=(i+q-1)/q;h[c]-=s*q
  for j,c in r:h[c]=h.get(c,0)+s*j
print h['ORE']
