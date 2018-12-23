import re
print sum(len(m)-2for m in re.findall('<[^>]*>',re.sub('!.','',open("input.txt").read().strip())))
