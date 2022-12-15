#Lists
#
#Data Structures:
#collections:
#storing multiple values in single variable
#4 inbuilt collextions:
#1. list
#2. tuples
#3. set
#4. dictionary
#common activity:
#thislist = ["apple", "banana", "cherry"]
#mylist = thislist
#print(mylist)

#create 
#add items
#replace
#remove 
#access
#delete
#List:
#used to store multiple values in single variable
#one of 4 inbuilt data structure
#heterogeneous---allows all datatypes in single 
#ordered
#changeable
#allow duplicates
#mutable
#follows indexing
#[]
# list1 = ["Mercury",3456,34.4664,False,3456]
# list1.append(1)
# print(list1)
#print(list1[0])
#print(list1[1])
#print(list1[2])
#print(list1[3])
#print(list1[4])
#for i in list1:
#    print(i)
#len() -- length function:
#print(len(list1))
#
#n  = len(list1)
#
#for i in range(5):
#    print(i,list1[i])
# l=[{2:5},3]
# b=2
# l.append(b)
# print(l)
#
#in / not in
# fruits = ["apple","banana","cherry","dates","mango","kiwi","orange","pomo"]
#print(fruits)
#print(len(fruits))
# print(type(fruits))
#print(fruits[2])
# print("apple" in fruits)
# index:
# print(fruits.index("kiwi") )
# add items to the list
#append---add item to the last
#insert --- add item anywhere
#fruits.append("papaya")
#
#print(fruits)
#
#fruits.insert(2,"strawberry")
#print(fruits)
#replace
#
#fruits[2] = "papaya"
# fruits=[7,5,2,0,1,8,2,9,4,7,3]
# print(len(fruits))
#print(fruits)
#slicing:
#print(fruits[1:5])
#print(fruits[3:6])
# print(fruits[:6])
# print(fruits[4:])
# print(fruits[2:7:2])
# print(fruits[::1])
# print(fruits[::-2])
# print(fruits[::-1])
# print(fruits[:])
#remove
#remove ---- remove by item name
#pop ---- remove by index number
#fruits.remove("orange")
# fruits.remove(5)
# print(fruits)
# fruits.pop(3)
# print(fruits)
#
# fruits.pop()
# print(fruits)
#
# fruits=[7,5,2,0,1,8,2,9,4,7,3]
# fruits.pop(3)
# print(fruits)
# del fruits[3]
# print(fruits)
# fruits.clear()
# print(fruits)
#
# del fruits
# print(fruits)


#no=[1,2,3,4,5,6,7,8,9,10]
#for i in no:
#    print(i)

#list=["dog","cat","monkey","bear","deer","pig","goat"]
#print(list[::-1])

#list=[1,2,3,4,5]
#list.insert(2,"ram")
#print(list)


#list1=[5,4,3,20,10,89,77]
#for i in range(len(list1)):
#    if list1[i]==20:
#        list1[i]=200
#print(list1)





# n_list = ["Happy", [2, 0, 1, 5]]
# print(n_list[0][1])


# my_list = ['p', 'r', 'o', 'b', 'e']
# print(my_list[4.0])

# Demonstration of list insert() method
# odd = [1,9,8,0,2]
# odd.insert(1,3)

# print(odd)

# odd[3:5] = [5,7]

# print(odd)





# Deleting list items
my_list = ['p', 'r', 'o', 'b', 'l', 'e', 'm']

# delete one item
# del my_list[2]

# print(my_list)

# # delete multiple items
# del my_list[1:5]

# print(my_list)

# # delete the entire list
# del my_list

# # Error: List not defined
# print(my_list)



# my_list = ['p','r','o','b','l','e','m']
# my_list.remove('p')

# Output: ['r', 'o', 'b', 'l', 'e', 'm']
# print(my_list)

# # Output: 'o'
# print(my_list.pop(1))


# # Output: ['r', 'b', 'l', 'e', 'm']
# print(my_list)

# # Output: 'm'
# print(my_list.pop())

# my_list.pop()
# print(my_list)

# # Output: ['r', 'b', 'l', 'e']
# print(my_list)

# my_list.clear()

# # Output: []
# print(my_list)




# my_list = ['p','r','o','b','l','e','m']
# my_list[2:3] = []
# print(my_list)
# ['p', 'r', 'b', 'l', 'e', 'm']
# my_list[2:5] = []
# print(my_list)
# ['p', 'r', 'm']



# pow2 = [2 ** x for x in range(10)]
# print(pow2)


# pow2 = [2 ** x for x in range(10) if x > 5]
# print(pow2)
# [64, 128, 256, 512]
# odd = [x for x in range(20) if x % 2 == 1]
# print(odd)
# print(1%2)
# [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
# print([x+y for x in ['Python ','C '] for y in ['Language','Programming']])
# ['Python Language', 'Python Programming', 'C Language', 'C Programming']

# a=[x+y for x in ['Python','C '] for y in ['Language','Programming']]
# print(a)




# print([a+b for a in ["Me ","she "] for b in ["Rhutuja","friend"]] )


# for fruit in ['apple','banana','mango']:
#     print("I like",fruit)



# Python program to demonstrate
# Creation of List
 
# # Creating a List
# List = []
# print("Blank List: ")
# print(List)
 
# # Creating a List of numbers
# List = [10, 20, 14]
# print("\nList of numbers: ")
# print(List)
 
# # Creating a List of strings and accessing
# # using index
# List = ["Geeks", "For", "Geeks"]
# print("\nList Items: ")
# print(List[0])
# print(List[2])



# Creating a Multi-Dimensional List
# (By Nesting a list inside a List)
# List = [['Geeks', 'For'], ['Geeks']]

# accessing an element from the
# Multi-Dimensional List using
# index number
# print("Accessing a element from a Multi-Dimensional list")
# print(List[0][1][1])
# print(List[1][0])


# # input size of the list
# n = int(input("Enter the size of list : "))
# # store integers in a list using map,
# # split and strip functions
# lst = list(map(int, input("Enter the integer\elements:").strip().split()))[:n]

# # printing the list
# print('The list is:', lst)


# a=[3,1,5,7,8]
# a.sort()
# print(a)
# a.reverse()
# print(a)

