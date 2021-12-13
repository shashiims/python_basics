# question is from problems.txt

defined_string = "Problem one"


def characterFinder():
    print("Please type your character:")
    inputCharacter = input()
    result = False

    for each in defined_string:
        if each == inputCharacter:
            result = True
            break
        else:
            result=False

    print(result)


if __name__ == "__main__":
    characterFinder()
