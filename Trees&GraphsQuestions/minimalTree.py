

# Minimal Binary Search Tree

# Given a sorted (increasing order) array with unique integer elemenst, write an algorithm to create a binary search tree with minimal height


class BSTNode:
    def __init__(self, data=None, left = None, right= None):
        self.data = data
        self.left = left
        self.right = right
    
    def display(self):
        lines, *_ = self._display_aux()
        for line in lines:
            print(line)

    def _display_aux(self):
        """Returns list of strings, width, height, and horizontal coordinate of the root."""
        # No child.
        if self.right is None and self.left is None:
            line = '%s' % self.data
            width = len(line)
            height = 1
            middle = width // 2
            return [line], width, height, middle

        # Only left child.
        if self.right is None:
            lines, n, p, x = self.left._display_aux()
            s = '%s' % self.data
            u = len(s)
            first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s
            second_line = x * ' ' + '/' + (n - x - 1 + u) * ' '
            shifted_lines = [line + u * ' ' for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, n + u // 2

        # Only right child.
        if self.left is None:
            lines, n, p, x = self.right._display_aux()
            s = '%s' % self.data
            u = len(s)
            first_line = s + x * '_' + (n - x) * ' '
            second_line = (u + x) * ' ' + '\\' + (n - x - 1) * ' '
            shifted_lines = [u * ' ' + line for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, u // 2

        # Two children.
        left, n, p, x = self.left._display_aux()
        right, m, q, y = self.right._display_aux()
        s = '%s' % self.data
        u = len(s)
        first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s + y * '_' + (m - y) * ' '
        second_line = x * ' ' + '/' + (n - x - 1 + u + y) * ' ' + '\\' + (m - y - 1) * ' '
        if p < q:
            left += [n * ' '] * (q - p)
        elif q < p:
            right += [m * ' '] * (p - q)
        zipped_lines = zip(left, right)
        lines = [first_line, second_line] + [a + u * ' ' + b for a, b in zipped_lines]
        return lines, n + m + u, max(p, q) + 2, n + u // 2

def minimalTree(sortedArray):
    # To solve this problem we would use AVL tree
    # If list is sorted we can use that to create tree faster
    # - first we can set middle element as rootnode (all left element are smaller so it will be leftsubtree and right rightsubtree)
    # - then continue with similar logic for left and right subtree (find middle element and so on...)
    if len(sortedArray) == 0: 
        return None
    if len(sortedArray) == 1: 
        return BSTNode(sortedArray[0])
    # # middle sortedArray element
    rootNode = len(sortedArray)//2
    # #run algorithm recursively for right and left subtree
    leftSubtree = minimalTree(sortedArray[:rootNode])
    rightSubtree = minimalTree(sortedArray[rootNode+1:])
    return BSTNode(sortedArray[rootNode], leftSubtree, rightSubtree)


sortedArray = [1,2,3,4,5,6,7,8,9]
binarySearchTree = minimalTree(sortedArray)
binarySearchTree.display()

'''
Final Result

   _5__  
  /    \ 
  3    8
 / \  / \
 2 4  7 9
/    /
1    6
'''

sortedArray = [1,2,3,4,5,6,7,8,9,10,11, 12, 13, 14, 15, 16, 17, 18, 19, 20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55]
binarySearchTree = minimalTree(sortedArray)
binarySearchTree.display()
'''
Final Result

                   __________________________28___________________________
                  /                                                       \
       __________14_____________                             ____________42_____________
      /                         \                           /                           \
    __7_____               ____21_______               ____35_______               ____49_______
   /        \             /             \             /             \             /             \
  _4_    __11___       __18___       __25___       __32___       __39___       __46___       __53___
 /   \  /       \     /       \     /       \     /       \     /       \     /       \     /       \
 2   6  9_     13    16_     20    23_     27    30_     34    37_     41    44_     48    51_     55
/ \ /  /  \   /     /   \   /     /   \   /     /   \   /     /   \   /     /   \   /     /   \   /
1 3 5  8 10  12    15  17  19    22  24  26    29  31  33    36  38  40    43  45  47    50  52  54
'''
