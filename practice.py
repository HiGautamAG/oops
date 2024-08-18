#create student class that takes name & marks of 3 sub as arguments in constructor. then create a method to print the avg.

class student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
        
    def get_avg(self):
        sum=0
        for val in self.marks:
            sum+=val
        print("Hi", self.name, "Your ang score is: ", sum/3)
        
s1 = student("Ansh", [75, 67, 89])
s1.get_avg()
        
        
s1.name ="Gautam"
s1.get_avg()



#create account class with 2 attrbutes - balance & account no. 
# create methods for debit, credit and print balance.


class account:
    def __init__(self, bal, acc):
        self.bal = bal
        self.acc = acc
        
        #debit
    def debit(self, amount):
        self.bal -= amount
        print("Amount Debited: ", amount)
        print("Remaining Balance: ", self.bal)
        
        #credit
    def credit(self, amount):
        self.bal += amount
        print("Amount Credited: ", amount)
        print("Remaining Balance: ", self.bal)
        
        #print balanceṇ
        
acc1 = account(1000, 123456789)
print("Account Balance: ", acc1.bal)
print("Account No: ", acc1.acc)
acc1.debit(500)
acc1.credit(1000)

#define a circle class to create a circle with radius r using the constructor.
# DEFINE an area method to calculate the area of the circle. # formula: 3.14 * r * r
# DEFINE a perimeter method to calculate the perimeter of the circle.


class Circle:
    def __init__(self, r):
        self.r = r
        
    def area(self):
        return 3.14 * self.r * self.r
    
    def perimeter(self):
        return 2 * 3.14 * self.r
    
c1 = Circle(5)
print("Area of Circle: ", c1.area())
print("Perimeter of Circle: ", c1.perimeter())
