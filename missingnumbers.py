import sys
n = int(sys.stdin.readline())
numbers = []
corr = []
good = True

for i in range(n):
    number = int(sys.stdin.readline())
    if i > 0:
        num = numbers[i-1] + 1
    if i == 0 and number != 1:
        good = False
        for z in range(1, number):
            corr.append(z)
    if i > 0 and number > num:
        good = False
        for b in range(num, number):
            corr.append(b)
    numbers.append(number)
if good:
    print("good job")
else:
    for j in range(len(corr)):
        print(corr[j])
