I=open("input.txt").read()
print min(p for p in range(len(I))if len(set(I[p-14:p]))>13)
