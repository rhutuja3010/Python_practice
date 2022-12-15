#Pandas : 
#pandas library:
#    
##data analytics
##data statistics
##AI & ML
#    
#2 different types of data structure:
#    
#    1. Pandas Series --- 1D dimension
#    2. pandas  DataFrame --- 2D 
#pandas series
#
import pandas as pd
#empty panda series
l1 = [2,3,4,6,7,8,0]
s1 = pd.Series(l1)
#print(s1)
#print(type(s1))
##
#t1 = tuple(l1)
#print(t1)
#print(type(t1))
##
#type()
#dtype keyword
#l1 = [2,3,4,6,7,8]
#
#d1 = {"name":"msk","age":22,"city":"aa"}
#
#s1 = pd.Series(d1)
#
#print(s1)
#t1 = (3,44,55,66,88,99,9900,3,3,3,3,3,99)
#s3 = pd.Series(t1)
#print(s3)
#print(s3+2)
#for i in s3:
#    for j in range(10):
##        print(j)
#        s3 = s3+j
##        
#print(s3)
##
##print(s3.count())
#
#print(s3.value_counts())
#print(s3)
#
#print(s3.max())
#print(s3.min())
##
#print(s3.mean())#average
#del s3
#print(s3)
#panda series is immutable:
#
#print(s3[4])
#
#print(s3[2:5])




#Pandas DataFrame
import pandas as pd
#
#df = pd.DataFrame(index = [1,2,3,4,5],columns = ["Name","Age","City"])
#
#print(df)


#from list
#
#l1 = [33,44,55,66,77,88,44]

#df = pd.DataFrame(l1,columns = ["marks"],index =["eng","tamil","physics","maths","science","chemistry","java"])
#
#print(df)


#from dictionary

#d1 = {"name":["msk","lily","bob","parr"],
#      "age":[22,33,44,23],
#"city":["aaa","bbb","ccc","ddd"]}
#
#df = pd.DataFrame(d1,index = ["A","B","C","D"])
##
#print(df)


#read_csv =---- csv file to dataframe
#read_excel --- excel file to dataframe
#convert excel to df
#import pandas as pd
df = pd.read_csv(r"C:\Users\rhutuja.b.patil\Downloads\Sample100 (1).csv")
print(df)
#
#print(type(df))
#head and Tail function:
#
#print(df.head(6))
#
#print(df.tail(2))


#indexing and slicing:

#how to select one particulat column or row from the df:
#print(df)
#select one column: syntax: df[column name]
#print(type(df["Leave"]))
#print(df["Leave"])
#
#df1 = pd.read_csv("sample2.csv")
#
#print(df1.tail())
#print(df["Age"])
#loc----using column names & iloc ---column index

#print(df.loc[3:6,["Leave"]])
#print(df.iloc[3:6,1:3])
#filtering :
#print(df)
#syntax: df[condition]
#print(df[df["Dept"]=="IT"])
#print(df[df['Leave']==2])
#
#print(df[df["Dept"] == "HR"])
#print(df[df["Age"]>25])
#syntax: df[()&()]
#print(df[(df["Dept"]=="IT") | (df["Age"]>25)])
#
#print(df[(df["Dept"]=="IT") & (df["Age"]>25)])
#print(~(df[df["Dept"]=="IT"]))