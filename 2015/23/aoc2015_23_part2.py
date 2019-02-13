P=[l.replace(',',' ').split()for l in open("input.txt")]
i=0;r={'a':1,'b':0}
while 0<=i<len(P):
 o,a=P[i][:2];o=o[2];i+=1
 if'f'==o:r[a]/=2
 if'l'==o:r[a]*=3
 if'c'==o:r[a]+=1
 if'p'==o:i+=int(a)-1
 if(o=='e'and r[a]&1<1)or(o=='o'and r[a]==1):i+=int(P[i-1][2])-1
print r['b']
