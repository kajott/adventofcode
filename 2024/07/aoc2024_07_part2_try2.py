def E(r,v,o):
 if o and v<=r:b,*x=o;return E(r,v+b,x)or E(r,v*b,x)or E(r,int(str(v)+str(b)),x)
 return(v==r)*r
print(sum(E((e:=[*map(int,l.replace(':','').split())])[0],e[1],e[2:])for l in open("input.txt")))
