I=open("input.txt").read()
print min(p for p in range(len(I))if len(set(I[p-4:p]))>3)
