#static methods that dont use the self parameter (work at class level)

class student:
    college = "BBDU"
    def __init__(self, name, age, rollno):
        self.name = name
        self.age = age
        self.rollno = rollno
        
    @staticmethod
    def info():
        print("This is student class")
        
    def display(self):
        print("Name: ", self.name)
        print("Age: ", self.age)
        print("college: ", student.college)
        print("rollno:", self.rollno)
        
s1 = student("Ansh", 21, 1210211043)
s1.display()
student.info()


        
        
        
#decorator  @staticmethod   allow us to wrap another func in order to extend the behavviour of the wrapped function, without permanently modifying it.