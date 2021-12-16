#write a program to read from sample.txt and count the numbers of
#words whose characters are less than 7

file = open("sample.txt",'r')
content = file.read()
splitted = content.split()

count = 0
for each in splitted:
    if len(each)<7:
        count+=1
    
print(count)