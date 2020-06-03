import random
class BinarySearchTree():
    def __init__(self,val = 0):
        self.val = val
        self.left = None
        self.right = None
        self.size = 1
    def insert(self, input):
        if input >= self.val:
            if self.right == None:
                self.right = BinarySearchTree(input)
                self.size += 1
            else:
                self.right.insert(input)
        else:
            if self.left == None:
                self.size += 1
                self.left = BinarySearchTree(input)
            else:
                self.left.insert(input)

    def find(self, target):
        if target == self.val:
            return self
        elif target > self.val:
            return self.right.find(target)
        else:
            return self.left.find(target)

    def findRandomNode(self):
        left_size = 0 if self.left == None else self.left.size
        chance = random.randint(1,self.size)
        print(chance)
        if chance == 1:
            return self
        elif chance < left_size:
            return self.left.findRandomNode()
        else:
            return self.right.findRandomNode()
        
tree = BinarySearchTree(5)
tree.insert(2)
tree.insert(3)
tree.insert(6)
tree.insert(7)

# A function to do preorder tree traversal 
def printPreorder(root): 
  
    if root: 
  
        # First print the data of node 
        print(root.val), 
  
        # Then recur on left child 
        printPreorder(root.left) 
  
        # Finally recur on right child 
        printPreorder(root.right) 
# printPreorder(tree)
print(tree.findRandomNode())