E,D=enumerate,(-1,0,1)
M={1j*x+y:c for y,l in E(open("input.txt"))for x,c in E(l)}
print(sum([M.get(p+(1j*u+v)*d,"")for d in(0,1,2,3)]==[*"XMAS"]for p in M for u in D for v in D))
