R,S={},str.split
for l in open("input.txt"):
 if'`'<l[0]<'{':
  n,r=l.split('{');e=R[n]=[]
  for r in S(S(r,'}')[0],','):
   if':'in r:r,t=S(r,':');g='>'in r;v,c=S(r,"<>"[g]);e+=[(v,g,int(c),t)]
   else:e+=[('x',1,0,r)]
def C(r,i,*d):
 if'B'>r:a,b,c,d,e,f,g,h=d;return(b-a)*(d-c)*(f-e)*(h-g)
 if'Z'>r:return 0
 v,g,c,t=R[r][i];v="xmas".index(v)*2
 if c<1:return C(t,0,*d)
 c+=g;a,b=d[v:v+2];x=[*d];x[v+1]=c;y=[*d];y[v]=c
 if g:x,y=y,x
 return C(r,i+1,*d)if(c<=a)+(c>=b)else C(t,0,*x)+C(r,i+1,*y)
print(C("in",0,*[1,4001]*4))
