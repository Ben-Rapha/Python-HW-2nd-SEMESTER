# Rational.py

class Rational(object):

    def __init__(self, num = 0, den = 1):

        '''creates a new Rational object
        pre: num and den are integers
        post: creates the Rational object num / den'''

        assert isinstance(num,int) and isinstance(den,int)
        
        self.num = int(num)
        self.den = int(den)

    def simplify(self):
        """ reduces the fraction to lowest terms
        pre: self is a Rational object
        post: returns a new Rational object, a fraction, reduced to lowest terms"""

        d = gcd(self.num,self.den)

        return Rational(int(self.num/d),int(self.den/d))


    def __mul__(self, other):

        '''* operator
        pre: self and other are Rational objects
        post: returns Rational product: self * other'''

        num = int(self.num * other.num)
        den = int(self.den * other.den)
        return Rational(num, den).simplify()

    def __truediv__(self,other):
        """ division operator
        pre: self and other are Rational objects
        post: returns Rational division: self / other"""

        tmp = Rational(other.den,other.num)

        return self.__mul__(tmp).simplify()

    def __add__(self,other):
        """ + operator
        pre: self and other are rational objects
        post: returns Rational sum: self + other """

        num = int(self.num * other.den + other.num * self.den)
        den = int(self.den * other.den)

        return Rational(num,den).simplify()

    def __eq__(self, other):
        """ checks for equivalence of two Rational objects
        pre: self and oother are Rational object
        post: returns True if self and other are equivalent, and false otherwise """

        devisor = self.num / other.num
        if devisor == self.den / other.den:
            return True
        else:
            return False
        
                
    def __str__(self):

        '''return string for printing
        pre: self is Rational object
        post: returns a string representation self'''
        
        return str(self.num) + '/' + str(self.den)

def gcd(n1,n2):
    """ finds the Greatest Common Divisor (GCD) for two integers
    pre: n1 and n2 are integers
    post: returns the GCD of n1 and n2 """

    assert isinstance(n1,int) and isinstance(n2,int)
    
    while True:
    
        u,v = n1,n2

        while v != 0:
            r = u % v
            u = v
            v = r
           
        return u
