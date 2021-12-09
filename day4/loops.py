# while  loop
# i = 0

# while i < 10:
#     print(i)
#     i = i+1  # equivalent to i+=1
#     if i!=5:
#         continue
#     else:
#         print("Halfway there!")

#     # if i==5:
#     #     break
# print("loop ended")
# myList = ["mon", "tue", "sat", "sun"]
# for each in myList:
#     print(each)
#     if each=="sat":
#         print("Holiday!")
#         break
#     else:
#         print("Not holiday!")

# print("loop ended")
# tempList=[0,1,2,3]
# for a in range(4):
#     print(a)
#     item = myList[a]
#     print(item)

# noOfItems = len(myList)
# for a in range(noOfItems):
#     print(myList[a])

myList = ["mon", "tue", "sat", "sun"]

i = 0
while i<len(myList):
    print(myList[i])
    i+=1