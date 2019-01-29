p,d=0,1
for i in map(str.strip,open("input.txt").read().split(',')):d*=1j*(1-2*(i[0]<'R'));p+=d*int(i[1:])
print int(abs(p.real)+abs(p.imag))
