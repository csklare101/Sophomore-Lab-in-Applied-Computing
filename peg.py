import sys
board = []
count = 0

for x in range(7):
    board.append(list(sys.stdin.readline()[:-1]))

for i in range(7):
    for j in range(7):
        if(board[i][j] == 'o'):
            if(board[i][max(j-1,0)] == 'o' and board[i][max(j-2,0)] == '.'):
                count+=1
            if(board[i][min(j+1,7-1)] == 'o' and board[i][min(j+2,7-1)] == '.'):
                count+=1
            if(board[max(i-1,0)][j] == 'o'and board[max(i-2,0)][j] == '.'):
                count+=1
            if(board[min(i+1,7-1)][j] == 'o' and board[min(i+2,7-1)][j] == '.'):
                count+=1

print(count)
