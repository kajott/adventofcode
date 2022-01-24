# This is actually *not* a "non-golf" version; it's just a commented
# and slightly more flexible version of the golf code.

from heapq import*

# index definitions of the state tuple
Slots   =4              # number of slots; 2 = part 1, 4 = part 2
iCorrect=0              # the number of correctly placed objects in each room
iForeign=iCorrect+4     # the number of foreign objects in each room
iRoom   =iForeign+4     # the foreign objects in each room, bottom-first, row-major, unoccupied slots end with -1
iPark   =iRoom+Slots*4  # the seven parking slots; -1 = unoccupied, 0..3 = A..D
iEnd    =iPark+7

# magic constants:
# P = parking spot X positions
# R = room X positions
# M = cost multipliers
P,R,M,E,T,L=[0,1,3,5,7,9,10],[2,4,6,8],[1,10,100,1000],range,tuple,list

# import initial state
s=[int(c,16)-10for c in open("input.txt").read()if'@'<c]
s=[0]*4+[Slots]*4+s[4:]+s[:4]+[-1]*7
if Slots==4:s[iRoom+4:iRoom+4]=[3,1,0,2,3,2,1,0]

# recognize pre-set correct slots; remove them from the "foreign" list
for i in E(4):
 while s[iRoom+i]==i:s[iCorrect+i]+=1;s[iForeign+i]-=1;s[iRoom+i:iRoom+i+Slots*4:4]=s[iRoom+i+4:iRoom+i+Slots*4:4]+[-1]

print "initial state:", s
assert len(s)==iEnd

# helper function to check whether a path on the corridor is free
def F(a,b):
 a,b=sorted((a,b))
 return 1-any(s[iPark+i]>=0for i in E(7)if a<P[i]<b)

# Dijkstra algorithm:
# O = open states [ (cost, state tuple), ... ]
# C = cost cache  { state tuple: cost, ... }
# m = list of possible moves with their cost (O format)
O=[(0,T(s))];C={T(s):0}
while O:
 # get least-cost state, check for optimality and winning state
 c,s=heappop(O);m=[]
 if c>C.get(s,1e9):continue
 if min(s[iCorrect:iCorrect+4])==Slots:break

 # generate moves for parked objects
 for i in E(7):
  r=s[i+iPark]
  # checks:
  # - there must be an object in the spot
  # - the object's target room must be free
  # - the path to the room must be free
  if(r>=0)*(s[iForeign+r]<1)*F(P[i],R[r]):
   d=L(s);d[i+iPark]=-1;d[r+iCorrect]+=1
   m+=[(c+M[r]*(abs(P[i]-R[r])+Slots-s[r+iCorrect]),T(d))]

 # generate moves for topmost foreign objects in rooms
 for i in E(4):
  if s[iForeign+i]:  # only do all that if there's a foreign object in the room at all
   k=iRoom+i+s[iForeign+i]*4-4  # index of the topmost foreign object in the state vector
   r=s[k]  # topmost foreign object type
   u=Slots-s[iCorrect+i]-s[iForeign+i]+1  # number of slots to move up into the hallway
   # can we move right into our target room?
   if(s[iForeign+r]<1)*F(R[i],R[r]):
    d=L(s);d[k]=-1;d[iForeign+i]-=1;d[iCorrect+r]+=1
    m+=[(c+M[r]*(abs(R[i]-R[r])+u+Slots-s[iCorrect+r]),T(d))]
   # else move into one of the free parking spots
   a=b=P.index(R[i]+1)
   while(s[iPark+a-1]<0)*a:a-=1
   while b<7and s[iPark+b]<0:b+=1
   for j in E(a,b):
    d=L(s);d[k]=-1;d[iForeign+i]-=1;d[iPark+j]=r
    m+=[(c+M[r]*(abs(R[i]-P[j])+u),T(d))]

 # add generated moves to list if they're interesting
 for c,s in m:
  if c<C.get(s,1e9):C[s]=c;heappush(O,(c,s))
print c
