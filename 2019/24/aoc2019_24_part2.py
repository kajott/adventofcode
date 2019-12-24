E,_=enumerate,range
R,A,S=_(5),[],{12}
for p in _(25):x,y=p%5,p/5;A+=[(p!=12)and(x<1and[-14-p,1]or x>3and[-12-p,-1]or(x==1)*(y==2)and[-1]+_(25-p,50-p,5)or(x==3)*(y==2)and[1]+_(29-p,50-p,5)or[-1,1])+(y<1and[-18-p,5]or y>3and[-8-p,-5]or(y==1)*(x==2)and[-5]+_(25-p,30-p)or(y==3)*(x==2)and[5]+_(45-p,50-p)or[-5,5])or[]]
for y,l in E(open("input.txt")):S|={x+y*5for x,c in E(l)if'#'==c}
for i in _(200):
 O=S;S=set()
 for j in _((min(O)/25-1)*25,(max(O)/25+2)*25):
  n=sum((j+k)in O for k in A[j%25])
  if(n==1if j in O else n in(1,2)):S|={j}
print len(S)
