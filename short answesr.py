#KINGSLEY OTTO
#SHORT ANSWERS
# power . py

def loopPower ( a , n) :
    """ computes an exponantial value rerusively
    Pre-Condition: First number provided by user can be either float or an integer, second
    number provided must be only an integer
    Post-Condition: returns an integer value """
    
    ans = 1
    for i in range (n) :
        ans = ans * a
    return ans

    
# power . py
def recPower ( a , n) :
    """ computes a number with an expotional value using the strategy of divide
    and conquer.
    pre-Condition: Both numbers provided by the user can be either float or an
    integer
    postCondition: returns an interger value """
    
    # raises a to the int power n
    if n == 0 :
        return 1
    else :
        factor = recPower ( a , n // 2)
        if n % 2 == 0 :# n is even
            return factor * factor
        else :# n is odd
            return factor * factor * a
