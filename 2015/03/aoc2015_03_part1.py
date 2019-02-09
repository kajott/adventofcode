p,v=0,{0}
for c in open("input.txt").read().strip():p+={'<':-1,'>':+1,'^':-1j,'v':1j}[c];v|={p}
print len(v)
