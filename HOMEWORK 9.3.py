#KINGSEY OTTO
#CSI 32
#HOME WORK 9.2

#This program has ﬁve distinct errors in its syntax and usage.
#Identify each of those errors.


class MyClass:
    def __init__(self):
        self._x = 1
        

    def increase(self):
        self._x += 1
        
class MyOtherClass(class MyClass):#<-- WRONG SYNTAX
class MyOtherClass(MyClass): #<-- CORRECT SYNTAX
    def __init__(self,z):#<---WRONG SYNTAX
    def __init__(self,z=0):#<---CORRECT SYNTAX Z NEEDS A VALUE 
        MyClass.__init__()#<--- WRONG SYNTAX
        MyClass.__init__(self)#<--- CORRECT SYNTAX
        self._x = z

    def decrease(self):
        self._x -=1


    
a = MyClass()
b = MyOtherClass()
b.increase()
a.decrease()#<-- WRONG SYNTAX MyClass DONT HAVE THE FUNTION DECRESE
b.decrease()#<--- CORRECT SYNTAX SINCE IT HAS THE SYNTAX DECREASE


