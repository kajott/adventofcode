p=0
for l in open("input.txt"):p+={"f":+1j,"d":1,"u":-1}[l[0]]*int(l.split()[1])
print int(p.real*p.imag)
