#KINGSLEY_OTTO
#CSI_32_FALL_2015
#1ST_HOMEWORK_GCD


                 #<---------EUCILDEAN ALGORITHM-------------->
# DEFINE FUCTION
#THIS FUCTION TAKES TO INTEGERS
def main():
    print("This program finds the GCD of two integers")
    x = eval(input("Please enter the first number :"))
    y= eval(input("Please enter the second digit :"))
    int(x),int(y)

    u, v = x, y
    

    while v != 0:
        r = u%v
        u = v
        v = r
        print("The GCD of the two numbers is :", u)
    
        
        
 
main()




"""
This program finds the GCD of two integers
Please enter the first number :54
Please enter the second digit :42
The GCD of the two numbers is : 42
The GCD of the two numbers is : 12
The GCD of the two numbers is : 6

"""
