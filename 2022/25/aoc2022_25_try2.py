E="012=-"
s=[0]*99
for l in open("input.txt"):
 i=-1
 for z in l.strip()[::-1]:d=s[i]+{E[x]:x for x in range(-2,3)}[z];c=(d>2)-(d<-2);s[i]=d-5*c;i-=1;s[i]+=c
print''.join(E[d]for d in s).lstrip('0')
