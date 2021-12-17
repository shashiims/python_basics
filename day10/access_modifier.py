class Car:
    __color=""
    brand =""
    regNo = ""
    engine =""

    def __init__(self,color,brand,regNo,engine):
        self.__color=color
        self.brand=brand
        self.regNo=regNo
        self.engine=engine

    def getColor(self):
        return self.__color
    
    def getOperationType(self):
        return self.operationType
    
    def __setColor(self,color):
        self.__color=color
    
if __name__ == "__main__":
   model3 = Car(color="Black",brand="Tesla",regNo="SomeREGNO",engine="EV")
   model3.engine="changedEV"
   print(model3.engine)
   #
   #
#    myCarColor = model3.getColor()
#    print("I have a car with color ",myCarColor)

#    i10= Car("Silver","Suzuki","REGNO","Petrol")
#    print(i10.__color)