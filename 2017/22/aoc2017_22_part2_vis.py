execfile("aoc2017_22_part2.py")
R=lambda z:range(min(z),max(z)+1)
X=R([int(x.real)for x in M])
Y=R([int(x.imag)for x in M])
open("vis.ppm",'wb').write("P6\n%d %d\n255\n"%(len(X),len(Y))+''.join(''.join(("---","\0\0\xe0","\xff\0\0","\0~\0","\0\0\0")[M.get(x+y*1j,4)]for x in X)for y in Y))
