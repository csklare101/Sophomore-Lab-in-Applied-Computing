import sys
nums = sys.stdin.readline().split()
ln = int(nums[0])
wd = int(nums[1])
first = int(nums[2])
second = int(nums[3])
third = int(nums[4])
range1 = int(nums[5])
range2 = int(nums[6])
volMax = ln//2
finalNum = 0
vols = []

for i in range(1,volMax):
    vols.append(i*(ln-(2*i))*(wd-(2*i)))

vs = []
v0 = 0
v1 = 0
v2 = 0
vs.append(v0)
vs.append(v1)
vs.append(v2)
for z in range(3):
    for x in range(len(vols)):
        if vols[x] > vs[z] and vols[x] not in vs:
            vs[z] = vols[x]
v0 = vs[0]
v1 = vs[1]
v2 = vs[2]

k = range1 // v0
l = range1 % v0
if l < first:
    firstX = k*v0+l+(first-l)
else:
    firstX = k*v0+l+(l-first)+v0


for j in range(firstX, range2, v0):
    num1 = j % v0
    num2 = j % v1
    num3 = j % v2
    if num1 == first and num2 == second and num3 == third:
        finalNum = j
        break
print(finalNum)
