E=enumerate;M={1j*x-y:c for y,l in E(open("input.txt"))for x,c in E(l.strip())}
n=p=[p for p in M if'Z'<M[p]][0];v,d={p},1
while n in M:
 if'.'>M[n]:d*=1j
 else:p=n;v|={p}
 n=p+d
print(len(v))
