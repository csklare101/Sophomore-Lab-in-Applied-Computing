
#pattern keeps repeating
#first line of input is length of terry's sleep pattern in seconds
#other 2 numbers are p and d
#second line tells if Terry is awake or sleeping

#output is number of seconds terry is tired during a time period

#SI2 has the pattern at 5, p at 3 (look at 3 seconds), and d is 2
#number of z's needs to be greater than to 2
#because pattern repeats, terry is tired for 4 seconds because he gets more than 2 z's at 1 after the repeat

## SAMPLE SOLUTION DOES NOT WORK, TIME LIMIT EXCEDES
##import sys
##
##while True:
##    npd = sys.stdin.readline()
##    if npd== '':
##        break
##    npd = npd.split()
##    n = int(npd[0])
##    p = int(npd[1])
##    d = int(npd[2])
##    pat = sys.stdin.readline()[:-1]
##
##    tired = 0 
##    for i in range(n): #looks for interval of z's
##        zs = 0
##        for j in range(i-p+1, i+1):
##            if pat[j] == 'Z':
##                zs+=1
##        if zs < d:
##            tired += 1
##    print(tired)

#can reuse z's for each substring in order to limit ammount of checks
#can can look at first and last characters in new substring
import sys
npd = sys.stdin.readline().split()
n = int(npd[0])
p = int(npd[1])
d = int(npd[2])
tired = 0
zs = 0
pat = sys.stdin.readline()[:-1]

#4/12/20 old code
##if(n == 2):
##    while(zs <d):
##        zs += pat.count('Z')
##        tired += 1
##else:
##    i = 0
##    while(zs < d):
##        newstr = pat[i-p+1:i]
##        zs += newstr.count('Z')
##        tired += 1
##        i += 1
##print(tired)

#new code
for j in range(-p+1,1):
    if pat[j] == 'Z':
        zs += 1
if zs < d:
    tired += 1
s = -p+1
e = 1
for i in range(1,n):
    if pat[s] == 'Z':
        zs -= 1
    if pat[e] == 'Z':
        zs += 1
    if zs < d:
        tired +=1
    s += 1
    e += 1
print(tired)
        
    
