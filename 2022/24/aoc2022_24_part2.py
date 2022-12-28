E=enumerate
W,B={(0,-2)},set()
for y,l in E(open("input.txt"),-1):
 for x,c in E(l,-1):W|=c=='#'and{(x,y)}or W;B|={'<':{(x,y,-1,0)},'>':{(x,y,1,0)},'^':{(x,y,0,-1)},'v':{(x,y,0,1)}}.get(c,B)
X=max(x for x,y in W);Y=max(y for x,y in W);W|={(X-1,Y+1)}
a,b=(0,-1),(X-1,Y);q={a};G=[b,a,b];t=0
while G:
 t+=1;q={(x+u,y+v)for u,v in((1,0),(0,1),(-1,0),(0,-1),(0,0))for x,y in q}-{((x+t*u)%X,(y+t*v)%Y)for x,y,u,v in B}-W
 if G[0]in q:q={G.pop(0)}
print t
