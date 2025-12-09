N=[[*map(int,l.split(','))]for l in open("input.txt")]
print(max((abs(x-u)+1)*(abs(y-v)+1)for i,(x,y)in enumerate(N)for u,v in N[i:]))
