import sys
a = 0
b = 0
for line in sys.stdin:
    for i in range(0, len(line[:-1]), 2):
        if line[i] == 'A':
            a += int(line[i+1])
        else:
            b += int(line[i+1])

    if(a > b):
        print('A')
    else:
        print('B')
