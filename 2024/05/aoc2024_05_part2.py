S,s=str.split,0;R,U=([[*map(int,S(l.replace('|',','),','))]for l in S(p)]for p in S(open("input.txt").read(),'\n\n'))
for u in U:
 w,c=0,1
 while c:
  c=0
  for a,b in R:
   if(a in u)*(b in u):
    x,y=(i:=u.index)(a),i(b)
    if x>y:u[x],u[y]=b,a;w=c=1
 s+=u[len(u)//2]*w
print(s)
