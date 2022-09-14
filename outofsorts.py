import sys
def binarySearch(l, t, lo, hi):
    if(hi >= lo):
        mid = (lo+hi) // 2
        if(l[mid] == t):
            return True
        elif(l[mid] > t):
            return binarySearch(l, t, lo, mid-1)
        else:
            return binarySearch(l, t, mid+1, hi)
    else:
        return False
        

start = sys.stdin.readline().split()
n = int(start[0])
m = int(start[1])
a = int(start[2])
c = int(start[3])
x = int(start[4])
numbers = []
count = 0
for i in range(n):
    numbers.append(((a*x) + c) % m)
    x = numbers[i]

for num in numbers:
    if(binarySearch(numbers, num, 0, len(numbers)-1)):
        count += 1
print(count)

