

'''
In-order Successor in BST
'''
# Write an algorithm to find the next node (i.e in-order successor) of given node in a binary search tree.
# You may assume that each node has a link to its parent

# inorder traversal:
# - Starts from left subtree then goes to rootnode then goes to right subtree

'''
  _4_  
 /   \ 
 2   8
/ \ / \
1 3 5 9
'''


class Node: 
	def __init__(self, key): 
		self.data = key 
		self.left = None
		self.right = None

def insert(node, data):
   if node is None:
       return Node(data)
   else:
       if data <= node.data:
           temp = insert(node.left, data)
           node.left = temp
           temp.parent = node
       else:
           temp = insert(node.right, data)
           node.right = temp
           temp.parent = node      
       return node

# helper functoin that finds most left leaf node
def minValue(node):
    currentNode = node
    
    #find left most leaf node
    while currentNode:
        if currentNode.left is None:
            break
        currentNode = currentNode.left
    return currentNode

def inOrderSuccessor(currentNode):
    if currentNode.right:
        return minValue(currentNode.right)

    parent = currentNode.parent
    # - If right subtree of node is NOT NONE, then successor lies in right subtree
    # - If right subtree of node is NONE, then successor is one of the anecstors
    while parent:
        if currentNode != parent.right:
            break
        currentNode = parent
        parent = parent.parent
    return parent

root = None
root = insert(root, 4)
root = insert(root, 2)
root = insert(root, 8)
root = insert(root, 1)
root = insert(root, 3)
root = insert(root, 5)
root = insert(root, 8)

'''
    _4_  
   /   \ 
  2     8
 / \   / \
1   3 5   9

In order traversal goes:
1 -> 2 -> 3 -> 4 -> 5 -> 8 -> 9

So successor of 3 should be 4
'''

temp = root.left.right #3
successor = inOrderSuccessor(temp)
print(successor.data)









