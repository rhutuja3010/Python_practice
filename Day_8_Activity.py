# Date and Time Module


# 1.Write a Python script to display the various Date Time formats -  a) Current date and time
# b) Current year
# c) Month of year
# d) Week number of the year
# e) Weekday of the week
# f) Day of year
# g) Day of the month
# h) Day of week
# Solution: -
import datetime 
# a)
current_date=datetime.datetime.now()
print(current_date)
# b)
date = current_date.date()
year = date.strftime("%Y")
print(f"Current Year -> {year}")
# c) 
month=date.strftime("%B")
print(f"Current Month -> {month}")
# d)
weeknumber_of_theyear=current_date.isocalendar()
print("current week number->",weeknumber_of_theyear)
# e) 
weekday=date.strftime("%A")
print("current week day ->",weekday)
# f) 
print("Weekday of the week: ", date.strftime("%w"))
# g)
print("Day of the month-> ",date.strftime("%d"))

# h) 
print("day of the year->",date.strftime("%j"))



# 2.Write a Python program to determine whether a given year is a leap year
# Solution: -
import calendar
print(calendar.isleap(2009))

# 3.Write a Python program to convert a string to datetime.  Sample String : Jan 1 2014 2:43PM
# Expected Output : 2014-07-01 14:43:00
# Solution: - 
time = input("enter the date and time") 
print(datetime.datetime.strptime(time,"%b %d,%Y %H:%M:%S %p"))

# 4.Write a Python program to get the current time in Python
# Solution: - 
current_time=datetime.datetime.now()
time=current_time.time()
print(time)


# 5.Write a Python program to subtract five days from current date
# Solution:- 
from datetime import date, timedelta
dt = date.today() - timedelta(5)
print('Current Date :',date.today())
print('5 days before Current Date :',dt)

# 6.Write a Python program to print yesterday, today, tomorrow.
# Solution:- 
yesterday=date.today()-timedelta(1)
tomorrow=date.today()+timedelta(1)
print("Yesterday date",yesterday)
print("Today date",date.today())
print("Tomorrow date",tomorrow)


# 7.Write a Python program to add 5 seconds with the current time
# Solution:- 
x= datetime.datetime.now()
y = x + datetime.timedelta(0,5)
print(x.time())
print(y.time()) 


# 8.Write a Python program to add year(s) with a given date and display the new date. 
# Solution:-
import datetime
from dateutil.relativedelta import relativedelta 
y=int(input("enter number of year u want add"))
my_date = datetime.datetime(2024, 11, 6, 14, 36, 56) 
my_date_years = my_date + relativedelta(years = y)
print(my_date_years)



# 9.Write a Python program to get days between two dates. Sample Dates : 2000,2,28, 2001,2,28
# Solution:-  
from datetime import date, datetime
str_d1 = '2021/10/20'
str_d2 = '2022/2/20'
d1 = datetime.strptime(str_d1, "%Y/%m/%d")
d2 = datetime.strptime(str_d2, "%Y/%m/%d")
delta = d2 - d1
print(f'Difference is {delta.days} days')


# 10.Write a Python program to add a month with a specified date
# Solution:-  
from dateutil.relativedelta import relativedelta
my_date = datetime.datetime(2024, 11, 6, 14, 36, 56) 
print(my_date)
my_date_months = my_date + relativedelta(months = 25)
print(my_date_months)


# Extra Questions
# Q1. Write a program to display the next consecutive 10 dates from the current date.
# Solution:-  
for i in range(1,10+1):
    my_date_days = my_date + datetime.timedelta(days = i)
    print(my_date_days)

# Q2. Write a program to accept the date of birth of two persons and find out, who is the 
# older of the two [Hint:Use the datetime module].
# Solution:- 
person1= datetime.date(1993,4,23)
person2 = datetime.date(1994,5,28)

age1 = (date.today()- person1) // datetime.timedelta(days=365.2425)
age2=(date.today()-person2)//datetime.timedelta(days=365.2425)
if age1>age2:
    print("Person1 is older than Person2",age1)
elif age2>age1:
    print("Person 2is older than Person1",age2)
else:
    print("both have same age")


# Q3.Write a program to display a bar graph for two departments in a company, where the 
# employee ids is in the x-axis and their salaries in the y-axis
# Ans:-
import matplotlib.pyplot as plt
salary=[20000,40000,22000,19000,30000]
employee_id1=[416,413,400,423,456]
employee_id2=[321,322,325,327,330]
plt.figure(figsize=(10,10))
plt.bar(employee_id1,salary,color="blue",label="department1")
plt.bar(employee_id2, salary,color="yellow",label="department2")
plt.grid()
plt.legend()
plt.show()


# Q4. Write a program to create a line graph to show the profits of a company for the 
# years 2015, 2016, 2017, 2018, 2019
# Solution: -
x=[2015,2016,2017,2018,2019]
y=[20,50,8,62,75]
plt.figure(figsize = (10,10))
plt.title("A Company profit graph")
plt.plot(x,y,color = "brown",linewidth = 5,marker = 'o',ms = 20,mfc = "blue")
plt.xlabel("Years")
plt.ylabel("profit in billions")
plt.grid(color = "yellow",linewidth =2)
plt.show()

# Q5. Create a program to display a pie chart showing the percentage of employees in 
# different departments of a company
# Solution: -
plt.style.use("ggplot")
percentage_of_employee=[23,55,78,50,88,76]
dept=["Audit","Sales","Training","IT","HR","Adminstrative"]
plt.pie(percentage_of_employee,labels=dept,shadow=True)
plt.legend(loc="best")
plt.show()
