
def hideEmail():
    print("Please enter your email")
    inputEmail = input()
    hiddenEmail = ""
    index = 0
    characterCounts = len(inputEmail)
    lastIndex = characterCounts-1
    for each in inputEmail:
        if lastIndex == 0:
            hiddenEmail = "*"

        elif index == 0:
            hiddenEmail += each  # hiddenEmail = HiddenEmail+each

        elif index == lastIndex:
            hiddenEmail += each

        else:
            hiddenEmail += '*'

        index = index+1

    print(hiddenEmail)


if __name__ == "__main__":
    hideEmail()


# Assignment: if character is single print '*' only
