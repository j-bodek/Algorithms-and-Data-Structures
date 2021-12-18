

# List of Depths
# Given a binary search tree, design an algorithm which creates a linked list of all the nodes at each depth 
# (ie, if you have a tree with depth D, you'll have D linked lists)

'''
Example:

  _1_    linked list: 1
 /   \   
 2   3   linked list: 2 -> 3
/ \ / \
4 5 6 7  linked list: 4 -> 5 -> 6 -> 7

To solve this problem we use pre order traversal (first start from root then leftsubtree and after finishing it continue to right subtree)
During traversing check depth of tree to see on which level ot tree is current element
'''



class LinkedList:
    def __init__(self, val):
        self.val = val
        self.next = None
    
    def add(self, val):
        if self.next == None:
            self.next = LinkedList(val)
        else:
            self.next.add(val)
    def __str__(self):
        return "({val})".format(val = self.val) + str(self.next)  #str will call recursively

class BinaryTree:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

    
def depth(tree):
    if not tree:
        return 0
    if not tree.left and not tree.right:
        return 1
    else:
        depthLeft = 1 + depth(tree.left)
        depthRight = 1 + depth(tree.right)
        return max(depthLeft, depthRight)

def treeToLinkedList(tree, custDict = {}, treeDepth = None):
    if not treeDepth: 
        treeDepth = depth(tree)
    if treeDepth not in custDict: 
        custDict[treeDepth] = LinkedList(tree.val)
    else:
        custDict[treeDepth].add(tree.val)
        if treeDepth == 1: return custDict
        
    # now make pre order traversal
    if tree.left:
        custDict = treeToLinkedList(tree.left, custDict, treeDepth-1)
    if tree.right:
        custDict = treeToLinkedList(tree.right, custDict, treeDepth-1)
    return custDict
        
mainTree = BinaryTree(1)
two = BinaryTree(2)
three = BinaryTree(3)
four = BinaryTree(4)
five = BinaryTree(5)
six = BinaryTree(6)
seven = BinaryTree(7)

mainTree.left = two
mainTree.right = three
two.left = four
two.right = five
three.left = six
three.right = seven

customdictionary = treeToLinkedList(mainTree)
for depthLevel, linkedList in customdictionary.items():
    print(f'{depthLevel} : {linkedList}')


'''
  _1_    linked list: 1
 /   \   
 2   3   linked list: 2 -> 3
/ \ / \
4 5 6 7  linked list: 4 -> 5 -> 6 -> 7
'''







