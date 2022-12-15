# def fibonacci_ser(n):
#     if(n <= 1):
#         return n
#     else:
#         return(fibonacci_ser(n-1) + fibonacci_ser(n-2))
# n = int(input("Enter number of terms:"))
# print("Fibonacci sequence:")
# for i in range(n):
#     print (fibonacci_ser(i))

# class Family:
#     family_name="Happy"
#     def __init__(self,fname,lname,age):
#         self.fname=fname
#         self.lname=lname
#         self.age=age
#     def full_name(self):
#         print(self.fname+" ",self.lname)
# father=Family("Vinod","Patil",51)
# mother=Family("Vinaya","Patil",47)
# print(Family.family_name)




##Q2
##Create a class named Student. Create class variable called school name. create instance 
##variables (name,age,class) using init method. Create two objects and print all the values 
##using the objects

# class Student:
#     school_name="Adarsh"
#     def __init__(self,name,age,Class):
#         self.name=name
#         self.age=age
#         self.Class=Class
# info=Student("Rhutuja",22,"Bsc")
# print(info.name,info.age,info.Class)


a=[5,6,7,4]
a.remove(6)
print(a)