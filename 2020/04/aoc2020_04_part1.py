p,v,R={0},0,set("byr iyr eyr hgt hcl ecl pid".split())
for l in map(str.split,open("input.txt"))+[[]]:
 if l:p|={k[:3]for k in l}
 else:v+=p&R==R;p={0}
print v
