#MIDTERM
#KINGSLEY OTTO
#SCI 32
#QUESTION 6




class Account:
    def __init__(self, ssn, yearOpened, balance = 0, rate = 2):
        self._id = ssn
        self._balance = balance
        self._rate = rate
        self._year = yearOpened

    def __str__(self):
        str1 = ("Account opened in " + str(self._year) + " has a balance of $")
        str2 = (str(round(self._balance,2)) + ", and your current rate is ")
        str3 = (str(self._rate) + "%")
        return str1 + str2 + str3

    
    def getBalance(self):
        return self._balance
    
    def addToBalance(self,amount):
        if amount < 0:
            print("Warning: you cannot add a negative amount to the account")
        else: self._balance += amount
        
    def updateRate(self,rate):
        self._rate = rate
    
    def getRate(self):
        return self._rate
    
    def getSSN(self):
        return self._id



