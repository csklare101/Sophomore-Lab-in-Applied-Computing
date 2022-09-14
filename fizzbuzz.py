import sys
nums = sys.stdin.readline().split()
x = int(nums[0])
y = int(nums[1])
n = int(nums[2])

for i in range(1,n+1):
    if(i % x == 0 and i % y == 0):
        print("FizzBuzz")
    if(i % x == 0 and i % y != 0):
        print("Fizz")
    if(i % x != 0 and i % y == 0):
        print("Buzz")
    if(i % x != 0 and i % y != 0):
        print(i)
