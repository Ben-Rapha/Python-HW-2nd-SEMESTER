#KINGSLEY OTTO
#CSI 33
#HOMEWORK 1
#THIS PROGRAM REMOVES DUPLICATE FROM A LIST



def removeD(List): #""" FUNCTION TO REMOVE DUPLICATE"""
    
    newList = []  #""" CREATE NEW EMPTY LIST"""
    for value in List:
        if value not in newList:
           newList.append(value)# """ ADD VALUES TO THE NEW LIST"""
    return newList
       

def main():
    List = [1,1,3,3,3,4,5,5,8,9,9,9,9,10]
    print("Duplicate list")
    print(List)
    print()
    print("New list")
    Unduplicated = removeD(List)#""" CALLS FUNCTION TO REMOVE DUPLIICATES"""
    print(Unduplicated)

main()
            
""""
Duplicate list
[1, 1, 3, 3, 3, 4, 5, 5, 8, 9, 9, 9, 9, 10]

New list
[1, 3, 4, 5, 8, 9, 10]

(Θ(n))
"""
