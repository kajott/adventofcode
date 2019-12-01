def f(x):x=x/3-2;return max(x,0)and f(x)+x
print sum(map(f,map(int,open("input.txt"))))
