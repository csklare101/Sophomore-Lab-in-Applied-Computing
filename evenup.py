n = int(input())
nums = input().split()

res = []
for i in range(n):
    if(i > 0 and len(res) > 0):
        test = int(nums[i]) + res[len(res)-1]
        if(test % 2 == 0):
            res.pop()
        else:
            res.append(int(nums[i]))
    else:
        res.append(int(nums[i]))
print(len(res))
