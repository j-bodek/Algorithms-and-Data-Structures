

# BINARY TREE
# - Binary trees are the data structures in which each node has at most two children,
# often referred to as the left and right children 
# - Binary tree is a family of data structure (BST, Heap tree, AVL, red black trees, Syntax trees)


# WHY WE NEED BINARY TREES 
# - Binary trees are a prerequisite for more advanced trees like BST, AVL, Red Black Trees
# - Huffman coding problem, heap priority problem and exporssion parsing problems can be solved 
# efficiently using binary trees 


# TYPES OF BINARY TREE
# - Full Binary Tree => if all non leafs nodes have one or two binary tree
# - Perfect Binary Tree => all non leafs nodes have two childrens and all are in the same level
# - Complete Binary Tree => all level are completly filled (two childrens on the same level) trees except the last level 
# - Balanced Binary Tree => all leaf nodes (without any children) are located from the root of the same distance


# HOW BINARY TREE CAN BE REPRESENTED 
# - with linked list 
# - with list (array)


# CREATE BINARY TREE USING LINKED LIST (operations):
# - Creation of Tree 
# - Insertion of a node 
# - Deletion of a node 
# - Search for a value
# - Traverse all nodes 
# - Deletion of tree 

class TreeNode:
    def __init__(self,data):
        self.leftChild = None
        self.data = data
        self.rightChild = None

# Create value of root node (in Binary Tree created with linked list)
newBinaryTree = TreeNode('Drings')
# Add childrens to root node
leftChild = TreeNode('Hot')
rightChild = TreeNode('Cold')
newBinaryTree.leftChild = leftChild
newBinaryTree.rightChild = rightChild
# Add childrens to leftChild
leftHot = TreeNode('Tea')
rightHot = TreeNode('Coffe')
leftChild.leftChild = leftHot
leftChild.rightChild = rightHot
# Add childrens to rightChild
leftCold = TreeNode('Pepsi')
rightCold = TreeNode('Sprite')
rightChild.leftChild = leftCold
rightChild.rightChild = rightCold


print('------------------PREORDER_TRAVERSAL------------------')
# rootNode => leftChild => leftHot => rightHot => rightChild => leftCold => rightCold
# Preorder travarsal
def preorderTravarsal(rootNode):
    if not rootNode: return None
    print(rootNode.data)
    preorderTravarsal(rootNode.leftChild)
    preorderTravarsal(rootNode.rightChild)

preorderTravarsal(newBinaryTree)


print('------------------INORDER_TRAVERSAL------------------')
# leftHot => leftChild => rightHot => rootNode => leftCold => rightChild => rightCold

# Inorder traversal
def inorderTraversal(rootNode):
    if not rootNode: return None #if node does not exist
    inorderTraversal(rootNode.leftChild) #First visit left child (to start from the left subtree)
    print(rootNode.data) #if there is not more subrees print node data
    inorderTraversal(rootNode.rightChild) # then start traversing right subtrees

inorderTraversal(newBinaryTree)


print('------------------POSTORDER_TRAVERSAL------------------')
# leftHot => rightHot => leftChild => leftCold => rightHot => rightChild => rootNode
# Postorder traversal 
def postorderTraversal(rootNode):
    if not rootNode: return None #if node does not exist
    postorderTraversal(rootNode.leftChild) #First visit left child (to start from the left subtree)
    postorderTraversal(rootNode.rightChild) # then visit right child
    print(rootNode.data) #if there is not more subrees print node data

postorderTraversal(newBinaryTree)


print('------------------LevelOrder_TRAVERSAL------------------')
# We traverse the tree by levels starting from the first level (rootNode)
# rootNode => leftChild => rightChild => leftHot => rightHot => leftCold => rightCold
# We will create levelOrderTraversal using Queue 

import sys
import os
sys.path.append(os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'Queues')))
from QueueLinkedList import Queue
def levelOrderTraversal(rootnode):
    if not rootnode: return 
    customeQueue = Queue()
    customeQueue.enqueue(rootnode)
    while not customeQueue.isEmpty():
        root = customeQueue.dequeue()
        print(root.data)
        if root.leftChild:
            customeQueue.enqueue(root.leftChild)
        if root.rightChild:
            customeQueue.enqueue(root.rightChild)

levelOrderTraversal(newBinaryTree)


print('--------------------------------LINEAR_SEARCHING_TREE--------------------------------')

# This searching algorithm use level traversal 
def searchBinaryTree(rootNode, Value):
    if not rootNode: return 
    customeQueue = Queue()
    customeQueue.enqueue(rootNode)
    while not customeQueue.isEmpty(): 
        root = customeQueue.dequeue()
        if root.data == Value: return True
        if root.leftChild:
            customeQueue.enqueue(root.leftChild)
        if root.rightChild:
            customeQueue.enqueue(root.rightChild)
    return False

print(searchBinaryTree(newBinaryTree, 'Pepsi'))


# INSERT NODE TO BINARY TREE
# Possibilities:
# - RootNode is blank
# - The tree exists and we have to look for the first vacant place
# (we use level order traversal to find first node that have less then two childrens and then add new one as his child)

def insert(rootNode, newNode):
    if not rootNode: return
    customeQueue = Queue()
    customeQueue.enqueue(rootNode)
    while not customeQueue.isEmpty():
        root = customeQueue.dequeue()
        if root.leftChild:
            customeQueue.enqueue(root.leftChild)
        if root.rightChild:
            customeQueue.enqueue(root.rightChild)
        if not root.leftChild:
            root.leftChild = newNode
            return
        if not root.rightChild:
            root.rightChild = newNode
            return
        
insert(newBinaryTree, TreeNode('With Ice'))
levelOrderTraversal(newBinaryTree)


print('------------------GET_DEEPEST_NODE------------------')

def getDeepestNode(rootNode):
    if not rootNode: return
    customeQueue = Queue()
    customeQueue.enqueue(rootNode)
    while not customeQueue.isEmpty():
        root = customeQueue.dequeue()
        if root.leftChild:
            customeQueue.enqueue(root.leftChild)
        if root.rightChild:
            customeQueue.enqueue(root.rightChild)
    deepestNode = root
    return root
    

print('------------------DELETE_DEEPEST_NODE------------------')


def deleteDeepestNode(rootNode, deepestNode):
    if not rootNode: return
    customeQueue = Queue()
    customeQueue.enqueue(rootNode)
    while not customeQueue.isEmpty(): 
        root = customeQueue.dequeue()
        if root is deepestNode: 
            root = None
            return
        if root.rightChild:
            if root.rightChild is deepestNode: 
                root.rightChild = None
                return
            else:
                customeQueue.enqueue(root.rightChild) 
        if root.leftChild:
            if root.leftChild is deepestNode: 
                root.leftChild = None
                return
            else:
                customeQueue.enqueue(root.leftChild) 
            
            
def deleteNode(rootNode, deleteNode):
    if not rootNode: return
    customeQueue = Queue()
    customeQueue.enqueue(rootNode)
    while not customeQueue.empty():
        root = customeQueue.dequeue()
        if not root.data == deleteNode:
            deepestNode = getDeepestNode(rootNode)
            root.data = deepestNode.data
            deleteDeepestNode(rootNode,deepestNode)
        if root.leftChild:
            customeQueue.enqueue(root.leftChild)
        if root.rightChild:
            customeQueue.enqueue(root.rightChild)


























































