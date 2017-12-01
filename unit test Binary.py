#KINGSLEY OTTO
#UNIT TESTING INSERCT_REC AND FIND METHOD
#HOMEWORK 13

from BST1 import*
import unittest

class Test(unittest.TestCase):
    def testinsert_rec(self):
        R = BST()
        R.insert_rec(7)
        R.insert_rec(3)
        R.insert_rec(8)
        R.insert_rec(2)
        R.insert_rec(5)
        R.insert_rec(9)
        print(R.asList())

        testList = [2,3,5,7,8,9]

        self.assertEqual(R.asList(), testList)
        
    def testfind(self):
        R = BST()
        R.insert_rec(3)
        R.insert_rec(8)
        R.insert_rec(2)
        R.insert_rec(5)
        R.insert_rec(9)
        R.asList()

        m = R.find(8)
        q = R.find(2)
        a = R.find(9)
        t = R.find(5)
        Tt = (m,q,a,t)
        print(Tt)
        self.assertEqual(Tt, (8,2,9,5))

    def testfind2(self):
        N = BST()
        mm = N.find(11)
        qq = N.find(1)
        aa = N.find(4)
        NN = (mm,qq,aa)
        print(NN)

        self.assertEqual(NN, (None,None,None))



unittest.main()

"""
(8, 2, 9, 5)
.(None, None, None)
.[2, 3, 5, 7, 8, 9]
.
----------------------------------------------------------------------
Ran 3 tests in 0.010s

OK
"""

        
        
        
