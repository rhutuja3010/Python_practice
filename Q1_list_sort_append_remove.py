#Q1-- Program that creates a list of computer languages. Use the appropriate list methods to:
# - sort the list
# - append to the list
# - remove an item from the list

lang=["python","Javascript","HTML","CSS","Bootsrap","React","Back-end","PHP","Java"]
# lang=[6,8,2,0,4]
# lang.sort()
# print(lang)

# lang.append("c++")
# print(lang)

# lang.remove("CSS")
# print(lang)


##Q2 - Write a program to print "Welcome to the world of Python"
# string="Welcome to the world of Python"
# print(string)

##Q3  Converting from one numeric datatype to another (casting)
# number=5.6
# integer=int(number)
# print(integer)


##Q4  Accepting three numbers from the user and displaying the product
# num1=int(input("enter the num1 :"))
# num2=int(input("enter the num2 :"))
# num3=int(input("enter the num3 :"))
# product=num1*num2+num3
# print(product)


##Q5 Write a program to accept a value from the user, store it in a variable and 
# display the datatype of a variable
# var=input("enter the number :")
# store=type(var)
# print(store)


##Q6 and Q7 Accept a string with "#" as a separator. Use the spilt method to display
#the strings in a listQ

# s="rhutuja#patil#20#accenture.com"
# b=s.split("#")
# print(b)


##Q8 Write program to make simple calculator by using if-else .
# num1=int(input("enter the num1 :"))
# num2=int(input("enter the num2 :"))
# operator=input("enter the operator (+,-,*,/,//,%)")
# if operator=="+":
#     print("Addition :",num1+num2)
# elif operator=="-":
#     print("Substraction :",num1-num2)
# elif operator=="*":
#     print("Multiplication :",num1*num2)
# elif operator=="/":
#     print("Division :",num1/num2)
# elif operator=="//":
#     print("Floor Division :",num1//num2)
# elif operator=="%":
#     print("Remander :",num1%num2)
# else:
#     print("plz enter correct operator")

##Q9 Accept a number from the user and test whether it is zero, positive or negative
#  number. Display a message accordingly
# num=int(input("enter the number :"))
# if num>0:
#     print(num,"is a positive number")
# elif num<0:
#     print(num,"is a negative number")
# elif num==0:
#     print("Number is zero")
# else:
#     print("plz enter number only")


##Q10 Write a program to display and find the sum of a list of numbers
# l=[4,5,5,1]
# b=sum(l)
# print(b)

##Q11  Write a program to display the numbers 10 to 6, and break the loop when it 
# is about to display the number 5

# i=10
# while i>=0:
#     print(i)
#     if i==5:
#         break
#     i-=1





##Q12 Write a program to know whether a sub string is there in the main string or not. 
# s=["Write a program to know whether a sub string is there in the main string or not"]
# for i in s:
#     for j in i:
#         print(j[0])

# s="Write a program to know whether a sub string is there in the main string or not"
# MyString1 = "Hii!Welcome to python Learning"
# if "to" in MyString1:
#     print("Yes! it is present in the string")
# else:
#     print("No! it is not present")





##13 Write a program to find out how many times a particular element is found in a 
# tuple
# import re
# text = 'Python exercises, PHP exercises, C# exercises'
# pattern = 'exercises'
# for match in re.finditer(pattern, text):
#     s = match.start()
#     e = match.end()
#     print('Found "%s" at %d:%d' % (text[s:e], s, e))




