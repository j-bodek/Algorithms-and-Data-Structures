

'''
First Common Ancestor
'''
# Design an algorithm and write code to find the first common ancestor of two nodes in a binary tree
# Avoid storing additional nodes in a data structure. NOTE: This is not necessarily a binary search tree


'''
Example:

             ___________55________      
            /                     \     
      _____44______                77
     /             \        
   _22___       __99__     
  /      \     /      \   
 35     88    90      95   
       /        \  
     54          33  

First common ancestor of 33 and 88 ?
first common ancestor is 44

Game plan:
- Create function that check if node exist in rightsubtree or leftsubtree
- traverse with this function through nodes of tree and check if both nodes exists and tree starting from specific rootNode
- last rootNode that meet conditions that both nodes exists in tree is first common ancestor


'''



class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.right = right
        self.left = left
        

def checkNodeInTree(target, rootNode):
    if not rootNode: return False
    if target == rootNode: 
        return True
    # else check left and right subtrees
    else:
        return (checkNodeInTree(target, rootNode.left), checkNodeInTree(target, rootNode.right))


def findFirstCommonAncestor(n1,n2,root):
    n1OnRight = checkNodeInTree(n1, root.right)
    n2OnRight = checkNodeInTree(n2, root.right)
    
    # Exclusive or operator => ^
    # True ^ False => return True
    # True ^ True => return False
    # False ^ True => return True
    # False ^ False => return False
    
    if n1OnRight ^ n2OnRight:
        return root
    
    # if both are true call method recursively
    else:
        if n1OnRight:
            return findFirstCommonAncestor(n1,n2, root.right)
        else:
            return findFirstCommonAncestor(n1,n2, root.left)
    















