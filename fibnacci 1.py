#KINGSLEY OTTO
#CSI 33
#HOMEWORK 10
#Modify the recursive Fibonacci program given in the chapter so that it prints
#tracing information. Specifically, have the function print a message when it is
#called and when it returns. For example, the output should contain lines like
#these:
#Comput ing f ib (4)
#Leaving f ib (4) returning 3
#Use your modified version of f ib to compute f ib ( 10 ) and count how many
#times f ib ( 3 ) is computed in the process.

numberOfThrees = 0

def recFib (n) :
    global numberOfThrees
    print ("computing.."+ "Fib("+ str(n)+")")
    print("... ")
    if n is 3:
        numberOfThrees +=1
    if n < 3 :
        #time.sleep(2)
        print('Leaving ...'+"Fib("+ str(n)+")" + "returning..." + str(1)+ "\n")
        return 1
    else :
        #time.sleep(1)
        
        print("Leaving... "+ "Fib("+ str(n)+")")#+ "returning..." + str( (recFib (n- 1) + recFib (n-2)))+ "\n")
        n = (recFib (n- 1) + recFib (n-2))
        print("returning..." + str(n))
        return n
    

def main():
    r = eval(input("Please enter a number you wish to find its Fibonacci: ",))
    recFib(r)
    print("The number of threes (3) is: ", numberOfThrees)
    
main()

"""
Please enter a number you wish to find its Fibonacci: 10
computing..Fib(10)
... 
Leaving... Fib(10)
computing..Fib(9)
... 
Leaving... Fib(9)
computing..Fib(8)
... 
Leaving... Fib(8)
computing..Fib(7)
... 
Leaving... Fib(7)
computing..Fib(6)
... 
Leaving... Fib(6)
computing..Fib(5)
... 
Leaving... Fib(5)
computing..Fib(4)
... 
Leaving... Fib(4)
computing..Fib(3)
... 
Leaving... Fib(3)
computing..Fib(2)
... 
Leaving ...Fib(2)returning...1

computing..Fib(1)
... 
Leaving ...Fib(1)returning...1

returning...2
computing..Fib(2)
... 
Leaving ...Fib(2)returning...1

returning...3
computing..Fib(3)
... 
Leaving... Fib(3)
computing..Fib(2)
... 
Leaving ...Fib(2)returning...1

computing..Fib(1)
... 
Leaving ...Fib(1)returning...1

returning...2
returning...5
computing..Fib(4)
... 
Leaving... Fib(4)
computing..Fib(3)
... 
Leaving... Fib(3)
computing..Fib(2)
... 
Leaving ...Fib(2)returning...1

computing..Fib(1)
... 
Leaving ...Fib(1)returning...1

returning...2
computing..Fib(2)
... 
Leaving ...Fib(2)returning...1

returning...3
returning...8
computing..Fib(5)
... 
Leaving... Fib(5)
computing..Fib(4)
... 
Leaving... Fib(4)
computing..Fib(3)
... 
Leaving... Fib(3)
computing..Fib(2)
... 
Leaving ...Fib(2)returning...1

computing..Fib(1)
... 
Leaving ...Fib(1)returning...1

returning...2
computing..Fib(2)
... 
Leaving ...Fib(2)returning...1

returning...3
computing..Fib(3)
... 
Leaving... Fib(3)
computing..Fib(2)
... 
Leaving ...Fib(2)returning...1

computing..Fib(1)
... 
Leaving ...Fib(1)returning...1

returning...2
returning...5
returning...13
computing..Fib(6)
... 
Leaving... Fib(6)
computing..Fib(5)
... 
Leaving... Fib(5)
computing..Fib(4)
... 
Leaving... Fib(4)
computing..Fib(3)
... 
Leaving... Fib(3)
computing..Fib(2)
... 
Leaving ...Fib(2)returning...1

computing..Fib(1)
... 
Leaving ...Fib(1)returning...1

returning...2
computing..Fib(2)
... 
Leaving ...Fib(2)returning...1

returning...3
computing..Fib(3)
... 
Leaving... Fib(3)
computing..Fib(2)
... 
Leaving ...Fib(2)returning...1

computing..Fib(1)
... 
Leaving ...Fib(1)returning...1

returning...2
returning...5
computing..Fib(4)
... 
Leaving... Fib(4)
computing..Fib(3)
... 
Leaving... Fib(3)
computing..Fib(2)
... 
Leaving ...Fib(2)returning...1

computing..Fib(1)
... 
Leaving ...Fib(1)returning...1

returning...2
computing..Fib(2)
... 
Leaving ...Fib(2)returning...1

returning...3
returning...8
returning...21
computing..Fib(7)
... 
Leaving... Fib(7)
computing..Fib(6)
... 
Leaving... Fib(6)
computing..Fib(5)
... 
Leaving... Fib(5)
computing..Fib(4)
... 
Leaving... Fib(4)
computing..Fib(3)
... 
Leaving... Fib(3)
computing..Fib(2)
... 
Leaving ...Fib(2)returning...1

computing..Fib(1)
... 
Leaving ...Fib(1)returning...1

returning...2
computing..Fib(2)
... 
Leaving ...Fib(2)returning...1

returning...3
computing..Fib(3)
... 
Leaving... Fib(3)
computing..Fib(2)
... 
Leaving ...Fib(2)returning...1

computing..Fib(1)
... 
Leaving ...Fib(1)returning...1

returning...2
returning...5
computing..Fib(4)
... 
Leaving... Fib(4)
computing..Fib(3)
... 
Leaving... Fib(3)
computing..Fib(2)
... 
Leaving ...Fib(2)returning...1

computing..Fib(1)
... 
Leaving ...Fib(1)returning...1

returning...2
computing..Fib(2)
... 
Leaving ...Fib(2)returning...1

returning...3
returning...8
computing..Fib(5)
... 
Leaving... Fib(5)
computing..Fib(4)
... 
Leaving... Fib(4)
computing..Fib(3)
... 
Leaving... Fib(3)
computing..Fib(2)
... 
Leaving ...Fib(2)returning...1

computing..Fib(1)
... 
Leaving ...Fib(1)returning...1

returning...2
computing..Fib(2)
... 
Leaving ...Fib(2)returning...1

returning...3
computing..Fib(3)
... 
Leaving... Fib(3)
computing..Fib(2)
... 
Leaving ...Fib(2)returning...1

computing..Fib(1)
... 
Leaving ...Fib(1)returning...1

returning...2
returning...5
returning...13
returning...34
computing..Fib(8)
... 
Leaving... Fib(8)
computing..Fib(7)
... 
Leaving... Fib(7)
computing..Fib(6)
... 
Leaving... Fib(6)
computing..Fib(5)
... 
Leaving... Fib(5)
computing..Fib(4)
... 
Leaving... Fib(4)
computing..Fib(3)
... 
Leaving... Fib(3)
computing..Fib(2)
... 
Leaving ...Fib(2)returning...1

computing..Fib(1)
... 
Leaving ...Fib(1)returning...1

returning...2
computing..Fib(2)
... 
Leaving ...Fib(2)returning...1

returning...3
computing..Fib(3)
... 
Leaving... Fib(3)
computing..Fib(2)
... 
Leaving ...Fib(2)returning...1

computing..Fib(1)
... 
Leaving ...Fib(1)returning...1

returning...2
returning...5
computing..Fib(4)
... 
Leaving... Fib(4)
computing..Fib(3)
... 
Leaving... Fib(3)
computing..Fib(2)
... 
Leaving ...Fib(2)returning...1

computing..Fib(1)
... 
Leaving ...Fib(1)returning...1

returning...2
computing..Fib(2)
... 
Leaving ...Fib(2)returning...1

returning...3
returning...8
computing..Fib(5)
... 
Leaving... Fib(5)
computing..Fib(4)
... 
Leaving... Fib(4)
computing..Fib(3)
... 
Leaving... Fib(3)
computing..Fib(2)
... 
Leaving ...Fib(2)returning...1

computing..Fib(1)
... 
Leaving ...Fib(1)returning...1

returning...2
computing..Fib(2)
... 
Leaving ...Fib(2)returning...1

returning...3
computing..Fib(3)
... 
Leaving... Fib(3)
computing..Fib(2)
... 
Leaving ...Fib(2)returning...1

computing..Fib(1)
... 
Leaving ...Fib(1)returning...1

returning...2
returning...5
returning...13
computing..Fib(6)
... 
Leaving... Fib(6)
computing..Fib(5)
... 
Leaving... Fib(5)
computing..Fib(4)
... 
Leaving... Fib(4)
computing..Fib(3)
... 
Leaving... Fib(3)
computing..Fib(2)
... 
Leaving ...Fib(2)returning...1

computing..Fib(1)
... 
Leaving ...Fib(1)returning...1

returning...2
computing..Fib(2)
... 
Leaving ...Fib(2)returning...1

returning...3
computing..Fib(3)
... 
Leaving... Fib(3)
computing..Fib(2)
... 
Leaving ...Fib(2)returning...1

computing..Fib(1)
... 
Leaving ...Fib(1)returning...1

returning...2
returning...5
computing..Fib(4)
... 
Leaving... Fib(4)
computing..Fib(3)
... 
Leaving... Fib(3)
computing..Fib(2)
... 
Leaving ...Fib(2)returning...1

computing..Fib(1)
... 
Leaving ...Fib(1)returning...1

returning...2
computing..Fib(2)
... 
Leaving ...Fib(2)returning...1

returning...3
returning...8
returning...21
returning...55
The number of threes (3) is:  21
"""
