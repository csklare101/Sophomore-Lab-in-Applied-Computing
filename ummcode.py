import sys, re

line = sys.stdin.readline()
words = line.split()
wordsline = ''
letters = []
finalword = ''

count1 = 0
for i in words:
    for j in range(0,len(i)):
        if i[j] != 'u' and i[j] != 'm':
            if not i[j].isalpha():
                newword = i[:j]
                words[count1] = newword
            else:
                words.remove(i)
                break
    count1 += 1

for w in words:
    wordsline += w


for x in range(0, len(wordsline),7):
    letters.append(wordsline[x:x+7])

count2 = 0
for let in letters:
    newlet = ''
    for k in range(0,len(let)):
        if let[k] == 'u':
            newlet += '1'
        else:
            newlet += '0'
    letters[count2] = chr(int(newlet,2))
    finalword += letters[count2]
    count2+= 1

print(finalword)
