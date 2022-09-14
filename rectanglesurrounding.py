import sys
n = -1

while(n != 0):
    n = int(input())

    points = [["*"]*500]*500
    total = 0
    if(n == 0):
        break
    else:
        low = 501
        high = -1
        for i in range(n):
            nums = input().split()
            pointa1 = int(nums[0])
            pointa2 = int(nums[1])
            pointb1 = int(nums[2])
            pointb2 = int(nums[3])
            for num in nums:
                if(int(num) > high):
                    high = int(num)
                if(int(num) < low):
                    low = int(num)
            for x in range(pointa1,pointb1):
                for y in range(pointa2,pointb2):
                    points[x][y] = 'x'
        for z in range(low, high):
            for w in range(low,high):
                if(points[z][w] == 'x'):
                    total += 1
        print(total)
            
            
            
            
            
