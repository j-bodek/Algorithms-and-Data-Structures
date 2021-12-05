

# What is a Binary Search Tree?
# - In the left subtree the value of a node is less than or equal to its parent node's value
# - In the right subtree the value of a node is greater than its parent node's value



# Example:

#          ___|70|___
#         /          \
#       |50|        |90|
#      /    \      /    \
#    |30|  |60|  |80|  |100|
#   /    \
# |20|  |40|



# Why Binary Search Tree?
# - It performs faster than Binary Tree when inserting and deleting nodes

# Common Operations on Binary Search Tree
# - Creation fo Tree 
# - Insertion of a node
# - Deletion of a node
# - Search for a value
# - Traverse all nodes
# - Delete entire Tree


# TIME AND SPACE COMPLEXITY OF BINARY SEARCH TREE
#----------------------------------------------------------------
# Create BST  O(1) - time complexity, O(1) - space complexity
#----------------------------------------------------------------
# Insert a node BST  O(logN) - time complexity, O(logN) - space complexity
#----------------------------------------------------------------
# Traverse BST  O(n) - time complexity, O(n) - space complexity
#----------------------------------------------------------------
# Search for a node BST  O(logN) - time complexity, O(logN) - space complexity
#----------------------------------------------------------------
# Delete node from BST  O(logN) - time complexity, O(logN) - space complexity
#----------------------------------------------------------------
# Delete entire BST O(1) - time complexity, O(1) - space complexity


class binarySearchTreeNode:
    def __init__(self,data):
        self.leftChild = None
        self.data = data
        self.rightChild = None
        
        
def insertNode(rootNode,value):
    if rootNode.data == None: 
        rootNode.data = value
        
    elif value <= rootNode.data:                                  
        if not rootNode.leftChild: #If left child is none     #|  
            rootNode.leftChild = binarySearchTreeNode(value)  #| 
        else: #else call insert recursively on leftChild      #|
            insertNode(rootNode.leftChild,value)              #|
                                                              #|____
    elif value > rootNode.data:                               #|____> spaceComplexity O(logN), timeComplexity O(logN)
        if not rootNode.rightChild: #If rightChild is none    #|
            rootNode.rightChild = binarySearchTreeNode(value) #|
        else: #else call insert recursively on rightChild     #|
            insertNode(rootNode.rightChild,value)             #|
            
            
            
# Traversal of Binary Search Tree
# Depth first search
# - preorder traversal
# - inorder Traversal
# - post order traversal

# Breadth first search 
# - level order traversal

def preorderTraversal(rootNode):
    # RootNode => LeftSubtree => RightSubtree
    if not rootNode: return
    print(rootNode.data)
    preorderTraversal(rootNode.leftChild) # recursively visit leftChild
    preorderTraversal(rootNode.rightChild) # Then recursively visit rightChild
    
def inorderTraversal(rootNode):
    # LeftSubtree => RootNode => RightSubtree
    if not rootNode: return
    inorderTraversal(rootNode.leftChild) #Visit leftChild
    print(rootNode.data) #then rootnode
    inorderTraversal(rootNode.rightChild) #and in the last step rightChild
            
def postorderTraversal(rootNode):
    # LeftSubtree => RightSubtree => rootNode
    if not rootNode: return
    postorderTraversal(rootNode.leftChild) #first visit leftSubtree
    postorderTraversal(rootNode.rightChild) #then visit rightSubtree
    print(rootNode.data) #and in the last step visit rootNode
            
            
import sys
import os
sys.path.append(os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'Queues')))
from QueueLinkedList import Queue
def levelOrderTraversal(rootNode):
    # start from rootNode then traverse through all levels (first, second ...) starting from left
    if not rootNode: return
    queue = Queue()
    queue.enqueue(rootNode)
    while not queue.isEmpty():
        root = queue.dequeue()
        print(root.data)
        if root.leftChild:
            queue.enqueue(root.leftChild)
        if root.rightChild:
            queue.enqueue(root.rightChild)
            
 
            
# Search for a node in Binary Search Tree
def searchBinarySearchTree(rootNode, value):
    if rootNode.data == value:
        print(f'{value} exists in binary search tree')    
    elif value <= rootNode.data:
        
        if rootNode.leftChild.data == value:
            print(f'{value} exists in binary search tree')        
        else:
            searchBinarySearchTree(rootNode.leftChild, value)
            
    elif value > rootNode.data:
        
        if rootNode.rightChild.data == value:
            print(f'{value} exists in binary search tree')    
        else:
            searchBinarySearchTree(rootNode.rightChild, value)
            
            
# Delete node from binary search tree
# Case 1: The node to be deleted is a leaf node
# Case 2: The node has one child
# Case 3: The node has two children
def minValueNode(rootNode):
    current = rootNode
    while current.leftChild:
        current = current.leftChild
    return current

def deleteNode(rootNode, nodeValue):
    if not rootNode: return
    if nodeValue < rootNode.data: #looking for node to delete
        rootNode.leftChild = deleteNode(rootNode.leftChild, nodeValue)
    elif nodeValue > rootNode.data: #looking for node to delete
        rootNode.rightChild = deleteNode(rootNode.rightChild, nodeValue)
    else: # node to be deleted
        # Check which case of deletion it is (is deleteNode has one,two,or none childrens)
        if not rootNode.leftChild:
            temp, rootNode = rootNode.rightChild, None
            return temp
        if not rootNode.rightChild:
            temp, rootNode = rootNode.leftChild, None
            return temp
        
        temp = minValueNode(rootNode.rightChild) #find smallest value in right subtree
        rootNode.data = temp.data #after finding it set its value to the node that you want to delete
        rootNode.rightChild = deleteNode(rootNode.rightChild, temp.data) # do the same for the right child of deleted node

    return rootNode


def deleteEntireBinaryTree(rootNode):
    if not rootNode: return
    rootNode.leftChild,rootNode.rightChild,rootNode.data = None,None,None
            
            
        

#Creation of binary search tree
newBinarySearchTree = binarySearchTreeNode(None)
insertNode(newBinarySearchTree,70)
insertNode(newBinarySearchTree,50)
insertNode(newBinarySearchTree,90)
insertNode(newBinarySearchTree,30)
insertNode(newBinarySearchTree,60)
insertNode(newBinarySearchTree,80)
insertNode(newBinarySearchTree,100)
insertNode(newBinarySearchTree,20)
insertNode(newBinarySearchTree,40)
# Visualization of this Binary Search Tree
#          ___|70|___
#         /          \
#       |50|        |90|
#      /    \      /    \
#    |30|  |60|  |80|  |100|
#   /    \
# |20|  |40|
print('--------------------------------Pre_Order_Traversal--------------------------------')
preorderTraversal(newBinarySearchTree)
print('--------------------------------In_Order_Traversal--------------------------------')
inorderTraversal(newBinarySearchTree)
print('--------------------------------Post_Order_Traversal--------------------------------')
postorderTraversal(newBinarySearchTree)
print('--------------------------------Level_Order_Traversal--------------------------------')
levelOrderTraversal(newBinarySearchTree)
print('--------------------------------Search_value_in_binary_search_tree--------------------------------')
searchBinarySearchTree(newBinarySearchTree, 100)
print('--------------------------------Delete_Node--------------------------------')
deleteNode(newBinarySearchTree,100)
levelOrderTraversal(newBinarySearchTree)
print('--------------------------------Delete_Entire_Binary_Search_Tree--------------------------------')
deleteEntireBinaryTree(newBinarySearchTree)
print(newBinarySearchTree.data, newBinarySearchTree.leftChild, newBinarySearchTree.rightChild)