R=[(a[0],int(b))for a,b in map(str.split,open("input.txt"))];L=len(R)
for m in range(L):
 C=R[:];i=C[m];C[m]=({"j":"n","n":"j"}.get(i[0],i[0]),i[1]);v,p,a={L},0,0
 while not p in v:
  o,x=C[p];d=1
  if"b">o:a+=x
  if"j"==o:d=x
  v|={p};p+=d
 if p==L:print a
