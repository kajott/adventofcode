A,B=158126,624574
print sum(all(a<=b for a,b in zip(s,s[1:]))*any(s.count(c)>1for c in s)for s in map(str,range(A,B+1)))
