#variables and datatypes:
# #Rules
# ##1.variable name should not be keyword or functions names
# #2. a variable name cannot start with number or special chars
# #3. no space inbetweeen variable name
# #4. case sensitive

# #datatypes: 
# 4 inbuilt datatypes in python
# #1. integer - int----eg:whole numbers 12,33333333,0,-43232#2. 
# #2. floating point integer - float  eg: 34.55678 
# #3. string - str  ----" " / ' ' eg: 'msk','24353',"343.232"
# #4. boolean - bool ---- eg: True/False.
# planet_name = "Mercury"
# planet_dia = 333452
# planet_gravity = 3.456
# planet_has_rings = False
# #print function:----print the value to the console
# #standard and user - defined function:
# #print(planet_name)
# #print(planet_dia)
# #print(planet_gravity)
# #print(planet_has_rings)
# print(planet_name,planet_dia,planet_gravity,planet_has_rings,sep ='\n' )
# name = "bob"
# print("Welcome to python training    ",name)
# print('Welcome to \'python\' training.')
# print("welcome to 'python' training")
# #input ----
# #age = input("Enter your age:")
# #print("your age is",age) 

 
#Type conversion / Type Casting: 
# #print(type(5))
# #print(type(4.5678))
# #print(type(False))
# #print(type("smksfrtf@$3"))
# #a = 5
# #print(type(a))
# age = input("Enter your age: " )
# print(type(age))

# #2 methods
# #implicit type conversion --- automatically
# #explicit type conversion  --- manually

# x = 10
# ##print(x,type(x))
# y = 10.2
# ##print(y,type(y))
# x = x + y
# print(x, type(x))
# #int()
# #int(base)
# #float()
# #str()
# #ord()---- converts a char to integer
# #hex()--- integer to hexadecimal string
# #oct()---- integer to octal string
# #chr()----string to unicode integer
# #a = 5
# #a = float(a)
# ##print(a,type(a))
# #a = 56.095
# #a = int(a)
# #print(a,type(a))
# #a = 556.987
# #a = str(a)
# #print(a,type(a))
# #a = "smsf"
# #a = float(a)
# #print(a,type(a))
# #a = "5.8766"
# #a = int(a)
# #print(a)
# #a = "5"
# #a = float(a)
# #print(a)
# #char to int---- displays the ASCII values


# #operators:#+#-#*#/
# #print(5+6)
# #print(5*6)
# #print(5-6)
# #print(5/6)
# #print(10.4//2)
# #print(10**2)
# ##= --- assignment operator
# #== ----- equivalent opertor
# ##a = 5
# ##print('apple' == 'apple')
# x = 1
# #x = 2 
# # changing the variable value
# ##print(x)
# #x = x + 1
#  # updating the variable value
#x += 1 # shorthand operator
# #x += 3
# #x *= 2
# #x -= 3
# #s = "1001101"
# #s = int(s,10)
# #print(s,type(s))
# c = hex(56) 

# print(c,type(c)) 

#base 2 - normal integer
# #base 10 - binary numbers
# #base 8 - octal numbers
# #base 16 - hexdecimal numbers 
# #s = "10111110000"
# #s = int(s,2)
# #print(s,type(s)) 


# print(help(int))