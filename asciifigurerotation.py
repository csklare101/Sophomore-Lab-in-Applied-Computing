n = -1
count = 0
while(n != 0):
    n = int(input())
    if(n == 0):
        break
    if(count > 0):
        print()
        
    asciir = []
    m = 0

    for i in range(n):
        inp = input()
        if(len(inp) > m):
            m = len(inp)
        asciir.append(inp)

    for j in range(len(asciir)):
        if(len(asciir[j]) != m):
            ad = m-len(asciir[j])
            asciir[j] += " "*ad


    for x in range(m):
        t = " "*m
        t = list(t)
        for y in range(n):
            
            ch = asciir[y][x]
            if(ch == "-"):
                ch = "|"
            elif(ch == "|"):
                ch = "-"
            t[n-y-1] = ch
        t = "".join(t)
        print(t)
        count+=1
    
