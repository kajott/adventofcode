import re
w,c={d:(o and o[0],a and a[:-1],b)for a,o,b,d in re.findall('([a-z0-9]+ )?([A-Z]+ )?([a-z0-9]+) -> ([a-z]+)',open("input.txt").read())},{}
def G(n):
 if n.isdigit():return int(n)
 if n in c:return c[n]
 o,a,b=w[n]
 if not o:v=G(b)
 if'A'==o:v=G(a)&G(b)
 if'O'==o:v=G(a)|G(b)
 if'R'==o:v=G(a)>>G(b)
 if'L'==o:v=(G(a)<<G(b))&65535
 if'N'==o:v=G(b)^65535
 c[n]=v;return v
z=G("a");print z
c={"b":z};print G("a")
