import sys
k = int(sys.stdin.readline())
passes = 1

comp = int(sys.stdin.readline())
for i in range(k-1):
    newnum = int(sys.stdin.readline())
    if(comp > newnum):
        passes += 1
    comp = newnum
print(passes)
