import sys, math
n = int(sys.stdin.readline())

for i in range(n):
    w = int(sys.stdin.readline())
    wheels = sys.stdin.readline().split()
    greatest = 0
    for j in range(w):
        wheels[j] = int(wheels[j])
    FGCD = (wheels[0]*wheels[1])//math.gcd(wheels[0],wheels[1])
    LCM = (wheels[2]*FGCD)//math.gcd(wheels[2],FGCD)
    if w > 3:
        for x in range(3,w):
            LCM = (wheels[x]*LCM)//math.gcd(wheels[x],LCM)
    print(LCM)
        

    
    
