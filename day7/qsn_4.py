# Write a program to take number of inputs from user and fill the list
# with those inputs. User should be able to choose how many items s/he
# wants to give

def fillList(inputCount):
    filledList = []

    i = 1
    while i <= inputCount:
        print("Enter your "+str(i) + " input")
        userInput = input()
        filledList.append(userInput)
        i += 1

    return filledList


if __name__ == "__main__":
    print("Please type numbers of input you want to give:")
    noOfInputasString = input()
    noOfInput = int(noOfInputasString)
    result = fillList(noOfInput)
    print("You have entered the following items")
    print(result)
