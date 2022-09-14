import sys, math
numOrders = int(sys.stdin.readline())
orderDic = {}
cooks = 1

for i in range(numOrders):
    order = sys.stdin.readline().split()
    order[0] = int(order[0])
    order[1] = int(order[1])
    p1 = order[0]
    p2 = order[1]
    

    for j in [p2, p2 -p1, p2-(p1*2)]:
        if j not in orderDic:
            orderDic[j] = 1
        else:
            orderDic[j] += 1

for d in orderDic:
    if orderDic[d] > cooks:
        cooks = orderDic[d]

print((cooks//2) + (cooks % 2))
