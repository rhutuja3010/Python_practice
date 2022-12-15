#matplotlib.pyplot as plt
#
import matplotlib.pyplot as plt
#print(plt.style.available)
##lineplot
##bar plot
##scatter plot
##pie chart
##line plot
#plt.style.use("dark_background")
#x = [2,3,4,5,6]
#y = [44,55,66,22,11]
#plt.figure(figsize = (10,10))
#plt.title("A simple graph")
#plt.plot(x,y,color = "brown",linewidth = 5,marker = 'o',ms = 20,mfc = "blue")
#plt.xlabel("Temperature")
#plt.ylabel("sensor")
#plt.grid(color = "yellow",linewidth = 2)
#plt.show()
#days = [1,2,3,4,5]
#enfield = [50,40,70,80,20]
#honda = [80,20,20,50,60]
#yamaha = [70,20,60,40,60]
#ktm = [80,20,20,50,60]
#plt.figure(figsize = (10,10))
##plt.plot(days,enfield,linewidth=2,color ="yellow",label="enfield")
##plt.plot(days,honda,linewidth=2,color ="orange",label="honda")
##plt.plot(days,yamaha,linewidth=2,color ="pink",label="yamaha")
##plt.plot(days,ktm,linewidth=2,color ="white",label="ktm")
#plt.scatter(days,enfield,marker='*',s = 50)
#plt.title("bike details ")
#plt.xlabel("kms")
#plt.ylabel("Days")
#plt.legend()
#plt.show()
#Bar chart
#
#year = [2022,2023,2019,2020]
#sales = [300,400,500,200]
#plt.figure(figsize=(10,10))
#plt.bar(x,y)
#plt.show()
#data = [23,45,56,78,213]
#data1 = [33,44,55,66,77]
#x = [1,2,3,4,5]
#l2 = ["blue","brown",'yellow',"red","orange"]
#l1 = ["apple","banana","cherry","dates","figs"]
#plt.figure(figsize=(10,10))
#plt.bar(x,data,color="blue",label="data1")
#plt.bar(x,data1,color="yellow",label="data2")
#plt.grid()
#plt.legend()
#plt.show()
#pie chart
#plt.style.use("ggplot")
#fruits = [23,44,55,66,80]
#l2 = [0,0.30,0,0.5,0]
#l1 = ["apple","banana","dates","plum","cherry"]
#plt.pie(fruits,labels=l1,explode=l2,shadow = True,autopct = "%1.0f%%")
#plt.legend(loc = "best")
#plt.show()