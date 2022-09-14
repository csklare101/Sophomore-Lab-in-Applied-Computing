import sys
boardSize = int(sys.stdin.readline())
rows = []
cols = []
corr = 1
for i in range(boardSize):
    rows.append(sys.stdin.readline()[:-1])

for j in range(boardSize):
    word = ""
    for x in range(boardSize):
       word += rows[x][j]
    cols.append(word)

for r in rows:
    rws = r.count('W')
    rbs = r.count('B')

    if(rws != rbs):
        corr = 0
        break
    counter = 0
    for z in range(len(r)):
        char = r[z]
        if(z > 0):
            if char == r[z-1]:
                counter += 1
            if counter == 3:
                break
    if counter == 3:
        corr = 0
        break

for c in cols:
    cws = c.count('W')
    cbs = c.count('B')

    if(cws != cbs):
        corr = 0
        break
    counter2 = 0
    for m in range(len(c)):
        char = c[m]
        if(m > 0):
            if char == c[m-1]:
                counter2 += 1
            if counter2 == 3:
                break
    if counter2 == 3:
        corr = 0
        break
print(corr)
