oper = [' + ' , ' - ', ' * ', ' // ']

vals = {}
for i in range(4):
    for j in range(4):
        for x in range(4):
            st = "4" + oper[i] + "4" + oper[j] + "4" + oper[x] + "4"
            val = eval(st)
            nst = st.replace('//', '/')
            vals[val] = nst + " = " + str(val)

inp = int(input())
for z in range(inp):
    num = int(input())
    if num not in vals:
        print("no solution")
    else:
        print(vals[num])
