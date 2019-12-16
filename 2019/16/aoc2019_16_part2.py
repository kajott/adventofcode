S=open("input.txt").read().strip()
S=(map(int,S)*10000)[int(S[:7]):][::-1]
for i in range(100):
 for j in range(1,len(S)):S[j]=(S[j]+S[j-1])%10
print''.join(map(str,S[-1:-9:-1]))
