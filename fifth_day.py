##Python statement and arithmetic operators
##
##1. Using input() function accepts 3 numbers from user and print the biggest number.
#
#solution---------------------------------------------------------------------


#num1=int(input("enter the number_1 :"))
#num2=int(input("enter the number_2 :"))
#num3=int(input("enter the number_3 :"))
#if num1>num2:
#    print(num1,"num1 is grater")
#elif num2>num3:
#    print(num2,"num2 is grater")
#else:
#    print(num3,"num3 is grater")



#2. Store the below words and each variable and print it
#Sample input
#All work and no play make Jack a dull boy.

#solution---------------------------------------------------------------------


#str1="All work and no play make Jack a dull boy"
#s=str1.split()
##print(s)
#for i in s:
#    print(i)



#3. Accept and long string from user and find the number of vowels in that string.
#Sample input

#solution---------------------------------------------------------------------


#string="My name is Paul I live in Mumbai"
#count=0
#l=[]
#for i in string:
#    if i=="a" or i=="e" or i=="i"or i=="I" or i=="o" or i=="u":
#        count+=1
#print(count)


##4. Input 2 numbers from user and an operator from user + , - ,* , / based on operator do the operation
##
##Sample input
##
##10 10 * it should do multiplication and display the output.
#

#solution---------------------------------------------------------------------

#a=7
#b=4
#print(a+b)
#print(a-b)
#print(a*b)
#print(a/b)

##5. Run below code on REPL and observer the output
#
##5 % 2
##9 % 5
##15%12
##12 % 15
##0 % 7
##7 % 0
#print(5%2)
#print(9%5)
#print(15%12)
#print(0%7)
#print(7%0)


##2 Python Conditioning if and else
##
##1. Accept a number from store it in variable name as age
##
##If the age greater then 18 and equal to 60 then print Person can vote
##
##If the age is less than 18 and greater than 0 print Person cannot vote
##
##Else print invalid age.

#solution---------------------------------------------------------------------

#
#age=int(input("enter the age :"))
#if age>=18 and age<=60:
#    print("Person can vote")
#elif age<18 and age>0:
#    print("Person cannot vote")
#else:
#    print("invalid age")
    
#
#2. Accept a character from user and check whether is vowel or not.

#solution---------------------------------------------------------------------


#alphabate=input("enter the alphabate :")
#if alphabate=="a" or alphabate=="e" or alphabate=="i" or alphabate=="o" or alphabate=="u":
#    print("vovel")
#else:
#    print("not")


##3. Accept username and password as string from user. If the username==” Admin” and 
##password==”123” then print Welcome Admin else print invalid username or password

#solution---------------------------------------------------------------------

#
#username=input("enter the username :")
#password=int(input("enter the password :"))
#if username=="Admin" and password==123:
#    print("Welcome")
#else:
#    print("invalid username or password")


#Python String operation
#1. Using 2 strings, s1 and s2, create a new string by appending s2 in the middle of s1
#Sample input
#s1 = "Samy"
#s2 = "Kelly"
#Sample output
#SaKellymy

#solution---------------------------------------------------------------------


#s1 = "Samy"
#s2 = "Kelly"
#print(s1[:2]+s2+s1[2:])


#2. Count all lower case, upper case, digits, and special symbols from a given string
#Sample input
#str1 = "P@#yn26at^&i5ve"
#Sample output
#Total counts of chars, digits, and symbols
#Chars = 8
#Digits = 3
#Symbol = 4

#solution---------------------------------------------------------------------


#str1 = "P@#yn26at^&i5ve"
#chr_count=0
#digit_count=0
#symbol_count=0
#c_l=[]
#d_l=[]
#s_l=[]
#l1='abcdefghijklmnopqrstuvdxyz'
#l2='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
#symbol='!@#$%^&*'
#for i in range(len(str1)):
#    if str1[i]in l1 or str1[i] in l2:
#        c_l.append(str1[i])
#        chr_count+=1
#    elif str1[i] in symbol :
#        s_l.append(str1[i])
#        symbol_count+=1
#    else:
#        d_l.append(str1[i])
#        digit_count+=1
#print("Chars =",chr_count)
#print("Digit =",digit_count)
#print("Symbol =",symbol_count)


#3. Accept a string, and return the sum and average of the digits that appear in the string, 
#ignoring all other characters
#Sample input
#str1 = "English = 78 Science = 83 Math = 68 History = 65".
#Sample output
#sum is 294
#average is 73.5

#solution---------------------------------------------------------------------


#str1 = "English = 78 Science = 83 Math = 68 History = 65"
##print((English+Science+Math+History)/4)
##or 
#sum=0
#count=0
#str2=str1.split(" ")
#for i in str2:
#    if i.isdigit():
#        sum+=int(i)
#        count+=1
#print("Sum :",sum)
#print("Average :",sum/count)





##4. Accept a long string from user and return each word in reverse way
##
##Sample input
##
##My name is Sam I live in Mumbai
##
##Sample output
##
##Mumbai in live I Sam is name My

#solution---------------------------------------------------------------------

#
#s="My name is Sam I live in Mumbai"
#a=s.split()
#b=a[::-1]
#j=" ".join(b)
#print(j)
#
##or
#a=s.split()
#for i in a:
#    b=a[::-1]
#    j=" ".join(b)
#print(j)
#



#
##5. Accept a string from user and print the word with is occurring maximum time.

#solution---------------------------------------------------------------------


##
##Sample input
##
##My name is Sam. Sam lives in Mumbai. Sam plays cricket.
##
##Sample output
##
##Sam is occurring 3 times
#
#str1="My name is Sam. Sam lives in Mumbai. Sam plays cricket"
#s=str1.split()
##print(s)
#c=str1.count("Sam")
#print(c)
#l=[]
#for i in str1:
#    s=str1.split()
#    count=1
#    for j in s:
#        if j=="Sam":
#            count+=1
#print("Sam is occurring :",count,"times")
    
    

#Python Collection
#
##1. Given a Python list, find value 20 in the list, and if it is present, replace it with 200.
## Only update the first occurrence of a value

#solution---------------------------------------------------------------------


#l=[5,2,4,20,6,66,20,9]
#for i in range(len(l)):
#    if l[i]==20:
#        l[i]=200
#print(l)
        
#
#2. Sort a tuple of tuples by 2nd item
#
#Sample input

#solution---------------------------------------------------------------------

#
#tuple1 = (('a', 23), ('b', 37), ('c', 11), ('d',29))
#
#Sample output
#
#(('c', 11), ('a', 23), ('d', 29), ('b', 37))

#tuple1 = (('a', 23), ('b', 37), ('c', 11), ('d',29))
   
    

#        
#3. Create below 2 sets and try intersection, union, difference, symmetric_difference() and 
#isdisjoint() function
#
#Sample input

#solution---------------------------------------------------------------------


#
#set1 = {10, 20, 30, 40, 50}
#set2 = {60, 70, 80, 90, 10}


#set1.intersection_update(set2)
#print(set1)

#set3=set1.union(set2)
#print(set3)

#set3=set1.difference(set2)
#print(set3)

#set3=set1.symmetric_difference(set2)
#print(set3)




#4. Create an empty dictionary and do following operation on it
#
#Add 5 key and values in it
#
#Accept a key from user and remove that key and values from dictionary

#solution---------------------------------------------------------------------


#dic={"Rhutuja":567,"Sonu":234,"Monu":455,"Tanu":345}
#key=input("enter the name :")
#if key in dic:
#    del dic[key]
#    print(dic)
#
#Accept a key from user and print the value of that key
#
#Accept all key and values from the dictionary



#3 Python logical operators
#
#1.Enter the following expressions into the Python shell and observe the output:
#
#True or False
#print(True or False)
#True and False
#print(True and False)
#not (False) and True
#print(not(False) and True)
#True or 7
#print(True or 7)
#False or 7
#print(False or 7)
#True and 0
#print(True and 0)
#False or 8
#print(False or 8)
#"happy" and "sad"
#print("happy" and "sad")
#"happy" or "sad"
#print("happy" or "sad")
#"" and "sad"
#print(" " and "sad")
#"happy" and "“
#print("happy" and " ")



#Python Loops

##1. Write a program using while loop to print even numbers in range of 1 to 25.

#solution---------------------------------------------------------------------


#for i in range(1,26):
#    if i%2==0:
#        print(i)


##2. Write the same using for loop.

#solution---------------------------------------------------------------------


#sum=0
#for i in range(1,26):
#    if i%2==0:
#        sum+=i
#print(sum)


##3. Write a program using while loop to evaluate factorial of a number.

#solution---------------------------------------------------------------------


#num=int(input("enter the no :"))
#fac=1
#while num>0:
#    fac=fac*num
#    num-=1
#print(fac)
    


#4. Write a function sum_of_squares that computes the sum of the squares
#Example, sum_of_squares(987) should return 194, since9**2 + 8**2 + 7**2 == 81 + 64 + 49 == 194
#Sample
#um_of_squares(1)
#1
#sum_of_squares(9)
#81
#sum_of_squares(11)
#2
#sum_of_squares(121)

#solution---------------------------------------------------------------------

#i=1
#squre_sum=0
#while i<=3:
#    num=int(input("enter the no :"))
#    squre=num**2
#    squre_sum+=squre
#    i+=1
#print(squre_sum)
    
    
#6
#5. Write a Python program to get the Fibonacci series between 0 to 50.
#Note : The Fibonacci Sequence is the series of numbers :
#0, 1, 1, 2, 3, 5, 8, 13, 21, ....
#Every next number is found by adding up the two numbers before it.
#Expected Output : 1 1 2 3 5 8 13 21 34

#solution---------------------------------------------------------------------

#limit=int(input("enter the no :"))
#num1=0
#num2=1
#for i in range(0,limit):
#    if (i<=1):
#        num3=i
#    else:
#        num3=num1+num2
#        num1=num2
#        num2=num3
#    print(num3,end=" ")



#limit=int(input("enter the no :"))
#n1=0
#n2=1
#for i in range(0,limit):
#    if i<=1:
#        num3=i
#    else:
#        num3=n1+n2
#        n1=n2
#        n2=num3
#    print(num3,end=" ")

#
#num=int(input("enter the no :"))
#fac=1
#while num>0:
#    fac*=num
#    num-=1
#print(fac)



#tuple1 = (('a', 23), ('b', 37), ('c', 11), ('d',29))
#tuple1=list(tuple1)
#t = 0   
#l = len(tuple1)   
#for k in range(0, l):   
#    for l in range(0, l-k-1):   
#        if (tuple1[l][1] > tuple1[l + 1][1]):   
#            new = tuple1[l]   
#            tuple1[l]= tuple1[l + 1]   
#            tuple1[l + 1]= new   
#tuple1=tuple(tuple1)
#print(tuple1)


#
#tuple1 = (('a', 23), ('b', 37), ('c', 11), ('d',29))
#tuple1=list(tuple1)
#l=len(tuple1)
#for k in range(0,l):
#    for l in range(0,l-k-1):
#        if (tuple1[l][1]>tuple1[l+1][1]):
#            new=tuple1[l]
#            tuple1[l]=tuple1[l+1]
#            tuple1[l+1]=new
#tuple1=tuple(tuple1)
#print(tuple1)





##Python function
##
##1. Write a function which accepts list containing integer and find the maximum in that list
##
##Sample input


#solution---------------------------------------------------------------------

##List1=[4,55,66,77,88,89,444]
##print(max(List1))
#def fun(List1):
#    max=0
#    for i in List1:
#        if i>max:
#            max=i
#    print(max)
#fun([4,55,66,77,88,89,444])



#2. Write an inner function / nested function which will accept a number and calculate the factorial of that number.

#solution---------------------------------------------------------------------

#def fac(num):
#    if num==0:
#        return 1
#    return num*fac(num-1)
#print(fac(5))



##3. Write a lambda function which accepts 3 numbers and return the minimum number
##get_min = lambda a, b : a if a < b else b

#solution---------------------------------------------------------------------

#store=lambda n1,n2,n3:min(n1,n2,n3)
#print(store(5,2,8))


#4. Write a Python program to reverse a string and prints its alternate characters

#solution---------------------------------------------------------------------

#s="Rhutuja"
#print(s[::-1])
#def reverse1(s):
#    for i in range(len(s)):
#        print(s[i][::-1])
#reverse1("Rhutuja")



#5. Write a function which takes 2 numbers as commandline argument from user and create Fibonacci series till 1000.

#solution-------------------------------------------------------------

#num1=0
#num2=1
#for i in range(1,1000):
#    if (i<=1):
#        num3=i
#    else:
#        num3=num1+num2
#        num1=num2
#        num2=num3
#    print(num3,end=" ")









#Write all file content into new file by skipping  line 5  from following file
#Sample input
#test.txt file:
#line1
#line2
#line3
#line4
#line5
#line6
#line7
#Sample output
# newFile.txt should be
#line1line2
#line3
#line4
#line6
#line7

#with open("today.txt","w") as f:
#    f.write("It is our attitude that drives us to the success.\n It is the thing that makes or breaks a person.\nIf you have a positive attitude in life, you will always look at the better side of things; you will always bring the positive out of every situation.\n This will keep you content and happy and will keep your mind peaceful.")
#    f.close()

#with open("today.txt","r") as fr:
#    lines=fr.readlines()
#    i=1
#    with open("today.txt","w") as fw:
#        if i!=5:
#            fw.write(line)
#        i+=1
#print("Deleted")
#


##Q2
##Accept a file name from user and print the file contain from last line to first line
#
#text=input("entter the ile name you want to open :")
#input_file=open(text,"r")
#l=[]
#for line in input_file:
#    l.append(line)
#print(l[::-1])
