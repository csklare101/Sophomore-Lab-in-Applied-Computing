import sys
cards = sys.stdin.readline().split()
orders = int(sys.stdin.readline())
finalNum = 0

for i in range(len(cards)):
    cards[i] = int(cards[i])

for z in range(1023+1):
    binz = bin(z)[2:]
    binz = ('0'*(10-len(binz))) + binz
    if(binz.count('1') == orders):
        num = 1
        for j in range(len(binz)):
            if binz[j] == 1 and cards[j] == 0:
                num = 0
                break
            if binz[j] == 1 and cards[j] != 0:
                num += cards[j]
        finalNum += num
print(finalNum)
        
