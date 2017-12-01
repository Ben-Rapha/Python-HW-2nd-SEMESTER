# The following methods are to be added to the AVLTree class


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
