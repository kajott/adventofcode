import functools as F
@F.cache
def D(n,i,r):return""if i<0 else max(D(n,i-1,r-1)+n[i],D(n,i-1,r))if r else max(n[:i+1])
print(sum(int(D(n:=l.strip(),len(n)-1,11))for l in open("input.txt")))
