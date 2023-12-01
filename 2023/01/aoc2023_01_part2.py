E,F=enumerate,lambda l,f,a,m:a([(f(l,d)&m,str(i+1))for i,d in E("one two three four five six seven eight nine".split())]+[x for x in E(l)if x[1].isdigit()])[1]
print(sum(int(F(l,str.find,min,63)+F(l,str.rfind,max,-1))for l in open("input.txt")))
