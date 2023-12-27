E,N,F=enumerate,(1,-1,1j,-1j),{1}
for y,l in E(open("input.txt")):
 for x,c in E(l.strip()):
  if'#'!=c:F|={y*1j+x}
G=y*1j+x-1
J={1,G}|{p for p in F if sum(p+d in F for d in N)>2}
D={j:[]for j in J}
for j in J:
 t,q,v=0,{j},{j}
 while q:
  t+=1;v|=q;q={p+d for p in q for d in N if p+d in F}-v
  for p in q&J:D[j]+=[(p,t)]
  q-=J
M={1:1,G:0}|{j:2<<i for i,j in E(J-{1,G})}
B={M[a]:[(M[b],d)for b,d in D[a]]for a in D if a!=G}
with open("a.c","w")as F:
 W=F.write;W('#include <stdio.h>\nint S(long p,long v,int l){int t,m=0;switch(p){case 0:m=l;')
 for a in B:
  W(f'break;case {a}:')
  for b,d in B[a]:W(f'if(!(v&{b})){{t=S({b},v|{b},l+{d});if(t>m)m=t;}}')
 W('break;}return m;}int main(){printf("%d\\n",S(1,0,0));return 0;}')
import subprocess as S
S.run(["cc","a.c"])
S.run(["./a.out"])
