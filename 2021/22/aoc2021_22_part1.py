import re
R,G=range,set()
for l in open("input.txt"):
 a,b,c,d,e,f=map(int,re.findall('-?\d+',l))
 u={(x,y,z)for x in R(max(-50,a),min(50,b)+1)for y in R(max(-50,c),min(50,d)+1)for z in R(max(-50,e),min(50,f)+1)}
 if'f'<l[1]:G|=u
 else:G-=u
print len(G)
