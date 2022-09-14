nums = input().split()
w = int(nums[0])
p = int(nums[1])

l = []
l.append(0)
final = []
ix = input().split()
for i in range(p):
    l.append(int(ix[i]))
l.append(w)


for x in range(0,len(l)-1):
    for y in range(len(l)-1,0,-1):
        if(l[x] != l[y] and not(l[x] > l[y])):
            if(l[y]-l[x] not in final):
                final.append(l[y]-l[x])

final.sort()
print(*final)
