list = [4, 5, 2,]  # unsorted
# list1 = [1,2,4,5,9] #sorted list

# selection sort


def findMin(startIndex):
    j = startIndex
    min_val = list[startIndex]
    currentMinValueIndex = startIndex
    while j < len(list):
        if list[j] < min_val:
            min_val = list[j]
            currentMinValueIndex = j
        j += 1
    return currentMinValueIndex


if __name__ == "__main__":
    lengthOfList = len(list)
    i = 0
    while i < lengthOfList-1:
        minIndex = findMin(i)

        tempVal = list[i]
        list[i] = list[minIndex]
        list[minIndex] = tempVal
#         temp = list[1]
# list[1]= list[3]
# list[3]= temp

        i += 1

print("sorted list is \n", list)

#Assignment: Write a program to sort a list in descending order
# you can choose above list for input
