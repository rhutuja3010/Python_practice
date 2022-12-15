#datetime module:
#import datetime
#print current date and time
#default format of datetime:
#
#YYYY-MM-DD HH:MM:SS --- timestamp
#
#
#HH - 24 HOURS
#datetime.now()
#a = datetime.datetime.now()
#print(a)
#print(a.year)
#print(type(a))
#print(current_date_time)
##print(type(current_date_time))
#
#
#print(current_date_time.year)
#print(current_date_time.month)
#print(current_date_time.day)
#print(current_date_time.hour)
#print(current_date_time.minute)
#print(current_date_time.second)


#timedelta functions:convert from one time zone to another
#IST - Indian Standard Time 
#UTC - 
#
#IST = UTC + 5.30
#PST = UTC - 7.00
#cur_time = datetime.datetime.now()
##print(cur_time)
##
#us_cur_time = cur_time + datetime.timedelta(hours=5 , minutes = 30)
#
#print(us_cur_time)
#

#silicon_valley_time = cur_time - datetime.timedelta(hours=7)
#print(silicon_valley_time)


#datetime.strftime() ---- string format function
#convert datetime objects to string data type 
#
#2020-01-22
#
#01,January 2022
#%a - weekday in short( eg: sun,mon,tue)
#%A - weekday in full(eg: Monday,Tuesday)
#%w - weekday as number(eg: 0 ,1,2,3,4,5,6.0 is sunday  )
#%W -week no
#%d - day of the month( eg: 01 , 02 , to 31)
#%b - month in short form ( eg: jan,feb,mar)
#%B - month in full form ( eg: January)
#%m - month in number (eg: 01,02,...12)
#%y - year in short fomr ( eg: 22,23,24 last two digits)
#%Y - year in full form ( eg: 2022, 2023)
#%H - hour ( 24 hour clock)(eg: 00,01,23)
#%I - hour ( 12 hour clock)(eg: 01,02...12)
#%p - (AM,PM)
#%M - minute(00 ...59)
#%S - (second(00...59))
#%f - microsecond
#convert the current date and time into string. Also print
#date and time in eg: "November 27, 2020 08:20:03 PM"
#cur_time = datetime.datetime.now()
#
#print(cur_time.strftime("%B %d,  %H:%M:%S %p"))


#strptime -- convert str to timestamp
#time = "Sep 11,1993 08:22:13 AM"
#
#
#print(datetime.datetime.strptime(time,"%b %d,%Y %H:%M:%S %p"))
#last_solar_eclipse = "26-Dec-2019 03-34-00 AM"
#
#
##An eclipse will repeat itself in 6585 days:
#last_solar_eclipse_string = "26-Dec-2019 03-34-00 AM"
##print(type(last_solar_eclipse_string))
#last_solar_eclipse_timestamp = datetime.datetime.strptime(last_solar_eclipse_string,"%d-%b-%Y %H-%M-%S %p")
##print(type(last_solar_eclipse_timestamp))
#next_solar_eclipse = last_solar_eclipse_timestamp + datetime.timedelta(days = 6585)
##print(next_solar_eclipse)
#next_solar_eclipse_string = next_solar_eclipse.strftime("%B %d,%Y %H:%M:%S %p")
#print(next_solar_eclipse_string)
#datetime.now()---current time of your system
#datetime.timedelta() --- used to add / subtract time
#strftime - convert timestamp to string
#strptime --- convert string to timestamp
#day
#year
#month
#date
#minute
#hour
#second
#date() and time()
#sweety_birthday = datetime.date(2002,1,3)
#
#print(type(sweety_birthday))
#
#exam_time = datetime.time(hour = 2,minute=30, second = 12)
#print(type(exam_time))




#from dateutil import relativedelta
##calculate days between dates
#d1 = "2021/10/20"
#d2 = "2022/2/20"
###convert string to date object
#d1 = datetime.datetime.strptime(d1,"%Y/%m/%d")
#d2 = datetime.datetime.strptime(d2,"%Y/%m/%d")
##print(d1)
##print(d2)
##
##
#result = relativedelta.relativedelta(d2,d1)#difference between dates in months
#result = result.months + (result.years*12)
##print(result)
#
#result = d2 - d1
#print(result.months)
#
#cur_time = datetime.datetime.now()
#
#print("Day of the week is" , cur_time.weekday())
#import calendar
#yy = 2024
##display the calendar
#print(calendar.calendar(yy))
##print(calendar.isleap(2022))

#import calendar 
#yy=2022
#mm=10
#print(calendar.month(yy,mm))


#Activity_2-------------------------------------------------------
#import datetime


#Q1)Write a Python script to display the various Date Time formats -  
#a) Current date and time
#b) Current year
#c) Month of year
#d) Week number of the year
#e) Weekday of the week
#f) Day of year
#g) Day of the month
#h) Day of week
#import datetime
#curr_date_time=datetime.datetime.now()
#print(curr_date_time)
#print(curr_date_time.year)
#print(curr_date_time.month)
#print(datetime.datetime.now().strftime("%W"))
#print(datetime.datetime.now().strftime("%A"))
#print(datetime.datetime.now().strftime("%Y"))




#print(curr_date_time.year)

#Q2)Write a Python program to determine whether a given year is a leap year
#import calendar
#
#x=int(input("enter the year :"))
#print(calendar.isleap(x))


###Q3)Write a Python program to convert a string to datetime.
##Sample String:Jan 1 2014 2:43PM
##Expected Output : 2014-07-01 14:43:00
#import datetime
#time = "Jul 01,2014 2:43:00 PM"
#print(datetime.datetime.strptime(time,"%b %d,%Y %I:%M:%S %p"))

#from datetime import timedelta,date
#import datetime
####Q4)Write a Python program to get the current time in Python
###
##curr_date_time=datetime.datetime.now()
###print(curr_date_time.time())
##
###Q5)Write a Python program to subtract five days from current date
#curr_date=datetime.datetime.now()
##CURR_DATE=curr_date.today()
#after_five_days_date=timedelta(days=5)
##print(curr_date.date())
#
#print(curr_date-after_five_days_date)


from datetime import timedelta,date
#Q6)Write a Python program to print yesterday, today, tomorrow.

#today=datetime.datetime.now()
#print(today)

#tomarro=timedelta(days=1)
#print(today+tomarro)

#yesterday=timedelta(days=1)
#print(today-yesterday)

#Q7)Write a Python program to add 5 seconds with the current time


#Q8)Write a Python program to add year(s) with a given date and display the new date.

 
#Q9)Write a Python program to get days between two dates. Sample Dates : 2000,2,28, 2001,2,28


#Q10)Write a Python program to add a month with a specified date.


#Q27_Excel_sheet
#Write a program to display the next consecutive 10 dates from the current date


#Q28
#Write a program to accept the date of birth of two persons and find out,
# who is the older of the two [Hint:Use the datetime module]



##Q23
#Write a program to display a bar graph for two departments in a company, where
#the employee ids is in the x-axis and their salaries in the y-axis
##Q24
#Write a program to create a line graph to show the profits of a company for the
#years 2015, 2016, 2017, 2018, 2019
#
##Q25
#Create a program to display a pie chart showing the percentage of employees in 
#different departments of a company


#some_string = “Python”
#a, b, c, d = some_string

#city = ‘Los Angeles’
#city.find(‘x’)
#print(city)