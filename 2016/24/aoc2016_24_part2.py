_=enumerate
o={0};p={}
for y,r in _(open("input.txt")):
 for x,c in _(r):
  if'#'!=c:o|={x+y*1j}
  if c.isdigit():p[int(c)]=x+y*1j
def D(i):
 d=0;q={p[i]};m={p[i]:0}
 while q:
  c=q;q=set();d+=1
  for x in c:
   for n in(x+1,x-1,x+1j,x-1j):
    if(n in o)and not n in m:m[n]=d;q|={n}
 return{i:m[p[i]]for i in p}
d={i:D(i)for i in p}
def T(c,r):return min(d[c][i]+T(i,r-{i})for i in r)if r else d[c][0]
print T(0,set(p)-{0})
