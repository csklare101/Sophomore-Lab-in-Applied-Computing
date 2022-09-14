import sys, math
r = -1
m = -1
c = -1
while(r != 0 and m != 0 and c != 0):
    numbs = sys.stdin.readline().split()
    r = float(numbs[0])
    m = int(numbs[1])
    c = int(numbs[2])

    if(r == 0 and m == 0 and c == 0):
        break
    else:
        true = math.pi*(r**2)
        est = c/m*(2*r)**2
        
        print(str(true) + " " + str(est))
