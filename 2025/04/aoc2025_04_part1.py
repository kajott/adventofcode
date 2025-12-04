E=enumerate;M={x+1j*y for y,l in E(open("input.txt"))for x,c in E(l.strip())if'.'<c}
print(sum(4>sum((p+d)in M for d in(-1j-1,-1j,1-1j,-1,+1,1j-1,1j,1j+1))for p in M))
