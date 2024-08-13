# Abstraction is the concept of hiding the complex implementation details and showing only the necessary features of the object.
# Abstraction is achieved using abstract classes and interfaces in Python.

class car:
    def __inint__(self):
        self.acc = False
        self.brk = False
        self.clutch = False
        
    def start(self):
        self.acc = True
        self.brk = False
        self.clutch = True
        print("Car is started")
        
        
car1 = car()  
car1.start()  