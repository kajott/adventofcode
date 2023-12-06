t,d=(int(''.join(l.split()[1:]))for l in open("input.txt"))
x=t/2;y=(x*x-d)**.5;print(int(x+y)-int(x-y))
