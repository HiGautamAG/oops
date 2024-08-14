# del keyword is used to delete the reference of the object.

class student:
    def __init__(self, name):
        self.name = name
        
s1 = student("Ansh")
print(s1.name)
del s1.name
print(s1.name)