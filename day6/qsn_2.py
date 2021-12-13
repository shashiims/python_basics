defined_string = "Problem one"


def characterCounter():
    print("Enter a character")
    inputCharacter = input()
    count = 0

    for each in defined_string:
        if each == inputCharacter:
            count = count+1
        else:
            # count=count-1
            print("Character not same")

    print(count)


if __name__ == "__main__":
    characterCounter()
