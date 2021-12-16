# write a program to read from sample.txt file and write
# to sample_reverse.txt file with all words reversed from sample.txt

file = open("sample.txt", 'r')
content = file.read()
file.close()
splitted = content.split()
reverseList = []
i = 0
lengthOfList = len(splitted)
while i < lengthOfList:
    splittedIndex = lengthOfList-1-i
    splittedItem = splitted[splittedIndex]
    reverseList.append(splittedItem)
    i += 1
reverseFile = open("sample_reverse.txt", 'w')
for each in reverseList:
    reverseFile.write(each + " ")
reverseFile.close()
