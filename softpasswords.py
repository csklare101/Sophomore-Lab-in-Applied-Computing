import sys
goodPass = False

while True:
    s1 = sys.stdin.readline()
    if s1 == '\n':
        break
    else:
        s = s1[:-1]
        p1 = sys.stdin.readline()
        if p1 == '\n':
            break
        p = p1[:-1]
 
#case 1
if s == p:
    goodPass = True
    print('Yes')

#case 2
elif s[0].isdigit() and s[1:] == p:
    goodPass = True
    print('Yes')

#case3
elif s[-1].isdigit() and s[:-1] == p:
    goodPass = True
    print('Yes')

#case 4
else:
    for i in range(0, len(s)):
        if s[i].isalpha() and s[i].isupper():
            if p[i].islower():
                goodPass = True
            else:
                goodPass = False
                break
        elif s[i].isalpha() and s[i].islower():
            if p[i].isupper():
                goodPass = True
            else:
                goodPass = False
                break

    if len(s) != len(p):
        goodPass = False

    if goodPass == False:
        print('No')
    if goodPass == True:
        print('Yes')
