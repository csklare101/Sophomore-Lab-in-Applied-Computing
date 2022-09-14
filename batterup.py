import sys
n = int(sys.stdin.readline())
nums = sys.stdin.readline().split()
finnums = 0
count = 0

for i in range(n):
    nums[i] = int(nums[i])
    if nums[i] > -1:
        count+= 1
        finnums += nums[i]

print(finnums/count)
