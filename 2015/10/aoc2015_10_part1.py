import re
s="1321131112"
for i in range(40):s=re.sub(r'(\d)\1*',lambda m:str(len(m.group(0)))+m.group(1),s)
print len(s)
