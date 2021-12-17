class User:
    photoUrl=""
    firstName=""
    lastName=""
    dob=""
    college=""
    address=""
    phone=""
    eamil=""
    gender=""

    def __init__(self, firstName):
        self.firstName = firstName


def displayPhoto():

    pass

def aboutSection(user):
    print(user.firstName)


if __name__=="__main__":
    user1 = User("John")
    aboutSection(user1)