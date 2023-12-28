H,R=[[*map(int,l.replace('@',',').split(','))]for l in open("input.txt")],0
for i,(p,q,_,s,t,_)in enumerate(H):
 for u,v,_,x,y,_ in H[:i]:
  if d:=y*s-x*t:z=((u-p)*y+(q-v)*x)/d;m,n=sorted([p+s*z,q+t*z]);R+=(z>0)*(((u-p)*t+(q-v)*s)/d>0)*(m>=2E14)*(n<=4E14)
print(R)
