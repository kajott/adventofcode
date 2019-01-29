import sys
p,d,v=0,1,{0}
for i in map(str.strip,open("input.txt").read().split(',')):
 d*=1j*(1-2*(i[0]<'R'))
 for x in range(int(i[1:])):
  v|={p};p+=d
  if p in v:print int(abs(p.real)+abs(p.imag));sys.exit(0)
