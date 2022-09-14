import sys
k = int(sys.stdin.readline())

for i in range(k):
    numbers = sys.stdin.readline().split()
    n = int(numbers[0])
    a = int(numbers[1])
    b = int(numbers[2])
    c = int(numbers[3])
    d = int(numbers[4])
    x0 = int(numbers[5])
    y0 = int(numbers[6])
    m = int(numbers[7])

    case = 1
    xs = []
    ys = []
    x = x0
    y = y0
    j = 1
    for j in range(n-1):
       x = (a*x+b) % m
       xs.append(x)
       y = (c*y+d) % m
       ys.append(y)

    n = n-1
    for z1 in range(n-2):
        for z2 in range(z1 + 1, n-1):
            for z3 in range(z2 + 1, n):
                xnum = xs[z1]+xs[z2]+xs[z3]
                ynum = ys[z1]+ys[z2]+ys[z3]
                if(xnum % 3 == 0 and ynum % 3 == 0):
                    case+=1
                
    strin = "Case #" + str(i+1) + ": " + str(case)            
    print(strin)
    
