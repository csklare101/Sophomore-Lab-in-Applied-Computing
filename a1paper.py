import math
smallan = int(input())
papers = [0,0]+list(map(int,input().split()))
req = 2
l = 0
found = False
p1 = 2**(-5/4)
p2 = 2**(-3/4)
t = p2

for i in range(2,smallan+1):
    pap = papers[i]
    if(pap >= req):
        found = True
        break
    t += (req-pap)*p1
    req = (req-pap)*2
    p2 /= math.sqrt(2)
    p1 /= math.sqrt(2)
        
        

if(found):
    print(t)
else:
    print("impossible")
        
        
