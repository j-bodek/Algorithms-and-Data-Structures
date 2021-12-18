

'''
Validate BST
'''
# Implement a function to check if a binary tree is a Binary Search Tree

# The binary Tree is Binary Search Tree if:
# - the left subtree of a node contains only nodes with keys less than the nodes key
# - The right subtree of a node contains only nodes with keys greater than the node's key
# - These conditions are applicable for both left and right subtrees

'''
Examples:
 2 
/ \
1 4
True

  _4_  
 /   \ 
1     3
     / \
     2 5
False
'''

# To solve this problem we will call recursively if child node (right and left) is less or greater then root nodes value
# We will set min and max value that will be updated during tree travering


class TreeNode:
     def __init__(self, value):
         self.val = value
         self.left = None
         self.right = None


def helper(node, minValue = float('-inf'), maxValue = float('inf')):
    if not node: return True 
    value = node.val
    if value <= minValue or value >= maxValue: 
        return False
    
    # call recursively for right subtree
    if not helper(node.right, value, maxValue): #check if right child is less or greater then root
        return False
    
    # call recursively for left subtree
    if not helper(node.left, minValue, value): #check if left child is less or greater then root
        return False
    
    return True

def isValidBST(root):
    return helper(root)


root1 = TreeNode(2)
root1.left = TreeNode(1)
root1.right = TreeNode(4)
'''
   2
  / \
 1   4
'''
print(isValidBST(root1))


root2 = TreeNode(4)
root2.left = TreeNode(1)
root2.right = TreeNode(3)
'''
   4
  / \
 1   3
'''

print(isValidBST(root2))



























