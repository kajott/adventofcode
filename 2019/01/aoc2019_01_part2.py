def f(x):x=int(x)/3-2;return(x>0)and f(x)+x
print sum(map(f,open("input.txt")))
