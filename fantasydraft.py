#first line of input is number of team owners, then size of each team 
#after that is prefference list for each owner
#after that is number of players then their names in generic ranked order

#SI1 has no owner preference list, so they take from the top of the generic list
#SI2 has team switching from preferd list to generic

#keep track of players who have been selected
#use set or dictonary since a list will take too long

#make sure you have an iterator for preference list and generic list to tell where you are
#don't go to begining of list each time
import sys
firstinp = sys.stdin.readline().split()
n = int(firstinp[0])
k = int(firstinp[0])
owners = {}
finallist = {}
placeint= 0
listint = 0
picked = False

for i in range(n):
    choices = sys.stdin.readline().split()
    choices.pop(0);
    owners[i] = choices
    finallist[i] = [] * k

playernum = int(sys.stdin.readline())
players = [None] * playernum
for x in range(playernum):
    players[x] = sys.stdin.readline()[:-1]

while(picked == False):
    if(owners[placeint][listint] in players):
        finallist[placeint].append(owners[placeint][listint])
        players.remove(owners[placeint][listint])
        placeint += 1
    else:
        finallist[placeint].append(players[listint])
        placeint+=1
    listint += 1
    if(placeint == n):
        if(len(finallist[placeint])) == k:
           picked = True
        else:
            placeint = 0

for z in finallist:
        print(z)
        

