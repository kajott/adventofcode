C=[(a[0],int(b))for a,b in map(str.split,open("input.txt"))]
v,p,a={-1},0,0
while not p in v:
 o,x=C[p];d=1
 if"b">o:a+=x
 if"j"==o:d=x
 v|={p};p+=d
print a
