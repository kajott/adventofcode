a,s,p=range(256),0,0
for l in map(int,open("input.txt").read().strip().split(',')):a=a[:l][::-1]+a[l:];m=(l+s)&255;s+=1;p+=m;a=a[m:]+a[:m]
p=-(p-1)&255
print a[p-1]*a[p]
