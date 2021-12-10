
# def functionName():
#     print("I am inside my first function")

def displayName():
    print("John Doe")


def areaFinder(length,width):
    # print(width)
    # length = 10
    # width = 5
    area = length*width
    # print(area)
    return area


if __name__ == "__main__":
    # print("Initializing program...")
    # displayName()
    returnedValue1 = areaFinder(10,2) 
    print(returnedValue1)
    returnedValue2 = areaFinder(6,3)
    print(returnedValue2)

