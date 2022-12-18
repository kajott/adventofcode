G={tuple(map(int,l.split(',')))for l in open("input.txt")}
print-sum((tuple(p[i]+d*(a==i)for i in(0,1,2))in G)-1for d in(-1,1)for a in(0,1,2)for p in G)
