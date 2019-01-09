import re,collections as C
I,F=open("input.txt").read(),re.findall
s,t,d=F('ate (\w)',I),map(int,F('\d+',I)),F('rig|le',I)
P={s[3*i+1]:[(t[4*i+2*j+2],1-2*(d[2*i+j]<'r'),s[3*i+j+2])for j in(0,1)]for i in range(len(d)/2)}
m,p=C.defaultdict(int),0
for x in range(t[0]):m[p],d,s[0]=P[s[0]][m[p]];p+=d
print sum(m.values())
