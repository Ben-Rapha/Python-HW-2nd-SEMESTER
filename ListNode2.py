# ListNode2.py

class ListNode2(object):
    
    def __init__(self, item = None, leftL = None, rightL = None):

        '''creates a ListNode with the specified data value and
           two links: to the previous node and to the next node
        post: creates a ListNode with the specified data value and links'''
        
        self.item = item
        self.leftL = leftL
        self.rightL = rightL

    def __str__(self):
      ''' for printing the node '''
      
      return str(self.item)

# Testing
# create a linked list of 5 values: 34, 1, 23, 7, and 10.
# Displays it.
# Then insert new value, say 8 between 34 and 1. Display the updated list
# Then delete and element, update the links and display the new list.

n5 = ListNode2(10) # creating the last node
n4 = ListNode2(7,None,n5) # creating the next to the last node
n5.leftL = n4 # updating the left link of the last node
n3 = ListNode2(23,None,n4)
n4.leftL = n3
n2 = ListNode2(1,None,n3)
n3.leftL = n2
n1 =  ListNode2(34,None,n2)
n2.leftL = n1

# printing all the nodes, one by one
print("Here is our list of doubly linked nodes:",n1,n2,n3,n4,n5)
print("For example,",n3,"has",n3.leftL,"on the left, and",n3.rightL,"on the right.")
print("Inserting 8 between 34 and 1, and properly updating all links")
n6 = ListNode2(8,n1,n2)
n1.rightL = n6
n2.leftL = n6
print("Now, after",n1,"goes,",n1.rightL,"and before",n2,"goes",n2.leftL)
print("Deleting 7...")
n3.rightL = n5
n5.leftL = n3
print("Now, after",n3,"goes",n3.rightL,"and before",n5,"goes",n5.leftL)

