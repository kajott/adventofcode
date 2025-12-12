M,D={(l:=r.replace(':','').split())[0]:l[1:]for r in open("input.txt")},lambda p:sum(map(D,M[p]))if p!='out'else 1;print(D('you'))
