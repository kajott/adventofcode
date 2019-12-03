def W(x):
 p=s=0;v={}
 for i in x.split(','):
  d={'L':-1,'R':1,'U':1j,'D':-1j}[i[0]]
  for i in range(int(i[1:])):p+=d;s+=1;v[p]=s
 return v
a,b=map(W,open("input.txt"))
print int(min(a[p]+b[p]for p in set(a)&set(b)))
