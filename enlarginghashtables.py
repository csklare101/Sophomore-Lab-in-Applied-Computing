import math
n=-1
while(n != 0):
    n = int(input())
    nprime = True
    ns = math.ceil(math.sqrt(n))

    if(n == 0):
        break
    else:
        for i in range(2,ns+1):
            if (n % i == 0):
                nprime = False
                break
        n2 = n*2
        final = 0
        n2s = math.ceil(math.sqrt(n2))

        for j in range(1,n2s+1):
            if (n2 % j == 0):
                final = j+n2
                break
        if(nprime):
            print(final)
        else:
            print(str(final) + " (" + str(n) + " is not prime)")
