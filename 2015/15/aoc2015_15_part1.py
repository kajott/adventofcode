import re
R=[map(int,re.findall('-?\d+',l))for l in open("input.txt")]
def I(k):
 l=len(k);s=100-sum(k);a,b,c,d=(max(0,sum(r[i]*n for r,n in zip(R,k+[s])))for i in(0,1,2,3))
 return a*b*c*d if l>len(R)-2else max(I(k+[i])for i in range(s+1))
print I([])
