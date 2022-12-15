#Multithreading:
#threading module ---- inbuilt
#process
#multiprocess-----parallellsim---2 sales person
#thread
#lightweight process
#a smalles executable program in the cpu
#a sub process
#thread life cycle
#thread id
#stack pointer ---memory location
#start
#run
#wait
#dead
#demon --- Unfinished thread
#multithread ---- concurrency----1 sales person(waiting)
#parallellism
#concurrency
#Multithreading in python:
#from threading import Thread
from threading import Thread
from time import sleep
class Hello(Thread):
    def run(self):
        for i in range(5):
            print("Hello")
            sleep(1)
class Hi(Thread):
    def run(self):
        for i in range(5):
            print("Hi")
            sleep(1)
t1 = Hello()
t2 = Hi()
t1.start()
sleep(0.2)
t2.start()