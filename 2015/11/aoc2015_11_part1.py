import re
p="hxbxwxba"
n=[ord(c)-97for c in p]
while all((n[i]+1!=n[i+1])+(n[i]+2!=n[i+2])for i in range(6))+bool(re.search('[iol]',p))+(len(set(re.findall(r'(\w)\1',p)))<2):
 for i in range(7,-1,-1):
  n[i]=(n[i]+1)%26
  if n[i]:break
 p=''.join(chr(c+97)for c in n)
print p
