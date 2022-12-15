# # Extra Activity


# # Q1.Write a program to display all the positions of a sub string in a main string
# # Solution: -
# import re
# text = 'Python exercises, PHP exercises, C# exercises'
# pattern = 'exercises'
# for match in re.finditer(pattern, text):
#     s = match.start()
#     e = match.end()
#     print('Found "%s" at %d:%d' % (text[s:e], s, e))


# # Q2.Write a program to know whether a sub string is there in the main string or not. 
# # Solution: -
# MyString1 = "Hii!Welcome to python Learning"
# if "python" in MyString1:
#     print("Yes! it is present in the string")
# else:
#     print("No! it is not present")


# # Q3.Create a dataframe from:
# import pandas as pd

# # a)- CSV file
# # Solution: -
# import pandas as pd
# df = pd.read_csv(r"C:\Users\swati.ah.kumari\Downloads\Data for repository.csv.csv")
# print(df)
# print(type(df))

# # b)- Dictionary
# # Solution: -
# capitals= {"Country":["Afghanistan","USA","India","Russia","France","China","Japan","Netherlands"],"Capital":["Kabul","Washington D.C","New delhi","Moscow","Paris","Beijing","Tokyo","Amsterdam"],"currency":["Afghani","Dollor","Indian_rupee","Ruble","Euro","Chinese_Yuan","Yen","Euro"]}
# df2=pd.DataFrame(capitals,index=["1","2","3","4","5","6","7","8"])
# print(df2)

# # c)Using the dataframe retrieve:
# # the first two rows
# #  the 2nd to 4th row
# # Solution: -
# print(df.iloc[0:2,:])
# print(df.iloc[2:5,:])


# Q4.Write a program to find out how many times a particular element is found in a tuple
# Solution: -
# Tu=(10, 8, 5, 2, 10, 15, 10, 8, 5, 8, 8, 2)
# a=int(input("element occurence check:"))
# count=0
# for i in Tu:
#     if i==a:
#         count+=1
# print(count)




##Q1 find the sum and maximum number

# def operation(mylist):
#     store_element=[]
#     for i in mylist:
#         for j in i:
#             store_element.append(j)
#     print("Maximum Integer Value :",max(store_element))
#     print("Sum of all numbers :",sum(store_element))
# operation([[3,5,6],[7,8,44],[33,1,99]])



# ##Q2 reverse the string

# def doreversed(string):
#     spl=string.split()
#     spl.reverse()
#     j=" ".join(spl)
#     print(j)
# doreversed("My name is Guido Van")



dic = {'python' : 3, 'pool' : 5, 'solution' : 6, 'sid' : 1}
# print("Input dictionary : ",dic)
 
sorted_values = sorted(dic.values()) # Sort the values
sorted_dict = {}
 
for i in sorted_values:
    for k in dic.keys():
        if dic[k] == i:
            sorted_dict[k] = dic[k]
            break
 
print("Sorted dictionary : ",sorted_dict)
