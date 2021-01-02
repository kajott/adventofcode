E={}
for t in open("input.txt").read().strip().split("\n\n"):
 t=t.split('\n');i=int(t[0][5:-1]);t=[[c<'.'for c in r]for r in t[1:]];e=[t[0],t[-1],[r[0]for r in t],[r[-1]for r in t]]
 for e in map(tuple,e+[r[::-1]for r in e]):E[e]=E.get(e,set())|{i}
f,m=[list(v)[0]for v in E.values()if len(v)<2],1
for t in set(f):
 if f.count(t)==4:m*=t
print m
