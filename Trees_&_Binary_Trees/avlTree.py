


# WHAT IS AN AVL (Balanced BST) TREE?
# An AVL tree is a self-balancing Binary Search tree where the difference between heights of left and 
# right subtrees cannot be MORE THAN ONE FOR ALL NODES.

# If at any time heights of left and right subtrees differ by more than one, 
# then rebalancing is done to restore AVL property, this process is called rotation



# WHY DO WE NEED AVL TREE?
# AVL tree makes sure that we wouldn't end with disbalanced tree (which will couse bad performances)
# this will increase performance during searching,deleting and inserting nodes
# for example:

# Disbalanced tree:                       Balanced Tree:
# |10|                                        _|40|_
#   \                                       /       \
#   |20|                                |20|         |60|
#     \                                /   \        /    \
#     |30|                          |10|  |30|    |50|  |70|
#       \
#       |40|
#         \ 
#         |50|
#           \
#           |60|
#             \
#             |70|



# Operations on AVL Tree
# - Creation of AVL tree
# - Search for a node in AVl trees
# - Traverse all nodes in AVl trees
# - Delete a node from AVL trees
# - Delete the enntire AVL trees


class AVLNode:
    def __init__(self, data):
        self.leftChild = None
        self.data = data
        self.rightChild = None
        self.height = 1 #to see if tree is Balanced
        

def preorderTravarsal(rootNode):
    if not rootNode: return
    print(rootNode.data)
    preorderTravarsal(rootNode.leftChild)
    preorderTravarsal(rootNode.leftChild)

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
    if not rootNode: return
    customeQueue = Queue()
    customeQueue.enqueue(rootNode)
    while not customeQueue.isEmpty():
        root = customeQueue.dequeue()
        print(root.data)
        if root.leftChild:
            customeQueue.enqueue(root.leftChild)
        if root.rightChild:
            customeQueue.enqueue(root.rightChild)
            
def searchNode(rootNode, nodeValue):
    if rootNode.data == nodeValue: 
        print(f'{nodeValue} exists in tree')
    elif nodeValue < rootNode.data:
        searchNode(rootNode.leftChild, nodeValue)
    else:
        searchNode(rootNode.rightChild, nodeValue)



# INSERT A NODE IN AVL TREE
# Case 1: Rotation is not required (then insertion is the same as in binary search tree)

# Case 2: Rotation is required (first we insert node and then check if any upper node couse disbalance)
# to find which condition to use we first find node that couse disbalance then check which child (left,right) and grandChild (left,right) have larger height
#------------------------------------------------------------------------------------------
#- LL- left left condition (in case of this condition we made right rotation for disblanced node)
###### rotateRight(disbalancedNode):
######     newRoot - disbalancedNode.leftChild
######     disbalancedNode.leftChild = disbalancedNode.leftChild.rightChild
######     newRoot.rightChild = disbalancedNode
######     update height of disbalancedNode and newRoot
######     return newRoot
#------------------------------------------------------------------------------------------
# - LR - left right condition  (in case of this condition we made left rotation for the left child and then right rotation as in case LL)
###### rotateLeft(disbalancedNode):
######    newRoot = disbalancedNode.rightChild
######    disbalancedNode.rightChild = disbalancedNode.rightChild.leftChild
######    newRoot.leftChild = disbalancedNode
######    update height of disbalancedNode and newRoot
######    return newRoot
#------------------------------------------------------------------------------------------
# - RR - right right condition (in case of this condition we made left rotation for disbalanced node)
#------------------------------------------------------------------------------------------
# - RL - right left condition (in case of this condition we made right rotation for the rightChild and then left rotation for disbalanced node)



# Function to find height of rootNode
def getHeight(rootNode):
    if not rootNode: return 0 #if node is none return height 0
    return rootNode.height

def rightRotation(disbalancedNode): #time and space complexity O(1)
    newRoot = disbalancedNode.leftChild
    disbalancedNode.leftChild = disbalancedNode.leftChild.rightChild
    newRoot.rightChild = disbalancedNode
    # update heights
    # to calculate height get highest subtree and add one to it
    disbalancedNode.height = 1 + max(getHeight(disbalancedNode.leftChild),getHeight(disbalancedNode.rightChild))
    newRoot.height = 1 + max(getHeight(newRoot.leftChild),getHeight(newRoot.rightChild))
    return newRoot

def leftRotation(disbalancedNode): #time and space complexity O(1)
    newRoot = disbalancedNode.rightChild
    disbalancedNode.rightChild = disbalancedNode.rightChild.leftChild
    newRoot.leftChild = disbalancedNode
    #update heights
    disbalancedNode.height = 1 + max(getHeight(disbalancedNode.leftChild),getHeight(disbalancedNode.rightChild))
    newRoot.height = 1 + max(getHeight(newRoot.leftChild),getHeight(newRoot.rightChild))
    return newRoot


# function that checks balance between left and right subtrees 
def getBalance(rootNode):
    if not rootNode: return
    return getHeight(rootNode.leftChild) - getHeight(rootNode.rightChild)


def insertNode(rootNode, value): #This function takes O(logN) time and space complexity
    if not rootNode: 
        return AVLNode(value)
    elif value < rootNode.data:
        rootNode.leftChild = insertNode(rootNode.leftChild, value)
    elif value > rootNode.data:
        rootNode.rightChild = insertNode(rootNode.rightChild, value)
    
    # OPERATIONS MADE AFTER INSERTION !!!
    #change rootNode.height
    rootNode.height = 1 + max(getHeight(rootNode.leftChild),getHeight(rootNode.rightChild))
    balance = getBalance(rootNode)
    if balance > 1 and value < rootNode.leftChild.data: #insertion to left side of leftChild (LL condition)
        return rightRotation(rootNode)
    elif balance > 1 and value > rootNode.leftChild.data: #insertion to right side of leftChild (LR condition)
        rootNode.leftChild = leftRotation(rootNode.leftChild) #update leftChild
        return rightRotation(rootNode)
    elif balance < -1 and value < rootNode.rightChild.data: #insertion to left side of right child (RL condition)
        rootNode.rightChild = rightRotation(rootNode.rightChild) #update rightChild
        return leftRotation(rootNode)
    elif balance < -1 and value > rootNode.rightChild.data: #insertion to right side of right child (RR condition)
        return leftRotation(rootNode)
    
    return rootNode




# DELETE A NODE FROM AVL TREE
# Case 1 - The tree does not exist 
#------------------------------------------
# Case 2 - Rotation is not required
# - The node to be deleted is a leaf node
# - The node to be deleted has a child node 
# - The node to be deleted has two children (after deleting node we find min element of the right subtree)
#------------------------------------------
# Case 3 - Rotation is required (after deleting node we check if tree is balanced)
# - LL condition 
# - LR condition
# - RR condition
# - RL condition

# function to find succesor (następca) (min value of right subtree)
def  getMinValueNode(rootNode):
    if not rootNode or not rootNode.leftChild: return rootNode
    return getMinValueNode(rootNode.leftChild)

def deleteNode(rootNode, value):
    if not rootNode: # Case 1: rootNode is none
        return rootNode
    elif value < rootNode.data:
        rootNode.leftChild = deleteNode(rootNode.leftChild, value)
    elif value > rootNode.data:
        rootNode.rightChild = deleteNode(rootNode.rightChild, value)
    else: #if node to be deleted is found
        
        # Case 2: Rotation is not required
        if not rootNode.leftChild: #if left child doesnt't exist set rootNode to rightChild
            temp = rootNode.rightChild
            rootNode = None
            return temp
        elif not rootNode.rightChild: #if right child doesnt't exist set rootNode to leftChild
            temp = rootNode.leftChild
            rootNode = None
            return temp

        # Now if exists find successor of rootNode
        temp = getMinValueNode(rootNode.rightChild)
        rootNode.data = temp.data
        rootNode.rightChild = deleteNode(rootNode.rightChild, temp.data) # now delete successor from the right child to don't double it


    # Case 3: Rotation is required    
    rootNode.height = 1 + max(getHeight(rootNode.leftChild),getHeight(rootNode.rightChild))
    balance = getBalance(rootNode)
    if balance > 1 and value < rootNode.leftChild.data: # LL condition
        return rightRotation(rootNode)
    if balance > 1 and value > rootNode.leftChild.data: #LR condition
        rootNode.leftChild = leftRotation(rootNode.leftChild)
        return rightRotation(rootNode)
    if balance > 1 and value > rootNode.rightChild.data: #RR condition
        return leftRotation(rootNode)
    if balance > 1 and value > rootNode.rightChild.data: #RL condition
        rootNode.rightChild = rightRotation(rootNode.rightChild)
        return leftRotation(rootNode)

    return rootNode



#DELETE ENTIRE AVL TREE
def deleteAVL(rootNode):
    rootNode.leftChild, rootNode.rightChild, rootNode.data = None, None, None




newAVL = AVLNode(5)
newAVL = insertNode(newAVL, 10)
newAVL = insertNode(newAVL, 15)
newAVL = insertNode(newAVL, 20)

# This tree made with BST:        #This Tree made with AVL tree:

# |5|                         |                 |10|
#   \                         |                /   \
#   |10|                      |              |5|   |15|
#      \                      |                       \
#      |15|                   |                       |20|
#         \                   |          
#         |20|                |          


newAVL = deleteNode(newAVL, 15)

#   #Tree after deletion of 15:

#                 |10|
#                /   \
#              |5|   |20|


deleteAVL(newAVL)

levelOrderTraversal(newAVL)




# TIME AND SPACE COMPLEXITY OF AVL TREE

# Create AVl       Time complexity - O(1) || Space complexity -  O(1)
#------------------------------------------------------------------------------------
# Insert a node AVL       Time complexity - O(logN) || Space complexity -  O(logN)
#------------------------------------------------------------------------------------
# Traverse AVL       Time complexity - O(n) || Space complexity -  O(n)
#------------------------------------------------------------------------------------
# Search for a node AVL       Time complexity - O(logN) || Space complexity -  O(logN)
#------------------------------------------------------------------------------------
# Delete node from AVL       Time complexity - O(logN) || Space complexity -  O(logN)
#------------------------------------------------------------------------------------
# Delete Entire AVL       Time complexity - O(1) || Space complexity -  O(1)




































