import re
I,B,M=int,bool,re.match
p,v={},0
for l in map(str.split,open("input.txt"))+[[]]:
 if l:p.update({k[:3]:k[4:]for k in l})
 else:b,i,x,s,h,e,p=(p.get(f,"0")for f in("byr iyr eyr hgt hcl ecl pid".split()));m=M('(\d+)([ci])',s);s,u=m.groups()if m else"00";v+=(1919<I(b)<2003)*(2009<I(i)<2021)*(2019<I(x)<2031)*(149<I(s)<194if u=="c"else 58<I(s)<76)*B(M("#[0-9a-f]{6}",h))*B(M("amb|blu|brn|gry|grn|hzl|oth",e))*B(M('\d{9}$',p));p={}
print v
