# class & object 
# class is a blueprint for creating objects
# object is an instance of a class

# class Student:
#     name = "Raj"
    
# s1 = Student()
# print(s1.name)

# s2 = Student()
# print(s2.name)


# class car:
#     color = "black"
#     brand = "BMW"
    
# car1 = car()
# print(car1.color)
# print(car1.brand)    



# constructor  __init__ method is used to initialize the object.
# self is a reference to the current instance of the class

class Student:
   
    def __init__(self, fullname):
        self.name = fullname
        print("constructor called")
        
s1 = Student("Gautam")
print(s1.name)