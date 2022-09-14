import sys
n = int(sys.stdin.readline())
size = n
numbers = sys.stdin.readline().split()

for i in range(len(numbers)):
    numbers[i] = (i+1,numbers[i])
    
while(size != 1):
    if(size == n):        
        number = int(numbers[0][1])
        pos = (number-1) % size
        del(numbers[pos])
        size -= 1
    else:
        pos = abs(pos-size)
        if(pos != 0):
            number = int(numbers[pos][1])
            pos = abs(((number-1) % size) - pos)
        else:
            number = int(numbers[pos][1])
            pos = (number-1) % size
        del(numbers[pos])
        size -= 1
print(numbers[pos][0])
