x=0
for i,c in enumerate(open("input.txt").read()):
 x+=81-2*ord(c)
 if x<0:break
print i+1
