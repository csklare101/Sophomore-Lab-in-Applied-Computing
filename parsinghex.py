import sys
hexdig = ["X","x","0","1","2","3","4","5","6","7","8","9","a","b","c","d","e","f","A","B","C","D","E","F"]
inp = "test"

while(inp != ""):
    inp = sys.stdin.readline()
    if(inp == ""):
        break
    else:
        start = -1
        end = -1
        for i in range(len(inp)):
            if(inp[i] == "0" and (inp[i+1] == "X" or inp[i+1] == "x")):
                start = i
            if(start != -1 and (inp[i] not in hexdig and (inp[i] != 'X' or inp[i] != 'x'))):
                end = i
                num = inp[start:end]
                print(inp[start:end],str(int(num,0)))
                start = -1
                end = -1
                
    
