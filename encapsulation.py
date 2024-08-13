#encapsulation  wrapping data and functions into a single unit(object).

class car:
    def __init__(self, name, model):
        self.__name = name
        self.__model = model
        print("Adding new car in database")
        
    def display(self):#self is class function or instance function
        print("Car Name: ", self.__name)
        print("Car Model: ", self.__model)
        
c1 = car("Audi", 2020)
c1.display()
c2 = car("BMW", 2021)
c2.display()