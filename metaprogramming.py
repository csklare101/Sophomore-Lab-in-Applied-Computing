import sys
dic = {}

inp = sys.stdin.readline().split()
while inp != []:
    if(inp[0] == 'define'):
        dic[inp[2]] = int(inp[1])
    if(inp[0] == 'eval'):
        if(inp[1] not in dic or inp[3] not in dic):
            print("undefined")
        else:
            if(inp[2] == '='):
                if(dic[inp[1]] == dic[inp[3]]):
                    print("true")
                else:
                    print("false")
            if(inp[2] == '<'):
                if(dic[inp[1]] < dic[inp[3]]):
                    print("true")
                else:
                    print("false")
            if(inp[2] == '>'):
                if(dic[inp[1]] > dic[inp[3]]):
                    print("true")
                else:
                    print("false")
        
    inp = sys.stdin.readline().split()            
