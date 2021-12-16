#write a program to dislay those words which starts with character 's'
#or 'S'. Read content from sample.txt


file = open("sample.txt",'r')
content = file.read()
splitted = content.split()
wordsList = []
for each in splitted:
    # if each[0]=='s' or each[0]=='S':
    if each[0].upper()=="S":
        wordsList.append(each)
    
print(wordsList)