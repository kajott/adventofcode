s=0
for r in(sorted(map(int,r.strip().split()))for r in open("input.txt")):
 for i in xrange(len(r)):s+=sum(x/r[i]for x in r[i+1:]if x%r[i]<1)
print s
