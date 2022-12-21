root=0
while root<1:
 for l in open("input.txt"):
  try:exec(l.replace(':','='))
  except:pass
print root
