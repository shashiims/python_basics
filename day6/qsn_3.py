
#input = Hello
def doubleCharacter():
    print("please give an input: ")
    userInput = input()
    repeatedResult = ""

    for each in userInput:
        singleRepeatedCharacter = each+each # first iteration, ee
        repeatedResult = repeatedResult+singleRepeatedCharacter #HHee

    return repeatedResult


if __name__ == "__main__":
    result = doubleCharacter()
    print(result)
    #H
    #HH
    #""+"HH"=>"HH"(repeatedResult)
    #'e'+'e'=>'ee'
    #'HH'+'ee'=>'HHee'