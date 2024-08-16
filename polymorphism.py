# polymorphism(operator overloading) when the same operator is allowed in the class to use the method as a property.

print(5+6)

print("5" + "6")

print("gautam" + "ansh")#concatenation

print ([1,2,3] + [4,5,6])#merge



#complex number

class complex:
    def __init__(self, real, img):
        self.real = real
        self.img = img
        
    def __add__(self, number):
        newReal = self.real + number.real
        newImg = self.img + number.img
        return complex(newReal, newImg)
    
    def showNumber(self):
        print(self.real, "i +", self.img, "i")
        
num1 = complex(5, 6)
num1.showNumber()

num2 = complex(7, 8)
num2.showNumber()


num3 = num1 + num2
num3.showNumber()


#subtraction

class complex:
    def __init__(self, real, img):
        self.real = real
        self.img = img
        
    def __sub__(self, number):
        newReal = self.real - number.real
        newImg = self.img - number.img
        return complex(newReal, newImg)
    
    def showNumber(self):
        print(self.real, "i +", self.img, "i")
        
num1 = complex(5, 6)
num1.showNumber()

num2 = complex(7, 8)
num2.showNumber()

num3 = num1 - num2
num3.showNumber()




