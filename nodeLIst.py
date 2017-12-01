#KINGSLEY.OTTO
#CSI 32
#HOMEWORK 6


class ListNode2(object):
    def __init__(self,leftL = None, item = None, rightL = None):
        self.item = item
        self.rightL = rightL
        self.leftL = leftL


    def __str__(self):
        return str(self.item)

n5 = ListNode2(10)
n4 = ListNode2(n5.rightL,7)
n3 = ListNode2(n4.rightL,23)
n2 = ListNode2(n3.rightL,1)
n1 = ListNode2(n2.rightL,34)

print(n5,n4,n3,n2,n1)

n6 = ListNode2(n2.rightL,8,n1.leftL)
n2.rightL = n6.leftL
n1.leftL =  n6.rightL
print(n5,n4,n3,n2,n6,n1)

n3 = ListNode2(n5.rightL,23)
n5 = ListNode2(10,n3.leftL)
n5.rightL = n3.leftL

