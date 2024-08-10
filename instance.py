# instance is an object of a class  


class Student:
    college_name ="BBDU"
    def _init_(self, name, marks):
        self.name = name
        self.marks = marks
        print("constructor called")
        
s1 = Student("Ansh", 90)
print(s1.name, s1.marks)


       