#lostlineup
#jimmy counts as 1 person
#(ie if there is 3 people between you and jimmy, you are the 5th person in line)
#input first line is how many people in line
#second line is how many people are between you and jimmy

#ie sample input 2 on kattis says that there is 4 people in line
#first (not jimmy) person has one person between him an jimmy (3rd in line)
#second person has two people between him and jimmy (4th in line)
#third person has 0 people in front of him (2nd in line)

#output will always start at 1


#can make all spaces 1s to start then replace with "person number"
import sys
size = (int)(sys.stdin.readline())

line = [1] * size
places = sys.stdin.readline().split();

for i in range(len(places)):
    places[i] = int(places[i])

  
j = 2;
for x in range(len(places)):
    line[places[x]+1] = j;
    j += 1
linestr = ' '.join(str(n) for n in line)
print(linestr)
    
