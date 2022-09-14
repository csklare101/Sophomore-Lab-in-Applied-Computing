import sys, math
n = int(sys.stdin.readline())
if(n == 1):
    print("Either")
else:
    n2 = math.floor(n/2)
    n3 = math.ceil(n/2)
    if(n2 == n3):
        if(n2 % 2 == 1):
            print("Odd")
        else:
            print("Even")
    else:
        print("Either");
