# 1.Write a Python program to create a Vehicle class with max_speed and mileage instance

# Solution: -
class Vehicle:
    max_speed=260
    mileage=25
    
BMW=Vehicle()
print(BMW.max_speed)

# 2.Create a class named Student. Create class variable called school name. 
# create instance variables (name,age,class) using init method. Create two 
# objects and print all the values using the objec

# Solution: -
class Student:
    school_name="DPS"
    def _init_(self,name,gender,grade,age):
        self.name=name
        self.gender=gender
        self.grade=grade
        self.age=age
    def details(self):
        print(self.name,self.gender,self.school_name)
student_data=Student("James","MAle",5,11)
print(student_data.school_name)
print(student_data.grade,student_data.name)


class Student:
    school_name="DPS"
    def __init__(self,name,gender,grade,age):
        self.name=name
        self.gender=gender
        self.grade=grade
        self.age=age
    def details(self):
        print(self.name,self.gender,self.school_name)
student_data=Student("James","Male",5,11)
s2=Student("Sham","male",12,18)
print(student_data.school_name)
print(student_data.grade,student_data.name)


# 3.Create a child class Bus that will inherit all of the variables and methods of the Vehicle class
# Solution: -
# Create a vehicle class with 3 instance variables, type,milage and model
# Create a child class with two instance variables capacity and build_year
# Create a object for child class and print all the values
# Create a class and two child classes.

# 4.Create a example for multilevel inheritance .

# Solution: -
class Vehicle:
    def __init__(self,Type,milege,model):
        self.Type=Type
        self.milege=milege
        self.model=model

class Bus(Vehicle):
    def __init__(self,Type,milage,model,pas_capacity,buildyear):
        Vehicle.__init__(self,Type,milage,model)
        self.pas_capacity=pas_capacity
        self.buildyear=buildyear
vehicle=Bus("bus",25,"old",50,2002)
print(vehicle.milege,vehicle.buildyear)
print(vehicle.model)

# Functions

# 1.Create a function that can accept two arguments name and 


# Solution: -
#   age and print its value
def details(name,age):
    print("NAME"+"=",name)
    print("AGE"+"=",age)
x=input("enter your name")
y=int(input("enter your age"))
details(x,y)


# 2.Write a function func1() such that it can accept a variable 

# Solution: -
#   length of  argument and print all arguments value
def func1(x):
    print(len(x))
    print(x)
func1("happyending")


#  3.Write a function calculation() such that it can accept two 

# Solution: -
  #variables and calculate the addition and subtraction of them. And a
  #lso it must return both addition and subtraction in a single return 
  #call
def add_sub(a,b):
    c=a+b
    d=a-b
    return c,d

print(add_sub(34,56))

# 4.Create a function showEmployee() in such a way that it 
#  should accept employee name, and its salary and display both. 
#  If the salary is missing in the function call assign default value 
#  9000 to salary

# Solution: -
def showEmployee(employee_name,salary=9000):
    print(employee_name,salary)
    
showEmployee("Raman")
showEmployee("Megha",12000)


# 5.Create an inner function to calculate the addition in the 
#   following way


# Solution: -
def outer_fun(a, b):
    
    def addition(a, b):
        return a + b

    add = addition(a, b)
    return add + 5

print(outer_fun(20,15))


# 6.Write a recursive function to calculate the sum of numbers 
#  from 0 to 10


# Solution: -
def sum_of_numbers(x,y):
    sum=0
    if x<=y:
        return x+(sum_of_numbers(x+1,y))
    else:
        return sum
print(sum_of_numbers(0,10))

        
# 7.Assign a different name to function and call it through the new name

# Solution: -
def full_name(fname,lname):
    print(fname+" "+lname)
display_name=full_name
display_name("Radha","Sharma")
