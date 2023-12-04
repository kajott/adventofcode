S=str.split;print(sum(1<<len(w&h)>>1 for w,h in(({*S(x)}for x in S(S(l,':')[1],'|'))for l in open("input.txt"))))
