#########Dictionary

# Dict1={"name":"Plato","country":"Ancient Greece","born":-427,"teacher":"Socrates","student":"Aristotle"}
# 1.Print the year that Plato born.
# Solution: -
# print(Dict1.get("born"))

# d={"a":1,"b":2,"c":3,"d":4}
# d["a"]=d["a"]+2
# print(d)
# del d["a"]
# print(d)
# store=d["b"]
# print(store)

# d.update({"work":["Apology","Phaedo","Republic","Symposium"]})
# print(d)



# # 2. Change the year from -427 to 428 :
# # Solution: -
# Dict1["born"]=428
# print(Dict1)

# # 3. “work”:[“Apology”,”Phaedo”,”Republic”,”Symposium”] . add this as new key pair in 
# # the above dictionary.
# # Solution: -
# Dict1["Apology"]="Phaedo"
# Dict1["Republic"]="Symposium"
# print(Dict1)

# d.update({"work":["Apology","Phaedo","Republic","Symposium"]})
# print(d)


# Dict2={"son's name": "Lucas", "son's eyes": "green", "son's height": 32, "son's weight": 25}

# # 1. Add 2 inches to the son's height. And print it.
# # Solution: -
# Dict2["son's height"]=Dict2["son's height"]+2
# print(Dict2)


# # 2.Using .items() method generate a list of tuples consisted of each key value pair
# # Solution: -
# for i in Dict2.items():
#     print(i)
# d={"a":1,"b":2,"c":3,"d":4}
# for i in d.items():
#     print(i)

# # 3. Using get() method print the value of “son’s eyes”.
# # Solution: - 
# print(Dict2.get("son's eyes"))
# 
# d={"a":1,"b":2,"c":3,"d":4} 
# s=d['a']
# print(s)
# s=d.get("a")    
# print(s) 
# d.clear()
# print(d) 


# # 4. Clear the whole dictionary.
# Dict2.clear()
# print(Dict2)

##5.Write a program to create a dictionary with cricket players names and their scores in a 
##match.Ask the user to enter the name of a player and return the runs scored by the player.
# # Solution: -
# cricket={"Virat":289,"Hardik":300,"Rohit":100,"Rahul":200}
# n=input("Enter the name:")
# for i in cricket:
#     if n==i:
#         print(cricket[i])
    # print(cricket[i])
# for i in cricket.keys():
#     if n==i:
#         print(cricket[i])

##Sets
# # 1.Given a Python list, Write a program to add all its elements into a given set.
# # Solution: -
# sample_set = {"Yellow", "Orange","Red", "Black"}
# sample_list = ["Blue", "Green", "Red"]
# new_set=sample_set.union(sample_list)
# print(new_set)

# # 2. Create a new set that only contains common items from both sets.
# S1 = {10,20,30,40,50}
# S2 = {30,40,50,60,70}
# # Solution: -
# S3=S1.intersection(S2)
# print(S3)

# # 3. Update the first set with items that don’t exist in the second set
# # Solution: -
# set1 = {10, 20, 30} 
# set2 = {20, 40, 50}
# set3=set1.symmetric_difference(set2)
# print(set3)

# # 4. Check if two sets have any elements in common. If yes, display the common elements
# set1 = {10, 20, 30, 40, 50}
# set2 = {60, 70, 80, 90, 10}
# # Solution: -
# s3=set1.intersection(set2)
# print("The common element is",s3)

# # 5.Write a program to find out how many times a particular element is found in a tuple.
# # Solution: -
# a=(1,2,4,5,3,2,4,2,3,1)
# print(a.count(2))

# a=(1,2,3,2,1,2)
# c=a.count(2)
# print(c)

# # 6. Create below 2 sets and try intersection, union, difference, symmetric_difference()
# # Sample input
# set1 = {10, 20, 30, 40, 50}
# set2 = {60, 70, 80, 90, 10}
# set3=set1.symmetric_difference(set2)
# print(set3)
# set4=set1.intersection(set2)
# print(set4)
# set5=set1.union(set2)
# print(set5)

# # 7.Create an empty dictionary and do following operation on it
# # Add 5 key and values in it
# # Accept a key from user and remove that key and values from dictionary
# # Accept a key from user and print the value of that key
# # Accept all key and values from the dictionary  
# # Solution: -
# a={}
# a["Maths"]=88
# a["English"]=66
# a["Biology"]=99
# a["Physics"]=77
# # print(a)
# b=input("Enter the key:")
# c={}
# if b in a.keys():
#     del a[b]
# print(a)


# n=input("Enter the key:")
# for i in a.keys():
#     if n==i:
#         print(a[i])



# # Strings
# # 1. Write a program to create a new string made of an input string’s first, middle,
# #  and last character.
# # Eg: “James” output : “Jms”
# # · Hint: String index always starts with 0
# # · Use string indexing to get the character present at the given index
# # · Get the index of the middle character by dividing string length by 2
# # Solution: -
# n=str(input("Enter the name:"))
# c=int(len(n)/2)
# d=n[0]+n[c]+n[-1]
# print(d)

# # 2. Given two strings, s1 and s2. Write a program to create a new string s3 by 
# # appending s2 in the middle of s1.
# # s1 = "Ault"
# # s2 = "Kelly"
# # o/p : AuKellylt
# # Solution:  -
# s1="Ault"
# s2="Kelly"
# s3=list(s1)
# print(s3)
# s3[2:2]=s2
# print(s3)
# s4="".join(s3)
# print(s4)

# # 3. Given string contains a combination of the lower and upper case letters. Write a program
# #  to arrange the characters of a string so that all lowercase letters should come first.
# # Str1 = "WElcome"
# # o/p: lcomeWE
# # Solution: -
# Str1 = "WElcome"
# b=[]
# c=[]
# for i in Str1:
#     if i.islower():
#         b.append(i)
#     else:
#         c.append(i)
#     d=b+c
# e="".join(d)
# print(e)

# # 4. Write a program to count occurrences of all characters within a string
# # Str1 = "Apple"
# # Op: {‘A”:1,’p’:2,’l’:1,’e’:1}
# # Solution: -
# Str1 = "Apple"
# for i in Str1:
#     c[i]=Str1.count(i)
# print(c)

# # 5. Write a program to split a given string on hyphens and display each substring.
# # str1 = Emma-is-a-data-scientist
# # o/p : Displaying each substring
# # Solution: -
# str1 = 'Emma-is-a-data-scientist'
# str2=str1.split('-')
# for i in str2:
#     print(i)

# # Extra Activity
# # 1.Write a Python program to display the elements of a list in a reverse order.

# # Solution: -

# a=[1,4,7,3,9]
# print(a[::-1])


# # 2. Accept a string with "#" as a separator. Use the spilt method to display the strings 
# # in a list
# # Solution: -
# n=input("Enter any string:")
# c=n.split('#')
# for i in c:
#     print(i)



# # 3. Write a program to use the addition operator to:
# # - add integers
# # - concatenate strings
# # - on lists to make a single list
# # Solution: -
# # -Add the integers
# a=int(input("Enter the number:"))
# b=int(input("Enter the number:"))
# print(a+b)

# # -Concatenate Strings
# a=str(input("Enter the first name:"))
# b=str(input("Enter the last name:"))
# print(a+b)

# # -on lists to make a single list
# a=["monkey","mouse","cat"]
# b=[1,"2",3]
# print(a+b)
