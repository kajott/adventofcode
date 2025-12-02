import re;print(sum(n*bool(re.match(r'(\d+)\1$',str(n)))for a,b in re.findall(r'(\d+)-(\d+)',open("input.txt").read())for n in range(int(a),int(b)+1)))
