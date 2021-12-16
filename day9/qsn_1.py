#write a program to count numbers of words from a text file

file = open("sample.txt",'r')
content = file.read()
listOfWords = content.split()
count = 0
for each in listOfWords:
    count+=1

print("Number of words is: ", count)
file.close()

# randomString = "this is just a random and random string"
# splitted = randomString.split("and")
# print(splitted)