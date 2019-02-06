n=sorted(int(n)for n in(l.split()[1]for l in open("input.txt")if l[0]=='c')if n.isdigit())
print 2730-n[-1]*n[-2]
