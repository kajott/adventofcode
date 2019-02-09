_=isinstance
import json
S=lambda x:(_(x,list)and sum(map(S,x)))or(_(x,dict)and(0if"red"in x.values()else sum(map(S,x.values()))))or(_(x,int)and x)
print S(json.load(open("input.txt")))
