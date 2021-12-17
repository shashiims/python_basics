
class NewClass:
    my_var1 = "some value"
    my_var2 = "some another value"
    a = 5

    def myMethod():
        print("inside my method")


class SmartPhone:
    color = ""
    storage = ""
    memory = ""
    os = ""

    def getColor(self):
        return self.color

    def displayMemory(self):
        print(self.memory)


class Person:
    name = ""
    dob = ""
    address = ""
    phone = ""
    gender = ""

    def __init__(self,n): #objname = Person("John")
        self.name = n
        

    def getName(self):
        return self.name

    def getPhone(self):
        return self.phone

    def getAge(self):
        pass
        # code to calculate and return age from dob


if __name__ == "__main__":
    # print("Initializing....")
    # somePerson = Person()
    # somePerson.getAge()
    # print(somePerson.phone)
    iphone = SmartPhone()
    samsung = SmartPhone()

    person1 = Person("John")
    print(person1.name)
    person1 = Person("not John")
    print(person1.name)
    # person2 = Person("Some other name")
    # print(person2.name)
    # print(person1.name)
