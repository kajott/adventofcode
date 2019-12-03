def W(x):
 p,v=0,set()
 for i in x.split(','):
  d={'L':-1,'R':1,'U':1j,'D':-1j}[i[0]]
  for i in range(int(i[1:])):p+=d;v|={p}
 return v
a,b=map(W,open("input.txt"))
print int(min(p.real+p.imag for p in a&b))
