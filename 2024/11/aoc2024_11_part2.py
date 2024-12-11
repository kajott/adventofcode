import functools as F
@F.cache
def S(n,t):l=len(n);t-=1;return 1 if t<0 else S('1',t)if n<'1'else S(str(int(n)*2024),t)if l&1 else S(n[:l//2],t)+S(str(int(n[l//2:],10)),t)
print(sum(S(n,75)for n in open("input.txt").read().split()))
