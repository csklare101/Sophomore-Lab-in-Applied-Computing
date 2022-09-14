import sys
nandm = sys.stdin.readline().split()
n = int(nandm[0])
m = int(nandm[1])

vill = []

for x in range(n):
    vill.append(list(sys.stdin.readline()[:-1]))

for i in range(n):
    strin = ""
    for j in range(m):
        if(vill[i][j] == '.'):
            if(vill[i][max(j-1,0)] != 'E'):
               if(vill[max(i-1,0)][j] != 'E'):
                  if(vill[i][min(j+1,m-1)] != 'E'):
                      if(vill[min(i+1,n-1)][j] != 'E'):
                          vill[i][j] = 'E'
        strin+= vill[i][j]
    print(strin)
        
