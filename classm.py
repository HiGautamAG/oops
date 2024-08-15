#class method is used to access the class variable and class method.
#staict method cannot access the class variable and class method.

class person:
    name ="Ramayan"
    
    def changename(self,name):
        self.name = name
        #self.name = person.name
        #person.name = name
        #self.__class__.name = name
        
        
p1 = person()
p1.changename("Mahabharat")
print(p1.name)
print(person.name)
