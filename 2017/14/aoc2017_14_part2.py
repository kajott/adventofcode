K="jxqlasbh"
_=range
C=[sum((x>>b)&1for b in _(8))for x in _(256)]
def H(x):
 l,a,s,p=map(ord,x)+[17,31,73,47,23],_(256),0,0
 for l in l*64:a=a[:l][::-1]+a[l:];m=(l+s)&255;s+=1;p+=m;a=a[m:]+a[:m]
 p=-p&255;a=a[p:]+a[:p];x=[reduce(lambda a,b:a^b,a[i:i+16])for i in _(0,256,16)];return[-((x[b/8]>>(~b&7))&1)for b in _(128)]
m,n=[H(K+'-'+str(x))+[0]for x in _(128)]+[[0]*129],0
for y in _(128):
 for x in _(128):
  if m[y][x]<0:
   n+=1;o,v={(y,x)},{0}
   while o:a,b=o.pop();m[a][b]=n;v|={(a,b)};o=o|{(c,d)for c,d in((a+c,b+d)for c,d in((-1,0),(1,0),(0,-1),(0,1)))if m[c][d]<0}-v
print n
