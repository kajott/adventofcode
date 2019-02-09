import re
def N(p):
 n,f=[ord(c)-97for c in p],1
 while f+all((n[i]+1!=n[i+1])+(n[i]+2!=n[i+2])for i in range(6))+bool(re.search('[iol]',p))+(len(set(re.findall(r'(\w)\1',p)))<2):
  for i in range(7,-1,-1):
   n[i]=(n[i]+1)%26
   if n[i]:break
  p,f=''.join(chr(c+97)for c in n),0
 return p
print N(N("hxbxwxba"))
