import re;P=[*map(int,re.findall(r'\d+',open("input.txt").read()))]
C=lambda a,i:min([C(x,i-1)for x in range(max(1,8*a),8*a+8)if(x^(x>>(~x&7)))&7==P[i-1]],default=1e99)if i>3 else a
print(C(0,len(P)))
