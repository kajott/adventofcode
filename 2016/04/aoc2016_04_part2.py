import re
for r,s,c in re.findall('([a-z-]+)(\d+)\[(\w+)',open("input.txt").read()):
 if"obj"in''.join(chr((ord(x)+7+int(s))%26+97)for x in r):print s
