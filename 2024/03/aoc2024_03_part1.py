import re;print(sum(int(a)*int(b)for a,b in re.findall(r'mul\((\d+),(\d+)\)',open("input.txt").read())))
