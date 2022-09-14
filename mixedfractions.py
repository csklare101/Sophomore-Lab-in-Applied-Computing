inp = -1

while(inp != [0,0]):
    inpu = input().split()
    i1 = int(inpu[0])
    i2 = int(inpu[1])
    inp = [i1,i2]

    if(inp == [0,0]):
        break
    else:
        if(inp[0] % inp[1] == 0):
            print(str(inp[0]//inp[1]) + " 0 / " + str(inp[1]))
        else:
            print(str(inp[0]//inp[1]) + " " + str(inp[0] % inp[1]) + " / " + str(inp[1]))
            
