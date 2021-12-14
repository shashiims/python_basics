file = open("some_file.txt",'r')

readContent = file.read()

# print(readContent)

# file1 = open("/Users/shashisharma/Projects/python/ims_class/python _basic/day6/problems.txt",'r')

# readContent = file1.read()
# print(readContent)

#read single line from a file
# line = file.readline()
# print(line)

for eachLine in file:
    print(eachLine)
