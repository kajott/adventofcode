E=enumerate
M={1j*x+y:c for y,l in E(open("input.txt"))for x,c in E(l)}
C=lambda p,d:{M.get(p-d),M.get(p+d)}=={*"MS"}
print(sum((M[p]=="A")*C(p,1j-1)*C(p,1j+1)for p in M))
