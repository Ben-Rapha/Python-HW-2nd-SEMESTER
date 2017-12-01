#KINGSLEY.OTTO
#CSI 33
#HOMEWORK 11

#Write a recursive function that detects whether a string is a palindrome. The
#basic idea is to check that the first and last letters of the string are the same
#letter; if they are, then the entire string is a palindrome if everything between
#those letters is a palindrome. There are a couple of special cases to check for.
#If either the first or last character of the string is not a letter, you can check
#to see if the rest of the string is a palindrome with that character removed.
#Also, when you compare letters, make sure that you do it in a case-insensitive
#way.

def IsPlaindrome(s):
    if len(s) < 1 :
        print ("This is a plaindrome")
        return True
    else:
        if s[0] == s[-1]:
            return IsPlaindrome(s[1:-1])
        else:
            print("This is not a plaindrome")
            

def main():
    print(" This program checks if a string is a plaindrome ")
    r = input(" Please enter your string you wish to check : ")
    r = r.casefold()
    if r.isalpha() == False:
        q = " ".join([c for c in r if c.isalpha()])
        IsPlaindrome(q)
    else:
        IsPlaindrome(r)
    
main()
"""
This program checks if a string is a plaindrome 
 Please enter your string you wish to check : "A man, a plan, a canal, Panama! "
This is a plaindrome

This program checks if a string is a plaindrome 
Please enter your string you wish to check : This is a plaindrome
This is not a plaindrome

This program checks if a string is a plaindrome
Please enter your string you wish to check : Sore was I ere I saw Eros
This is a plaindrome
"""
