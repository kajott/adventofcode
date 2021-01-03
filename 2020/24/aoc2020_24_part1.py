import re
D,F={'e':2,'w':-2,'se':1+1j,'sw':1j-1,'ne':1-1j,'nw':-1-1j},{}
for l in open("input.txt"):p=sum(D[x]for x in re.findall('|'.join(D),l));F[p]=1-F.get(p,0)
print sum(F.values())
