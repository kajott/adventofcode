import re
g=filter(None,(map(int,re.findall('\d+',l))for l in open("input.txt")))
w=g[-1][0]
x,y=min((z[3],z[:2])for z in g)[1]
b=min(z[0]for z in g if z[3]>99)
print y+x-2*b+6*w-3
