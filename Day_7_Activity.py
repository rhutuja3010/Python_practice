# Extra Activity

# 1.Create a simple calculator using functions

# Solution: -
class Calculator:
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def add(self):
        return self.a+self.b
    def subtract(self):
        return self.a-self.b
    def multiply(self):
        return self.a*self.b
    def divide(self):
        return self.a/self.b
s1=Calculator(22,33)
print(s1.add())
print(s1.subtract())


# 2. Write a program to define a student class that has the following attributes:
# - Name
# - Student ID
# - Marks
# The class must have a method to display the details.
# Also create an object that calls the method to display the details
# Solution: -
class Student:
    def __init__(self,name,student_ID,marks):
        self.name=name
        self.student_ID=student_ID
        self.marks=marks
s1=Student("Swati",1234,89)
s2=Student("Ram",7890,55)
print(s1.name,s1.student_ID,s1.marks)    

# 3. Write a program to explain the difference between a local and global variable
# Solution: -
# Global Variable
a="Hii"
def num():
    global b
    b="Hello"
num()
print(a)

# Local Variable
def sum():
    d="local"
    print(d)
sum()

# 4. Write a lambda function:
# - to calculate the sum of two numbers
# - that returns the square of a number
# - that returns the even numbers in a list
# Solution: -
add=lambda a,b: a+b
a=int(input("Enter the number:"))
b=int(input("Enter the number:"))
print(add(a,b))


square=lambda c,d:c**b
c=int(input("Enter the number:"))
d=int(input("Enter the number:"))
print(square(c,d))


even=lambda g:"even number" if g%2==0 else"odd number"
g=int(input("Enter the number:"))
print(even(g))


# 5.Write a program to :
# - Read the data from an existing file
# - Append data to the file
# - Display the data with newly appended data
# Solution: -
a=open(r"C:\Users\megha.ai.sharma\Desktop\data.txt",'r')
print(a.read())
a.close()

a=open(r"C:\Users\megha.ai.sharma\Desktop\data.txt",'a')
a.write("Raspberry")
a.close()

a=open(r"C:\Users\megha.ai.sharma\Desktop\data.txt",'r')
print(a.read())

# 6.Write a Python program to display the elements of a list in a reverse order
# Solution: -
# Solution: -

a=[1,4,7,3,9]
print(a[::-1])

# 7. . Write a program to use the addition operator to:
# - add integers
# - concatenate strings
# - on lists to make a single list
# Solution: -
# -Add the integers
a=int(input("Enter the number:"))
b=int(input("Enter the number:"))
print(a+b)

# -Concatenate Strings
a=str(input("Enter the first name:"))
b=str(input("Enter the last name:"))
print(a+b)

# -on lists to make a single list
a=["monkey","mouse","cat"]
b=[1,"2",3]
print(a+b)








# OOPS

# 1.Create a class mobile with 3 instance variables :brand , model, price
#  Create two functions  : call and discount
#  Def call (self,mobile_number):
#  Print(“calling to “,mobile_number)

# Def discount(self,discount_amt)
# Self.price -= discount amt

# Print the variable values and run the functions
# Make the variables private. Use get and set functions to change and print the values of private variables

class Mobile:
    def __init__(self,brand,model,price):
        self.__brand=brand
        self.__model=model
        self.__price=price
    def get_brand(self):
        return self.__brand
    def get_model(self):
        return self.__model
    def get_price(self):
        return self.__price
    def set_price(self,new_price):
        self.__price=new_price
    def call (self,mobile_number):
        print("calling to",mobile_number)
    def discount(self,discount_amt):
        self.price-=discount_amt
info=Mobile("vivo","v25",25000)
print(info.get_brand())
info.set_price(30000)
print(info.get_price())
