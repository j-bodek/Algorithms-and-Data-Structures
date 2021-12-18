

'''
Check Balanced
'''
# Implement a function to check if a binary tree is balanced. for the purposes of this question, a balanced
# tree is defined to be a tree such that the heights of the two subtrees of any node never differ by more than one

# HINT DURING TREE DATA STRUCTURE PROBLEMS : ALWAYS TRY IF YOU CAN SOLVE IT USEING RECURSION

# THE BINARY TREE IS BALANCED IF:
# - The right subrtree is balanced 
# - The left subtree is balanced 
# - The difference between the height of the left subtree and the right subtree is at most 1


class Node():
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


# helper function
def isBalancedHelper(root):
    if not root: return 0 # return height of 0
    # call recursively for left subtree
    leftHeight = isBalancedHelper(root.left)
    if leftHeight == -1:
        return -1
    # call recursively for right subtree
    rightHeight = isBalancedHelper(root.right)
    if rightHeight == -1:
        return -1
    
    if abs(rightHeight - leftHeight) > 1:
        return -1
    
    return max(leftHeight, rightHeight) + 1
    
def isBalanced(root):
    return isBalancedHelper(root) > -1

N1 = Node("N1")
N2 = Node("N2")
N3 = Node("N3")
N4 = Node("N4")
N5 = Node("N5")
N6 = Node("N6")
N1.left = N2
N1.right = N3
N2.left = N4
N2.right = N5
N3.right = N6

print(isBalanced(N1))


















