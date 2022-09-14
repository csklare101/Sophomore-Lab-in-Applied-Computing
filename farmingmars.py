import sys, math

inp = sys.stdin.readline()
n = int(inp[0])
m = int(inp[-2])

phs = []
ls = []
rs = []
majoritys = []
for i in range(0,n):
    phs.append(float(sys.stdin.readline()))

for x in range(0,m):
    inp2 = sys.stdin.readline()
    ls.append(int(inp2[0]))
    rs.append(int(inp2[-2]))
    majoritys.append(math.floor((int(inp2[-2]) - int(inp2[0]) + 1) / 2))


for j in range(0,m):
    counts = []
    greater = False
    for z in range(ls[j]-1,rs[j]):
        counts.append(phs[ls[j]-1:rs[j]].count(phs[z]))
        if majoritys[j] < phs[ls[j]-1:rs[j]].count(phs[z]):
            greater = True
            break;
    if greater:
        print("usable")
    else:
        print("unusable")
