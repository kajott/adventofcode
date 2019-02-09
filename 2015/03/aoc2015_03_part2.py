p,v,i=[0,0],{0},0
for c in open("input.txt").read().strip():p[i]+={'<':-1,'>':+1,'^':-1j,'v':1j}[c];v|={p[i]};i^=1
print len(v)
