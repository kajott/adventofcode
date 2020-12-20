M=[[c<'.'for c in l.strip()]for l in open("input.txt")]
def C(u,v=1):return sum(r[(u*y)%len(r)]for y,r in enumerate(M[::v]))
print C(1)*C(3)*C(5)*C(7)*C(1,2)
