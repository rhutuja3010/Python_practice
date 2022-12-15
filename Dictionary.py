#-------------------------------------------------------------------------
#Dictionary:
#key:value pairs
#unordered *
#changeable
#duplicates----keys doenst allow duplicates, but values can be duplicates
#{}
#d1 = {}
#print(d1,type(d1))
#d1 = {"empname":"msk","age":22,"city":"aaa","active":False}
#
#keys----string,float,int,bool,tuple
#keys are immutable
#
#
#values - anything can be a value
#d1 = {"brand":"Ford","model":["hyundai","Maruti"],"age":{"one":1,"two":2}}
#
#print(d1)
#print(d1)


#access values:
#1. square bracket method
#2. get method
#
#print(d1["brand"])
#print(d1.get("active"))
#keys , values, items
#
#print(d1.keys())
#print(d1.values())
#print(d1.items())
#for i in d1.items():
#    print(i)
#
#for i in d1.keys():
#    print(d1[i])
#add an item
#
#d1["fruits"] = "orange"
#print(d1)
#
#d1["age"] = 44
#print(d1)
##
#del d1["active"]
#print(d1)
#d1["dept"] = "aaa"
#print(d1)
#d1["color"] = "orange"
#
#print(d1)
#update
#cars_dict = {"Ford":["Figo","Ecosport"],
#            "Honda":"city",
#            "Hyundai":["Verna","creta"]}
#supercars = {"Ford":"MustangGT",
#             "Lamborghini":"Elemento",
#             "Bugatti":"Veyron"}
#update
#cars_dict.update(supercars)     
#
#print(cars_dict)


#d={"a":1,"b":2,"c":3,"d":4,"e":5}

#delete 
#del d["a"]
#print(d)

##add
#d["f"]=6
#print(d)


#print(d.keys())
#print(d.values())



#Activity_1---------------------

#Q1
#Dict1={"name": "Plato", "country": "Ancient Greece", "born": -427, "teacher": "Socrates", "student": "Aristotle"}
#Print the year that Plato born.
#Change the year from -427 to 428

#Solution
#print(Dict1["born"])
#print(Dict1.get("born"))
#Dict1["born"]=428
#print(Dict1)


#Q2
#“work”:[“Apology”,”Phaedo”,”Republic”,”Symposium”] 
#add this as new key pair in the above dictionary

#solution

#Dict1["work"]=["Apology","Phaedo","Republic","Symposium"] 
#print(Dict1)



#Q3
##Add 2 inches to the son's height. And print it.
#Dict2={"son's name": "Lucas", "son's eyes": "green", "son's height": 32, "son's weight": 25}
#
#solution

#Dict2["green", "son's height"]=34
#Dict2["green", "son's height"]=32+2
#print(Dict2)


#Using .items() method generate a list of tuples consisted of each key value pair
#print(Dict2.items())

#solution

##Using get() method print the value of “son’s eyes”
#
#Dict2={"son's name": "Lucas", "son's eyes": "green", "son's height": 32, "son's weight": 25}
#print(Dict2.get("son's eyes"))
#Clear the whole dictionary

#Dict2.clear()


#print(Dict2)


