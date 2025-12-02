import re;print(sum(n*(len(s:=str(n))>(s+s).find(s,1))for a,b in re.findall(r'(\d+)-(\d+)',open("input.txt").read())for n in range(int(a),int(b)+1)))
