


# WHAT IS AN AVL TREE?
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
            customeQueue.enqueue(root.right)
            
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
#- LL- left left condition (in case of this condition we made right rotation)
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
# - RR - right right condition
#------------------------------------------------------------------------------------------
# - RL - right left condition









newAVL = AVLNode(10)












































