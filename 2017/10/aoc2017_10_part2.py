_=range
l=map(ord,open("input.txt").read().strip())+[17,31,73,47,23]
a,s,p=_(256),0,0
for l in l*64:a=a[:l][::-1]+a[l:];m=(l+s)&255;s+=1;p+=m;a=a[m:]+a[:m]
p=-p&255;a=a[p:]+a[:p]
print''.join("%02x"%reduce(lambda a,b:a^b,a[i:i+16])for i in _(0,256,16))
