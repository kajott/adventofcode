E=lambda r,v,*o:E(r,v+o[0],*o[1:])|E(r,v*o[0],*o[1:])if o else(r==v)*r
print(sum(E(*map(int,l.replace(':','').split()))for l in open("input.txt")))
