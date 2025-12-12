import functools as F
M={(l:=r.replace(':','').split())[0]:l[1:]for r in open("input.txt")}
@F.cache
def D(p,h=0):h|=(p=='dac')+(p=='fft')*2;return sum(D(n,h)for n in M[p])if p!='out'else h>2
print(D('svr'))
