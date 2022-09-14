#given two lines of input, first line is number of numbers and devisor
#second line is the quotents that the devisor will devide from

#output is number of pairs that have the same answer from integer devision
#ie sample output 1 has pairs such as (4,5) (4,6) (4,7) (5,6) (5,7) (6,7), 6 pairs

#if divisor is 1 and all quoteints are different (SI2) then output will be 0

#number of pairs is n choose 2

#make a dictonary of the quotients that have the same key (answer)
#take elements in dictornary to do n choose 2
import sys
firstin = sys.stdin.readline().split()
size = (int)(firstin[0])
devisor = (int)(firstin[1])
pairs = 0;
numbers = sys.stdin.readline().split()
numbdict = {}

#older code
##for i in range(len(numbers)):
##    numbers[i] = (int)(numbers[i])
##
##for x in range(len(numbers)):
##    test = numbers[x] // devisor
##    for z in range(x+1, len(numbers)):
##        if(test == numbers[z] // devisor):          
##            if test not in numbdict:
##                numbdict[test] = 1
##            else:
##                numbdict[test] += 1
##
##for n in numbdict:
##    pairs += numbdict[n]

#new code
for i in numbers:
    test = int(i) // devisor
    if test in numbdict:
        numbdict[test] += 1
    else:
        numbdict[test] = 1
for j in numbdict:
    pairs += numbdict[j]*(numbdict[j]-1)//2
print(pairs)
