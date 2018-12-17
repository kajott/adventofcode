execfile("aoc2018_17.py");f=open("vis.ppm","wb");f.write("P6\n%d %d\n255\n"%(w+2,h+1)+''.join(''.join(("\0\0\0","\xff\xff\xff","\0\0\xff","\x80\xc0\xff")[c]for c in r)for r in m))
