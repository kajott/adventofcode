def P(t,p):m=p*2-2;y=t%m;return abs(m*(y>=p)-y)
print sum(t*p*(P(t,p)<1)for t,p in([int(x.strip())for x in l.split(':')]for l in open("input.txt")))
