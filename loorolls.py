import sys
nums = sys.stdin.readline().split()
l = int(nums[0])
n = int(nums[1])
k = 1
while(l % n != 0):
    leftover = l % n
    n = n-leftover
    k+=1
print(k)
