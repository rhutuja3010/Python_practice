##Q17
##Create a simple calculator using functions
#
#class Calculator:
#    def __init__(self,a,b):
#        self.a=a
#        self.b=b
#    def add(self):
#        return self.a+self.b
#    def substract(self):
#        return self.a-self.b
#    def multiply(self):
#        return self.a*self.b
#    def divide(self):
#        return self.a/self.b
#c=Calculator(6,2)
#print(c.add())
#print(c.substract())
#print(c.multiply())
#print(c.divide())
#    

#class Calculator:
#    def __init__(self,a,b):
#        self.a=a
#        self.b=b
#    def add(self):
#        return self.a+self.b
#    def substraction(self):
#        return self.a-self.b
#c=Calculator(5,2)
#print(c.add())
#print(c.substraction())





#Q18
##"Write a program to define a student class that has the following attributes:
##- Name
##- Student ID
##- Marks
##The class must have a method to display the details.
##Also create an object that calls the method to display the details"

#class Student :
#    def __init__(self,name,student_id,marks):
#        self.name=name
#        self.student_id=student_id
#        self.marks=marks
#info=Student("Rhutuja","Rhutuja_@",90)
#print(info.name,info.student_id,info.marks)

#class Student:
#    def __init__(self,ID,name, age):
#        self.ID=ID
#        self.name=name
#        self.age=age
#s=Student("Rhutuja_@","Rhutuja",22)
#print(s.ID,s.name,s.age)


##Q19
#Write a program to explain the difference between a local and global variable
#"a" is global variable
#1)
#def fun():
#    global a
#    a="Hii"
#fun()
#print(a)

#Q20
##"a" is local variable
#def fun():
#    c="local"
#    print(c)
#fun()
#print(c)


##Q20
###"Write a lambda function:
#
##- to calculate the sum of two numbers
#add=lambda a,b :a+b
#a=int(input("enter the no_1 :"))
#b=int(input("enter the no_2 :"))
#print(add(a,b))

##- that returns the square of a number
#squre=lambda a : a**2
#a=int(input("enter the no_1 :"))
#print(squre(a))
#
##- that returns the even numbers in a list"
#even=lambda a : "even" if a%2==0 else "odd"
#a=int(input("enter the no_1 :"))
#print(even(a))
#
#
##Excel_sheet_Q26:
#
#
#f=open(r"C:\Users\rhutuja.b.patil\Desktop\New_file1.txt","r")
#print(f.read())
#f.close()
#
#
#f=open(r"C:\Users\rhutuja.b.patil\Desktop\New_file1.txt","a")
#f.write("Welcome")
#f.close()
#
#
#f=open(r"C:\Users\rhutuja.b.patil\Desktop\New_file1.txt","r")
#print(f.read())