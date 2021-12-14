# Write a program to reverse the elements in list and display it
# if list =[1,2,3] ans should be [3,2,1]

myList = [20, 30, 40, 50, 60]


def reverseList():
    reversedList = []
    i = 0
    lenOfList = len(myList)
    while i < lenOfList:
        item = myList[lenOfList-1-i]
        reversedList.append(item)
        i += 1

    return reversedList


def reverseListMethodOne():
    reversedList = []
    lenOfList = len(myList)
    i = lenOfList-1
    while i >= 0:
        item = myList[i]
        reversedList.append(item)
        i -= 1

    return reversedList


if __name__ == "__main__":
    result = reverseList()
    print(result)
    result1 = reverseListMethodOne()
    print(result1)

# iteration 1:
    # i = 0, lenOfList = 5, reversedList=[]
    # lenOfList-1-i = 5-1-0 = 4
# iteration 2:
    # i = 1, lenOfList = 5, reversedList=[60]
    # 5-1-1 = 3
# iteration 3:
    # i=2, lenOfList = 5, reversedList = [60,50]
