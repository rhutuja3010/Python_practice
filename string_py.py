#------------------------------------------------------------------------
#string:
#str1 = "Hello World!!!!..."
#print(str1)
#print(type(str1))
#print(len(str1))
#for i in range(len(str1)):
#    print(i,str1[i])
#print(str1[5])
#print(str1[5:14])
#print(str1[::-1])
#print(str1[5:14:2])
#print(str1+" welcome")
#
#print(str1.replace("H","J"))
#multiline strings:
#sentence = """Hi how are you
#welcome to python training
#have a nice day python!!!!!"""
#print(sentence.replace("python","java"))
#print(str1.lower())
#print(str1.upper())
#print("hi how are you doing".title())
#print(str1.capitalize())
#strip: ---- remove the whitespace at begining and end
#s = "#Hello!!#"
#print(s.strip('#'))
#print(s.lstrip('#'))
#print(s.rstrip('#'))
#print("HI HOW ARE YOU DOING".title())
#print("HI HOW ARE YOU DOING".capitalize())
#split:convert str into a list of strings
# s = "Hi how #are you doing"

#print(s.split())
#join:will work only for list of strings:
#syntax:
#    
#joining character.join(list name)\
#s = ["Prevention","is","better","than","cure"]
# 
#str2 = " ".join(s)
#print(str2)
#name = "msk"
#age = 22
#
#print("Your name is",name,"and your age is",age)
#
#
#print("your name is {} and your age is {}".format(name,age))
#
#f-string
#name = "msk"
#age = 23
#print(f"your name is {name} and your age is {age}")
#r-string --- raw string:
#print(r"C:\Users\meenakshi.sugumar\OneDrive - Accenture\Desktop\today\abc.txt")
#print("C:\\Users\\meenakshi.sugumar\\OneDrive - Accenture\\Desktop\\today\\abc.txt")



#Q1

#1. Write a program to create a new string made of an input string’s first, middle, and last character.
#Q1
#Eg: “James” output : “Jms”
#
#· Hint: String index always starts with 0
#
#· Use string indexing to get the character present at the given index
#
#· Get the index of the middle character by dividing string length by 2

#string=input("enter the string :")
#a=int(len(string)/2)
#print(string[0]+string[a]+string[-1])



#Q2
#Given two strings, s1 and s2. Write a program to create a new string s3 by appending s2 in the 
#middle of s1.

#s1 = "Ault"
#
#s2 = "Kelly"
#
#o/p : AuKellylt
#
#Hint: Use built-in function len(s1) to get the string length.
#
#Next, get the middle index number by dividing string length by 2.

#o/p : AuKellylt
#s1 = "Ault"
#s2 = "Kelly"
#s3=list(s1)
#s3[2:2]=s2
#s4="".join(s3)
#print(s4)



#Q3
#Given string contains a combination of the lower and upper case letters. Write a program 
#to arrange the characters of a string so that all lowercase letters should come first.
#
#Str1 = “WElcome”
#
#o/p: lcomeWE
#
#Hint: Create two lists lower and upper
#
#Iterate a string using a for loop
#
#In each loop iteration, check if the current character is the lower or upper case using the islower() string function.
#
#If a character is the lower case, add it to the lower list, else add it to the upper list
#
#to join the lower and upper list using a join() function.
#
#convert list to string
#
#print the final string

##o/p: lcomeWE
#Str1 = "WElcome"
#upperletter=[]
#lowerletter=[]
#for i in Str1:
#    if i.isupper():
#        upperletter.append(i)
#    else:
#        lowerletter.append(i)
#    letter=lowerletter+upperletter
#join_letter="".join(letter)
#print(join_letter)


#Q4
#Write a program to count occurrences of all characters within a string
#
#Str1 = “Apple”
#
#Op: {‘A”:1,’p’:2,’l’:1,’e’:1} · Hint: create an empty dictionary to store the result. character is the key, and the count is the value
#
#· Iterate each character from a string s1 using a loop
#
#· In the body of a loop, use the count() function to find how many times a current character appeared in a string
#
#· Add key-value pair in a dictionary


#Str1 = "Apple"
#d={}
#for i in Str1:
#    value=Str1.count(i)
#    d.update({i:value})
##    d[i]=value
#print(d)


#Q5
#Write a program to split a given string on hyphens and display each substring.
#
#str1 = Emma-is-a-data-scientist
#
#o/p : Displaying each substring
#
#Emma
#
#is
#
#a
#
#data
#
#scientist

#string="I'm_Rhutuja_Patil"
#a=string.split("_")
#for i in a:
#    print(i)








#Activity_1---------------------

#Q1
#Dict1={"name": "Plato", "country": "Ancient Greece", "born": -427, "teacher": "Socrates", "student": "Aristotle"}
#i)  Print the year that Plato born.

#print(Dict1["born"])
#or
#print(Dict1.get("born"))


#ii)  Change the year from -427 to 428

#Dict1["born"]=428
#print(Dict1)


#iii)
#“work”:[“Apology”,”Phaedo”,”Republic”,”Symposium”] 
#add this as new key pair in the above dictionary


#Dict1["work"]=["Apology","Phaedo","Republic","Symposium"] 
#print(Dict1)



#Q2
##Add 2 inches to the son's height. And print it.
#Dict2={"son's name": "Lucas", "son's eyes": "green", "son's height": 32, "son's weight": 25}
#
#solution

#Dict2["green", "son's height"]=34
#Dict2["green", "son's height"]=32+2
#print(Dict2)

#Q3
#Using .items() method generate a list of tuples consisted of each key value pair

#solution

#print(Dict2.items())


#Q4
##Using get() method print the value of “son’s eyes”


#solution

#Dict2={"son's name": "Lucas", "son's eyes": "green", "son's height": 32, "son's weight": 25}
#print(Dict2.get("son's eyes"))


#Q5
#Clear the whole dictionary

#solution

#Dict2.clear()
#print(Dict2)





#Activity_2---------------------------------------------------------------------


###Q1...  Given a Python list, Write a program to add all its elements into a given set.
#sample_set = {"Yellow", "Orange", "Black"}
#sample_list=["Blue", "Green", "Red"]
#sample_set_1=list(sample_set)
#sample_set_1.append(sample_list)   
#print(sample_set_1)



##Q2 Create a new set that only contains common items from both sets.
#S1 = {10,20,30,40,50}
#S2 = {30,40,50,60,70}
#S3=S1.intersection(S2)
#print(S3)

##Q3  Update the first set with items that don’t exist in the second set
#set1 = {10, 20, 30} 
#set2 = {20, 40, 50}
#set3=set1.symmetric_difference(set2)
#print(set3)



## Q4 Check if two sets have any elements in common. If yes, display the common elements
#set1 = {10, 20, 30, 40, 50}
#set2 = {60, 70, 80, 90, 10}
#set3=set1.intersection(set2)
#print(set3)


##Q15

#player_data={"Sachin":234,"Dhoni":435,"Virat":500,"Rohit":453}
#name_of_player=input("enter the player name :")
#for name,score in player_data.items():
#    if name_of_player==name:
#        print(score)



#Activity_3--------------------------------------------------------------------


#Q1

#Create below 2 sets and try intersection, union, difference, symmetric_difference()
#Sample input

#set1 = {10, 20, 30, 40, 50}
#set2 = {60, 70, 80, 90, 10}


#set3=set1.intersection(set2)
#print(set3)


#set3=set1.union(set2)
#print(set3)


#set3=set1.difference(set2)
#print(set3)


#set3=set1.symmetric_difference(set2)
#print(set3)


#Q2
#Create an empty dictionary and do following operation on it
#   Add 5 key and values in it
#
#   Accept a key from user and remove that key and values from dictionary
#
#   Accept a key from user and print the value of that key

#Solution

#dict1={"name":"Rhutuja","Sub":"Maths"}
#key=input("enter the key  :")
#if key in dict1:
#    del dict1[key]
#    print(dict1)






#Activity4----------------------------------------------------------------------



#Q1
#Eg: “James” output : “Jms”
#string=input("enter the string :")
#a=int(len(string)/2)
#print(string[0]+string[a]+string[-1])


#Q2
#o/p : AuKellylt
#s1 = "Ault"
#s2 = "Kelly"
#s3=list(s1)
#s3[2:2]=s2
#s4="".join(s3)
#print(s4)


#Q3
##o/p: lcomeWE
#Str1 = "WElcome"
#upperletter=[]
#lowerletter=[]
#for i in Str1:
#    if i.isupper():
#        upperletter.append(i)
#    else:
#        lowerletter.append(i)
#    letter=lowerletter+upperletter
#join_letter="".join(letter)
#print(join_letter)


##Q4
##Str1 = “Apple”
##Op: {‘A”:1,’p’:2,’l’:1,’e’:1}
#
#Str1 = "Apple"
#d={}
#for i in Str1:
#    value=Str1.count(i)
#    d.update({i:value})
##    d[i]=value
#print(d)


##Q5
##str1 = Emma-is-a-data-scientist
##o/p : Displaying each substring
#string="I'm_Rhutuja_Patil"
#a=string.split("_")
#for i in a:
#    print(i)


##exel_sheet_Q_6-------
#
#separater_is_#

#s="I'm#Rhutuja#Patil"
#b=s.split("#")
#l=[]
#for i in b:
#    l.append(i)
#print(l)


#exel_sheet_Q_21------------

##Reverse_order


#l=[3,5,7,1,9]
#print(l[::-1])


##exel_sheet_Q_22-------------
#
##Q.Write aprogram to use the addition operator to:
#
##i) add integers
#
#a=5
#b=2
#print(a+b)

##ii) concatenate string
#
#name="Rhutuja"
#last_name="Patil"
#print(name+last_name)


##iii) on lists to make a single list
#
#list1=[1,2,3]
#list2=[4,5,6]
#print(list1+list2)
    












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
#print((English+Science+Math+History)/4)





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
##a=s.split()
##b=a[::-1]
##j=" ".join(b)
##print(j)
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
#l=[]
#for i in str1:
#    s=str1.split()
#    count=1
#    for j in s:
#        if j=="Sam":
#            count+=1
#print("Sam is occurring :",count,"times")


# s = "Hi how #are you doing"
# a=s.split()
# a.reverse()
# j=" ".join(a)
# print(j)
    

l=[[3,5,6],[7,8,44],[33,1,99]]
l2=[]
for i in l:
    for j in i:
        l2.append(j)
print(max(l2))
print(sum(l2))


# lst = []
 
# num = int(input('How many numbers: '))
 
# for n in range(num):
#     numbers = int(input('Enter number '))
#     lst.append(numbers)
     
# print("Maximum element in the list is :", max(lst))

        