def D(s):
 c=0
 while'('in s:b=s.find('(');e=s.find(')')+1;l,r=map(int,s[b+1:e-1].split('x'));c+=D(s[e:e+l])*r;s=s[:b]+s[e+l:]
 return len(s)+c
print D(open("input.txt").read().strip())
