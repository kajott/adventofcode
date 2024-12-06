import re;N=[[*map(int,re.findall(r'\d+',l))]for l in open("input.txt")]
print(sum(u[len(u)//2]*all((i:=u.index)(r[0])<i(r[1])for r in N if(len(r)==2)*all(x in u for x in r))for u in N if len(u)>2))
