class Person:
    dob = ""
    __age = ""

    def __init__(self,dob):
        self.dob=dob
        self.__calculateAge()

    def getAge(self):
        return self.__age

    def getDob(self):
        return self.dob

    def __calculateAge(self):
        self.__age = 2021 - int(self.dob)


if __name__ == "__main__":
    person1 = Person("2020")
    # person1.calculateAge()
    print(person1.getAge())

    person2 = Person("2010")
    # person2.calculateAge()
    print(person2.getAge())
   
