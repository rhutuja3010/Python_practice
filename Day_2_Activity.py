# # 1.Get any number as input from user and check the given number is odd or even
# # Hint : to check even the condition is  :
# # n % 2 == 0

# # Solution: 
# n=int(input("Enter the number::"))
# if n%2==0:
#     print("The number is even")
# else:
#     print("The number is odd")



# # 2. Get a number as input and check if the number is divisible by 5 or not.

# # Solution: -
# a=int(input("Enter the number:"))
# if a%5==0:
#     print("Yes,It is divisble by 5")
# else:
#     print("No,It is not divisble by 5")



# # 3.Get three numbers from users and find the biggest number among them and print it.
# # Solution: -
# a=int(input("Enter the number:"))
# b=int(input("Enter the number:"))
# c=int(input("Enter the number:"))
# if a>b and a>c:
#     print(a,"is the greatest number")
# elif b>c and b>a:
#     print(b,"is the greatest number")
# else:
#     print(c,"is the greatest number")


# # 4. Write a program using while loop to print even numbers in range of 1 to 25.
# # Solution: -
# i=1
# while i<=25:
#     if i%2==0:
#         print(i)
#     i+=1

# # 5. Write a program using while loop to evaluate factorial of a number.
# # Solution: -
# i=1
# fac=1
# a=int(input("Enter the number:"))
# while i<=a:
#     fac*=i
#     i+=1
# print(fac)
##or
# fac=1
# n=int(input("enter the no :"))
# while n>0:
#     fac*=n
#     n-=1
# print(fac)


# # 6. Accept a number from  store it in variable  name as  age If the age greater 
# # then 18 and equal to 60 then print Person can vote If the age is less than 18 
# # and greater than 0 print Person cannot vote Else print invalid age.
# # Solution: -
# age=int(input("Enter your age:"))
# if age>18 or age<=60:
#     print("Person can vote")
# elif age<18 or age>0:
#     print("Person cannot vote")
# else:
#     print("Invalid Age")

# # 7. Create a list with 10 numbers and  Display numbers from a list using  a for loop.
# # Solution: -
# no=[1,2,3,4,5,6,7,8,9,10]
# for i in no:
#     print(i)

# # 8. Create a list and print in reverse order using slicing.
# # Solution: -
# list=["dog","cat","monkey","bear","deer","pig","goat"]
# print(list[::-1])

# # 9.Create two list and join two list using + operator
# # Solution:-
# a=[1,2,3]
# b=[4,5,6]
# print(a+b)

# # 10. Create a list and add a new item in the 4th index.
# # Solution: -
# list=[1,2,3,4,5]
# list.insert(4,"ram")
# print(list)

# # 11. Write a program to find value 20 in a list. If 20 is present in the list 
# # replace it with 200.
# # Solution: -
# list1=[5,4,3,20,10,89,77]
# for i in range(len(list1)):
#     if list1[i]==20:
#         list1[i]=200
# print(list1)


# list1=[5,4,3,20,10,89,77]
# for i in range(len(list1)):
#     if list1[i]==20:
#         list1[i]=200
# print(list1)

# # 12. Create a tuple with 10 items and reverse it.
# # Solution: -
# a=("maths","english","biology","chemistry","hindi","punjabi","physics","economicas","history","accounts")
# print(a[::-1])



# # 13. Given is a nested tuple. Write a program to modify the first item(22) of the 
# # list inside a following tuple to 222.
# # Eg: t1 = (11,[22,33],44,55)
# # Solution: -
# t1 = (11,[22,33],44,55)
# for i in t1:
#     if type(i)==list:
#         for j in range(len(i)):
#             if i[j]==22:
#                 i[j]=222
# print(t1)






# # Extra Activity
# # 1.Program that creates a list of computer languages. Use the appropriate list 
# # methods to:
# # - sort the list
# # - append to the list
# # - remove an item from the list
# # Solution: -
# # -Sort the list
# a=["Python","C","Java","NodeJs"]
# a.sort()
# print(a)


# # -Append to the list
# a=["Python","C","Java","NodeJs"]
# a.append("ReactJs")
# print(a)
# # -remove an item from list

# a=["Python","C","Java","NodeJs"]
# a.remove("Java")
# print(a)


# l=[3,5,6,8]
# l.remove(5)
# print(l)



# # 2. Write a program to print "Welcome to the world of Python.
# # Solution:-
# n=input("Enter a sentence here:")
# print(n)

# # 3. Converting from one numeric datatype to another (casting).
# # Solution: -
# z=1
# print(float(z))

# # 4. Adding two numbers and storing it in a variable.
# # Solution: -
# a=55
# b=45
# c=a+b
# print(c)

# # 5. Accepting three numbers from the user and displaying the product.
# # Solution: -
# a=int(input("Enter the number:"))
# b=int(input("Enter the number:"))
# c=int(input("Enter the number:"))
# print(a*b*c)





# # 6. Write a program to accept a value from the user, store it in a variable and 
# # display the datatype of a variable.
# # Solution: -
# y=int(input("Enter the number:"))
# v=y
# print(type(v))

# # 9. Accept two numbers and an operator from the user. Basis the operator, perform
# #  the operation on the numbers.
# # Solution: -
# d=int(input("Enter the number:"))
# e=int(input("Enter the number:"))
# operator=input("Enter the operator:")
# if operator=="+":
#     print(d+e)
# elif operator=="-":
#     print(d-e)
# elif operator=="*":
#     print(d*e)
# elif operator=="/":
#     print(d/e)
# elif operator=="**":
#     print(d**e)
# elif operator=="//":
#     print(d//e)
# elif operator=="%":
#     print(d%e)
# else:
#     print("invalid operator")


# # 10. Accept a number from the user and test whether it is zero, positive or 
# # negative number. Display a message accordingly.
# # Solution: -
# n=int(input("Enter the number:"))
# if n>0:
#     print("The number is positive")
# elif n<0:
#   print("The number is negative")
# else:
#     print("The number is zero")

# # 11. Write a program to display and find the sum of a list of numbers.
# # Solution: -

# a=[2,2,6]
# s=sum(a)
# print(s)

# a=[2,5,7,9,12]
# sum=0
# for i in a:
#     sum+=i
# print(sum)

# # 12. Write a program to display the numbers 10 to 6, and break the loop when it is 
# # about to display the number 5.
# i=10
# while i>=1:
#     print(i)
#     if i==6:
#         break
#     i-=1
