#-------------------------------------------------------------------------
#Set :
#unordered
#unindexed
#u cant replace items but you can add new items ,remove items
#{}
#heterogeneous
#doesnt allow duplicates
#empty set 
#s1 = set()
#print(s1,type(s1))
#
#s1 = {"apple","banana","orange",333,45.77,"banana"}
#print(s1)
#print(len(s1))
#print(type(s1))
#for i in s1:
#    print(i)
#add item to a set
#
#s1.add("pomo")
##print(s1)
#
##remove items from set
#
##remove
##discard
#
#s1.remove("apples")
#print(s1)
#
#s1.discard("apples")
#print(s1)
#s1 = {22,33,44,56,66}
##
#if 45 in s1:
#    s1.remove(45)
#else:
#    print("45 doesnt exist in the set")
#    
#print(s1)
#
#s1.discard(45)
#print(s1)
#work with duplicates
#1.update
#2. union
#3.intersection_update---keep only the duplicates
#4. intersection
#5. symmetric_difference_update
#6. symmetric_difference
# s1 = {"abc",40,True,34,"male"}
#
# s2 = {"apple",40,"male","dates"}
#
#s1.update(s2)
#print(s1)
#
# s3 = s1.union(s2)
##
# print(s3)
##
#s1 = {22,33,44}
#s2 = {11,22,33}
#
#s1.update(s2)
#
#s3 = s1.union(s2)
#
#print(s1)
#print(s2)
#print(s3)
#
# s1 = {"apple","banana","dates"}
# s2 = {"microsoft","goolge","apple"}

# s1.intersection_update(s2)
# print(s1)
#s3 = s1.intersection(s2)
#print(s3)
#combine the sets
#
#union - remove the duplicates and join the set
#intersection-----keep only the duplicates
# symmetric_difference---keep only items that are not duplicate
s1 = {22,66,77}
s2 = {11,15,77}
# s3 = s1.union(s2)
#s1.intersection_update(s2)
#print(s1)
# s1.symmetric_difference_update(s2)
# print(s1)
#s3=s1.symmetric_difference(s2)
# print(s3)



#Activity_2---------------------------------------------------------------------


###Q1...  Given a Python list, Write a program to add all its elements into a given set.
#sample_set = {"Yellow", "Orange", "Black"}
#sample_set.add("White")
#print(sample_set)
##(o/p)sample_list = ["Blue", "Green", "Red"]
#print(list(sample_set))

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



#cricket_players = {
#
#    "Dhoni":256,
#
#    "Virat":434,
#
#    "Sachin":747,
#
#    "Rohit":736,
#
#    "Rishabh":283
#
#}
#
#
#
#User = input("Enter Player's name:- ")
#
#print(User)


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


#name = "msk"
#age = 23
#print(f"your name is {name} and your age is {age}")



# s1 = {"apple","banana","dates"}
# s2 = {"microsoft","goolge","apple"}

# s1.update(s2)
# print(s1)
# s2.union(s1)
# print(s2)

