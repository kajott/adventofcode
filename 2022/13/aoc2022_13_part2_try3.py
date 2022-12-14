A=[0]+sorted([l.replace('10','X').translate(None,'[]')for l in open("input.txt")if l.strip()]+["2","6"])
print A.index("2")*A.index("6")
