#polymorphism: - greek word
#
#poly  ---- many/ multiple
#
#morph --- forms/ shapes 
#
#
#one thing can take multiple shapes or forms
#
#Water: 
#operator overloading
#method overloading
#method overriding


#operator overloading
#
#print(5+6)
#
#print("5"+"6")
#
#print([1,2,4]+[5,6,7])
#Magic methods: __ __, __init__, __dict__
#+ __add__()
#a + b
#
#+ is operator
#a,b is called as operands
#print(type(5))
#print(5+6)
#print(int.__add__(5,6))
#
#
#print("5"+"6")
#
#print(str.__add__('5','6'))
#
#
#print(list.__add__([1,2,3],[5,6,7]))
#operator overloading example
class Student:
    def __init__(self,m1,m2):
        self.m1 = m1
        self.m2 = m2
    def __add__(s1,s2):
        final_m1 = s1.m1 + s2.m1
        final_m2 = s1.m2 + s2.m2
        object1 = Student(final_m1,final_m2)
        return object1
s1 = Student(66,88)
s2 = Student(77,84)
s4 = s1 + s2
print(s4.m1,s4.m2)
print(type(s4))


#magic_method