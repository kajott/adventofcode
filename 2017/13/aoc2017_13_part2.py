S,d=[[int(x.strip())for x in l.split(':')]for l in open("input.txt")],0
def P(t,p):m=p*2-2;y=t%m;return abs(m*(y>=p)-y)
while any(P(t+d,p)<1for t,p in S):d+=1
print d
