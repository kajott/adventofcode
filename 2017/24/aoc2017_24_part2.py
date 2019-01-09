from collections import*
B=[map(int,l.strip().split('/'))for l in open("input.txt")]
R=defaultdict(set)
def m(s,p,v,l):R[l]|={s};[m(s+sum(b),b[1-b.index(p)],v|{i},l+1)for i,b in enumerate(B)if p in b and not i in v]
m(0,0,{-1},0)
print max(max(R.items())[1])
