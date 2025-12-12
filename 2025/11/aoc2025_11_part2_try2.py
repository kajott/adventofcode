import functools as F
M={(l:=r.replace(':','').split())[0]:l[1:]for r in open("input.txt")}
@F.cache
def D(p,t):return sum(D(n,t)for n in M[p])if p!=t else 1
x,y,z,w='svr','dac','fft','out';M[w]=[]
print(D(x,y)*D(y,z)*D(z,w)+D(x,z)*D(z,y)*D(y,w))
