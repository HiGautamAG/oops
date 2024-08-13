#Method are functions that belongs to the object.


class car:
    def __init__(self, name, model):
        self.name = name
        self.model = model
        print("Adding new car in database")
        
    def display(self):#self is class function or instance function
        print("Car Name: ", self.name)
        print("Car Model: ", self.model)
        
c1 = car("Audi", 2020)
c1.display()
c2 = car("BMW", 2021)
c2.display()
c3 = car("Mercedes", 2022)
c3.display()