A=[0]+sorted([map(int,filter(None,l.replace(']',',0').replace('[','').split(',')))for l in open("input.txt")if l.strip()]+[[2],[6]])
print A.index([2])*A.index([6])
