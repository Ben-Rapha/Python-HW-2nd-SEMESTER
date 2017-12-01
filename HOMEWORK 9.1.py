#KINGSEY OTTO
#CSI 32
#HOME WORK 9.1



class Sneetch:
    def __init__(self):
        self._a = 3
        self._b = 4
        
    def x(self):
        print(self._a)

    def y(self):
        print(self._b)

class StarBellySneetch(Sneetch):
    def __init__(self):
        Sneetch.__init__(self)
        self._b = 7
        self._c = 8

    def y(self):
        print(self._b,self._c)

    def z(self):
        print(self._a,self._c)


def main():
    
    alice = Sneetch()
    bob = StarBellySneetch()
    alice.x()
    alice.y()
    #alice.z() <----- raises an attribute error
    bob.x()
    bob.y()
    bob.z()

main()

#THIS IS THE OUTCOME WHEN I RUNNED THE PROGRAM WITH THE EXECEPTION OF
# "alice .z()" WHICH RAISED AN ATTRIBUTE ERROR BECAUSE "Sneecth" DOESN'T
#SUPPORT THE METHOD Z
""""

3
4
3
7 8
3 8
"""
