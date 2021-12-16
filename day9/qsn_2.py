#write a program to count the word "the" from sample.txt file

file = open("sample.txt","r")
content = file.read()
splitted = content.split()
count = 0
for each in splitted:
    if(each == "the" or each=="The"):
        count+=1

print("number of the words: ",count)