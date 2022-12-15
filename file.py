#Text File Handling :
#csv--comma separated values
#excel--table format
#text file
#open()
#write()
#read()
#create()
#syntax:
#    
#open(filename,mode)
#mode
#-r- read -open the file to read. 
#-w- it will open the file to overwrite
#-a- it will add some new data to the file
#-x- it will create a new file.
#-b- binary images
#-t- text
#read
#readline
#readlines
#
#f = open(r"C:\Users\meenakshi.sugumar\OneDrive - Accenture\Desktop\abc1.txt",'r')
#f.close()

#f=open(r"C:\Users\rhutuja.b.patil\Desktop\New_file1.txt","x")

#f=open(r"C:\Users\rhutuja.b.patil\Desktop\New_file1.txt","r")
#print(f.read())
#f.close()

# f=open("file.txt",'x')
# f=open("file.txt","w")
# f.close()


#f=open(r"C:\Users\rhutuja.b.patil\Desktop\New_file1.txt","a")
#f.write("Welcome")
#f.close()


# f=open(r"C:\Users\rhutuja.b.patil\Desktop\New_file1.txt","r")
# print(type(f.read()))




#print(f.read(4))
#print(f.readline())
#print(f.readline())
#print(f.readlines())
#read particular line from the doc
#data = f.readlines()
#print(data[14])
#last five lines of the file
#
#for i in range(1,6):
#    print(data[i*-1])
#Write and append
#f = open(r"C:\Users\meenakshi.sugumar\OneDrive - Accenture\Desktop\abc1.txt",'a')
#f.write("\nHi i am the newly added line")
#f.close()
#how to append in the middle of a file:
#f = open(r"C:\Users\meenakshi.sugumar\OneDrive - Accenture\Desktop\abc1.txt",'r')
#data = f.readlines()
#print(data)
#f.close()
#
#data.insert(7,"Hi I am the newly inserted line\n")
#newdata = "".join(data)
#f = open(r"C:\Users\meenakshi.sugumar\OneDrive - Accenture\Desktop\abc1.txt",'w')
#f.write(newdata)
#f.close()
#f = open(r"C:\Users\meenakshi.sugumar\OneDrive - Accenture\Desktop\msk.txt",'w')
#f.write("Hello All")
#
# import os
# os.remove("Q.txt")
# #os.remove(r"C:\Users\meenakshi.sugumar\OneDrive - Accenture\Documents\Python Scripts\test")
#
#
##remove folder along with file
#
#import shutil
#shutil.rmtree("test")