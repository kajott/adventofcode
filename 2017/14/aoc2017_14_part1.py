K="jxqlasbh"
_=range
C=[sum((x>>b)&1for b in _(8))for x in _(256)]
def H(x):
 l,a,s,p=map(ord,x)+[17,31,73,47,23],_(256),0,0
 for l in l*64:a=a[:l][::-1]+a[l:];m=(l+s)&255;s+=1;p+=m;a=a[m:]+a[:m]
 p=-p&255;a=a[p:]+a[:p];return[reduce(lambda a,b:a^b,a[i:i+16])for i in _(0,256,16)]
print sum(sum(C[b]for b in H(K+'-'+str(x)))for x in _(128))
