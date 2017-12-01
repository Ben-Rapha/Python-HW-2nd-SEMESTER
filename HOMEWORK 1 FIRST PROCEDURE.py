#KINGSLEY_OTTO
#CSI_32_FALL_2015
#1ST_HOMEWORK_GCD


                 #<---------FIRST PROCEDURE-------------->
# DEFINE FUCTION
#THIS FUCTION TAKES TO INTEGERS
def main():
    print("This program finds the GCD of two integers")
    x = eval(input("Please enter the first number :"))
    y= eval(input("Please enter the second digit :"))
    int(x),int(y)
    
    
        

# CHOOSE THE SMALLER INTEGER
    if x > y :
        guess = y
    else:
        guess = x            
        
    
# SUBTRACT 1 IF GUESS IS NOT DIVISIBLE BY BOTH X AND Y 
    while x%guess != 0 or y%guess != 0:
            guess -=1
    print("The GCD of the numbers you entered is :",guess)
   
        
    
    
main()


"""
This program finds the GCD of two integers
Please enter the first number :54
Please enter the second digit :42
The GCD of the numbers you entered is : 6
"""
