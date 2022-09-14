import sys
numbs = sys.stdin.readline().split()
numbs[0] = int(numbs[0])
numbs[1] = int(numbs[1])
numbs[2] = int(numbs[2])
final = 0

if(numbs[0] - numbs[1] > numbs[1]):
    final = numbs[0] - numbs[1]
else:
    final = numbs[1]

if(numbs[0] - numbs[2] > numbs[2]):
    final = final * (numbs[0] - numbs[2]) * 4
else:
    final = final * numbs[2] * 4

print(final)
