
numbers = [5, 9, 1, 90, 15,0]


# def minMax():
#     minimum = numbers[0]
#     maximum = numbers[0]

#     for each in numbers:
#         if each < minimum:
#             minimum = each

#     for each in numbers:
#         if each > maximum:
#             maximum = each

#     print("Minimum is ", minimum)
#     print("Maximum is ", maximum)

def findMinimum():
    minimum = numbers[0]
    for each in numbers:
        if each < minimum:
            minimum=each

    print(minimum)


if __name__ == "__main__":
    # minMax()
    findMinimum()
