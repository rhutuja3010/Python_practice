###Q1
##
###dic={101:"Max",102:"Sunil",103:"David",104:"JD"}
##
##Take emppty dictionary
dic={}
dic[101]="Max"
dic[102]="Sunil"
dic[103]="David"
dic[104]="JD"

#console the dictionary 
#print("Created Dictionary :",dic)

#store keys in list
keys_list=[]
for i in dic.keys():
    keys_list.append(i) 
    s=sum(keys_list) #using sum function sum of all key
print("The sum of all key is",s)



###Q2 #Highest to lower the list
#
myList=[100,500,300,400]
#myList=[4,7,1,9,2]

#Using sorted() sort the list
sort_list=sorted(myList)
#
##Using slicing reverse the sort_list 
store_list=sort_list[::-1]
print("Sorting list on higher to lower:",store_list)
#
###other method
#
##Using  reverse() reverse the sort_list 
sort_list.reverse()
print("Sorting list on higher to lower:",sort_list)

