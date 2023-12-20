S,F,A,R,M=str.strip,{},1,{},{}
for l in open("input.txt"):
 n,o=l.split('->');n=S(n);t=n[0];n=n['a'>t:3];o=[*map(S,o.split(','))];M[n]=o;F[n]='&'>t
 for d in o:R[d]=R.get(d,[])+[n]
for n in R[R['rx'][0]]:
 n=R[n][0];f,p=[z for z in R[n]if[n]==M[z]],0
 while f:p=2*p+(n in M[f[0]]);f=[z for z in R[f[0]]if F[z]]
 A*=p
print(A)
