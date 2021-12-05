
# Binary Tree (Python list vs Linked List)
#---------------------------------------------------------------
# Create Binary Tree O(1), O(n) - python list
# Create Binary Tree O(1), O(1) - Linked list
#---------------------------------------------------------------
# Insert a node to Binarty tree O(1), O(1) - Python list
# Insert a node to Binarty tree O(n), O(n) - Linked list
#---------------------------------------------------------------
# Delete a node from Binary Tree O(n), O(1) - Python list
# Delete a node from Binary Tree O(n), O(n) - Linked list
#---------------------------------------------------------------
# Search for a node in Binary Tree O(n), O(1) - Python list
# Search for a node in Binary Tree O(n), O(n) - Linked list
#---------------------------------------------------------------
#Traverse Binary Tree O(n), O(1) - Python list
#Traverse Binary Tree O(n), O(n) - Linked list
#---------------------------------------------------------------
# Delete entire Binary Tree O(1), O(1) - Python list
# Delete entire Binary Tree O(1), O(1) - Linked list






class binaryTree:
    def __init__(self, size):
        self.list = [None] * size
        self.lastUsedIndex = 0
        self.maxSize = size
        
    def insert(self, value):
        if self.lastUsedIndex + 1 == self.maxSize: return 'Is full'
        self.list[self.lastUsedIndex+1] = value
        self.lastUsedIndex += 1
        
    def search(self, value):
        for node in self.list:
            if node == value: return f'{value} exists in binary tree'
        return f'{value} not found'
    
    def preorderTravarsal(self, index):
        if index > self.lastUsedIndex:return
        rootNode = self.list[index]
        print(rootNode)
        #while inserting new values to tree made with list to insert left 
        # child we append it to nth*2 place but for right child nth*2+1 where n is index of parent node
        self.preorderTravarsal(index*2) #visit left subtree
        self.preorderTravarsal(index*2+1) #visit right subtree
        
    def inOrderTravarsal(self, index):
        if index > self.lastUsedIndex:return
        self.inOrderTravarsal(index*2) #first visit left subtrees until you reach last left element
        print(self.list[index]) 
        self.inOrderTravarsal(index*2+1) #then visi right subtree
        
    def postOrderTravarsal(self, index):
        if index > self.lastUsedIndex: return
        self.inOrderTravarsal(index*2) #first visit left subtrees until you reach last left element
        self.inOrderTravarsal(index*2+1) #then visi right subtree
        print(self.list[index]) # after visiting left and right child print value of node
        
    def levelOrderTraversal(self,index):
        for nodeIndex in range(1,self.lastUsedIndex+1):
            print(self.list[nodeIndex])
            
    def deleteNode(self, value):
        if self.lastUsedIndex == 0: return 
        for nodeIndex in range(1,self.lastUsedIndex+1):
            if self.list[nodeIndex] == value: 
                self.list[nodeIndex],self.list[self.lastUsedIndex] = self.list[self.lastUsedIndex], None
                self.lastUsedIndex -= 1
                
    def deleteBinaryTree(self):
        self.list = None
        
        



# Create new binary tree 
newBinaryTree = binaryTree(10)
newBinaryTree.insert('Drinks')
newBinaryTree.insert('Hot')
newBinaryTree.insert('Cold')
newBinaryTree.insert('Tea')
newBinaryTree.insert('Coffe')

print(newBinaryTree.search('Tea'))
print(newBinaryTree.list)
newBinaryTree.preorderTravarsal(1)
print('------------------In_Order_Traversal')
newBinaryTree.inOrderTravarsal(1)
print('------------------Post_Order_Traversal')
newBinaryTree.postOrderTravarsal(1)
print('------------------Level_Order_Traversal')
newBinaryTree.levelOrderTraversal(1)
print('------------------Delete_Tea')
newBinaryTree.deleteNode('Tea')
print(newBinaryTree.list)
print('------------------Delete_Binary_Tree')
newBinaryTree.deleteBinaryTree()
print(newBinaryTree.list)























































