# AVLTree.py
#KINGSLEY OTTO
#CSI 33 
#HOMEWORK 14
from TreeNode import *
from MyQueue import *

class AVLTree(object):

    #------------------------------------------------------------

    def __init__(self):

        '''post: creates empty AVL tree'''

        self.root = None

    #------------------------------------------------------------

    def insert(self, value):

        '''post: insert value into proper location in AVL tree'''

        self.root = self._insert_help(self.root, value)

    #------------------------------------------------------------

    def _insert_help(self, t, value):

        '''private helper method to insert value into AVL (sub)tree with
        root node t'''

        if t is None:
            t = TreeNode(value)
            
        elif value < t.item: # inserting into the left subtree
            t.left = self._insert_help(t.left, value)
            # left subtree height may be now larger than right subtree
            if get_height(t.left) - get_height(t.right) == 2:
                # determine which subtree the new value was inserted
                if value < t.left.item:
                    # insertion into left subtree of left child: single rotation
                    t = self._left_single_rotate(t)
                else:
                    # insertion into right subtree of left child: double rotation
                    t = self._right_left_rotate(t)

        else: # inserting into the right subtree
            if value > t.item:
                t.right = self._insert_help(t.right, value)
            if get_height(t.right) - get_height(t.left) == 2:
                if value > t.right.item:
                    t = self._right_single_rotate(t)
                else:
                    t = self._left_right_rotate(t)
            # exercise for reader
            
        # update height of tree rooted at t
        t.height = max(get_height(t.left), get_height(t.right)) + 1
        return t

    #------------------------------------------------------------

    def _left_single_rotate(self, t):

        '''private rotation method for inserting into left subtree of
        left child of t'''

        grandparent = t
        parent = t.left

        grandparent.left = parent.right
        parent.right = grandparent
        t = parent

        grandparent.height = max(get_height(grandparent.left),
                                 get_height(grandparent.right)) + 1
        parent.height = max(get_height(parent.left), 
                            get_height(parent.right)) + 1
        return t
    #---------------------------------------------------------------

    def _right_single_rotate(self, t):
        '''private rotation method for inserting into right subtree of
        right child of t'''

        grandparent = t
        parent = t.right

        grandparent.right = parent.left
        parent.left = grandparent
        t = parent

        grandparent.height = max(get_height(grandparent.right),get_height(grandparent.left))+1
        parent.height = max(get_height(parent.right),get_height(parent.left)) +1
        return t 

    #------------------------------------------------------------

    def _right_left_rotate(self, t):

        '''private rotation method for inserting into right subtree of
        left child of t'''

        t.left = self._right_single_rotate(t.left)
        t = self._left_single_rotate(t)
        return t

    #--------------------------------------------------------------

    def _left_right_rotate(self, t):

        '''private rotation method for inserting into left subtree of
        right child of t'''

        t.right = self._left_single_rotate(t.right)
        t = self._right_single_rotate(t)
        return t

 #--------------- Some of the code below is just grabbed from BST code ----

    def __len__(self):
        return self.size

    def height(self):
        return self.root.height

    def printTree(self):
        "just prints all nodes at each level"
        roots = Queue()
        roots.enqueue(self.root)
        
        # iterating over the height of the tree
        for i in range(get_height(self.root)+1):
            for j in range(roots.size()):
                nextRoot = roots.dequeue()
                if nextRoot is not None:
                    print(nextRoot.item, end="   ")

                    if nextRoot.left is not None:
                        roots.enqueue(nextRoot.left)
                    else:
                        roots.enqueue(None)
                    if nextRoot.right is not None:
                        roots.enqueue(nextRoot.right)
                    else:
                        roots.enqueue(None)
                else:
                    print("   ")
                
            print("\n")

# This is the test-code

def main():
    a = AVLTree()
    a.insert(5)
    a.insert(3)
    a.insert(7)
    
    a.insert(2)
    a.insert(4)
    a.insert(10)
    print("Before addition of 13 (right-right) - which will make the tree unballanced:")
    a.printTree()
    a.insert(13)
    print("After addition and re-ballancing:")
    a.printTree()

    b = AVLTree()
    b.insert(5)
    b.insert(3)
    b.insert(7)
    b.insert(2)
    b.insert(4)
    b.insert(10)
    print("Before addition of 8 (right-left) - which will make the tree unballanced:")
    b.printTree()
    b.insert(8)
    print("After addition and re-ballancing:")
    b.printTree()

main()    

