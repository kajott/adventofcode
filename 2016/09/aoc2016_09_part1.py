s,c=open("input.txt").read().strip(),0
while'('in s:b=s.find('(');e=s.find(')')+1;l,r=map(int,s[b+1:e-1].split('x'));c+=l*r;s=s[:b]+s[e+l:]
print len(s)+c
