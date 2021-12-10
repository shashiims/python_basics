myList = [2, 3, "lsfk", True, False]
myDictionary = {'keyName': "someValue", "anotherKey": True}

userDetails = {"firstname": "John",
               "lastname": "Doe", "address": "Kathmandu, Nepal", "phone": "98********", "age": 45}

initialName = userDetails["firstname"]
fullName = initialName+" "+userDetails['lastname']
# print(fullName)

address = userDetails.get("address")
# print(address)

valuesOnly = userDetails.values()
# print(valuesOnly)
keysOnly = userDetails.keys()
# print(keysOnly)

userDetails.update({"firstname":"Changed FirstName","lastname":"Changed LastName"})
# print(userDetails)
# myList.clear()
