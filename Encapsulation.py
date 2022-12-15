##Encapsulation:
#class BankAccount:
#    bank_name = "CCCC"
#    interest_Rate = 8.00
#    def __init__(self,acc_num,acc_name,balance):
#        self.__acc_num = acc_num
#        self.__acc_name = acc_name
#        self.__balance = balance
#    def get_acc_name(self):
#        return self.__acc_name
#    def get_acc_num(self):
#        return self.__acc_num
#    def get_balance(self):
#        return self.__balance
#    def set_balance(self,new_balance):
#        self.__balance = new_balance
#    def add_money(self,deposit_amt):
#        self.__balance += deposit_amt
#        print("The amount is deposited, your new balance is",self.__balance)
#    def withdraw_money(self,withdraw_amt):
#        if withdraw_amt <= self.__balance:
#            self.__balance -= withdraw_amt
#            print("The amount withdrawn, final balance is",self.__balance)
#        else:
#            print("Insufficient balance")
#millionaire = BankAccount(1105,"Jeff",1000000000)
##print(millionaire.acc_name,millionaire.acc_num,millionaire.balance)
##millionaire.add_money(500)
##
##millionaire.withdraw_money(198700000000000)
#millionaire.acc_name = "msk"
##print(millionaire.acc_name,millionaire.acc_num,millionaire.balance) 
##
##millionaire.add_money(12344)
##millionaire.withdraw_money(234567)
##
##print(millionaire.__balance)
##millionaire.__acc_name = "jeff"
##getter and setter methods
##print(millionaire.get_acc_name())
##print(millionaire.get_acc_num())
##print(millionaire.get_balance())
##
##millionaire.set_balance(1000)
##
##print(millionaire.get_balance())




#Create a class mobile with 3 instance variables :brand , model, price
#Create two functions  : call and discount
#Def call (self,mobile_number):
#Print(“calling to “,mobile_number)
#
#Def discount(self,discount_amt)
#Self.price -= discount amt
#
#Print the variable values and run the functions
#Make the variables private. Use get and set functions to change and print 
#the values of private variables

class Mobile:
    def __init__(self,brand,model,price):
        self.__brand=brand
        self.__model=model
        self.__price=price
    def get_brand(self):
        return self.__brand
    def get_model(self):
        return self.__model
    def get_price(self):
        return self.__price
    
    def set_price(self,new_price):
        self.__price=new_price
    def call(self,mobile_number):
        print("calling to ",mobile_number)
    def discount(self,discount_amt):
       self.__price-=discount_amt
       
m1=Mobile("Apple","one_plus",50000)
print(m1.get_brand(),m1.get_model(),m1.get_price())
m1.call("9876543215")
m1.discount(2000)
m1.set_price(60000)
print("After changing the the value :",m1.get_price())




#class Mobile:
#    def __init__(self,brand,model,price):
#        self.__brand=brand
#        self.__model=model
#        self.__price=price
#    def get_brand(self):
#        return self.__brand
#    def get_model(self):
#        return self.__model
#    def get_price(self):
#        return self.__price
#    def set_price(self,new_price):
#        self.__price=new_price
#    def call (self,mobile_number):
#        print("calling to",mobile_number)
#    def discount(self,discount_amt):
#        self.price-=discount_amt
#info=Mobile("vivo","v25",25000)
#print(info.get_brand())
#info.set_price(30000)
#print(info.get_price())






#class Mobile:
#    def __init__(self, brand, model, price):
#        self.__brand = brand
#        self.__model = model
#        self.__price = price
#    def get__brand(self):
#        return self.__brand
#    def get__model(self):
#        return self.__model
#    def get__price(self):
#        return self.__price
#    
#    def set__price(self, new_price):
#        self.__price = new_price
#    
#    def call (self,mobile_number):
#        print("calling to " , mobile_number)
#    def discount(self,discount_amt):
#        self.__price -= discount_amt
#        
#m1 = Mobile("Mi", "M11", 25000)
##print(m1.brand, m1.model, m1.price)
##
##m1.call("8978445678")
##
##m1.discount(2000)
##print(m1.get__price())
#print(m1.get__brand())
#print(m1.get__model())
#print(m1.get__price())
#m1.set__price(35000)
#print("after changing the value of mobile ",m1.get__price())
#       
#
