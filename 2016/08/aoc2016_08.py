import re
s=[50*[0]for y in range(6)]
def T():global s;s=map(list,zip(*s))
def R():s[a]=s[a][-b:]+s[a][:-b]
for l in open("input.txt"):
 a,b=map(int,re.findall('\d+',l))
 if'r'==l[7]:R()
 elif'c'==l[7]:T();R();T()
 else:
  for y in range(b):s[y][:a]=[1]*a
for r in s:print''.join(" #"[c]for c in r)
print sum(map(sum,s))
