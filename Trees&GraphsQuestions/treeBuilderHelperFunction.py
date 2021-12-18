
# Queue created with linked list

class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None
        
    def __str__(self):
        return str(self.value) 

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    def __iter__(self):
        node = self.head 
        while node:
            yield node
            node = node.next

class Queue:
    def __init__(self):
        self.items = LinkedList()
    
    def __str__(self):
        values = [str(node) for node in self.items if node]
        if not values: return 'Queue is empty'
        return 'start -> ' + '-'.join(values)
    
    # isEmpty method
    def isEmpty(self): # time complexity is O(1)
        if self.items.head == None:
            return True
        else:
            return False
    
    # Enqueue method
    def enqueue(self, value):  # time complexity is O(1)
        newNode = Node(value)
        if not self.items.head:
            self.items.head, self.items.tail = newNode, newNode
        else:
            self.items.tail.next, self.items.tail = newNode, newNode

    # Dequeue method
    def dequeue(self):  # time complexity is O(1)
        if self.isEmpty(): return 'Queue is empty'
        dequeueNode = self.items.head
        if self.items.head == self.items.tail: 
            self.items.head, self.items.tail = None, None
        else:
            self.items.head = self.items.head.next
        return dequeueNode.value

    # Peek method
    def peek(self): # time complexity is O(1)
        if self.isEmpty(): 'Queue is empty'
        return self.items.head.value

    # Delete method
    def delete(self): # time complexity is O(1)
        self.items.head, self.items.tail = None, None



class binaryTree:
    def __init__(self,data):
        self.left = None
        self.data = data
        self.right = None
        
    def insert(self, newNode):
        if not self: return
        customeQueue = Queue()
        customeQueue.enqueue(self)
        while not customeQueue.isEmpty():
            root = customeQueue.dequeue()
            if root.left:
                customeQueue.enqueue(root.left)
            if root.right:
                customeQueue.enqueue(root.right)
            if not root.left:
                root.left = binaryTree(newNode)
                return
            if not root.right:
                root.right = binaryTree(newNode)
                return
                
        
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




newBinaryTree = binaryTree('55')
newBinaryTree.insert('44')
newBinaryTree.insert('77')
newBinaryTree.insert('22')
newBinaryTree.insert('99')
newBinaryTree.insert('-')
newBinaryTree.insert('-')
newBinaryTree.insert('35')
newBinaryTree.insert('88')
newBinaryTree.insert('90')
newBinaryTree.insert('95')
newBinaryTree.insert('-')
newBinaryTree.insert('-')
newBinaryTree.insert('-')
newBinaryTree.insert('-')
newBinaryTree.insert('-')
newBinaryTree.insert('-')
newBinaryTree.insert('54')
newBinaryTree.insert('-')
newBinaryTree.insert('-')
newBinaryTree.insert('33')
newBinaryTree.insert('-')
newBinaryTree.insert('-')
newBinaryTree.insert('-')
newBinaryTree.insert('-')
newBinaryTree.insert('-')
newBinaryTree.insert('-')
newBinaryTree.insert('-')
newBinaryTree.insert('-')

# newBinaryTree.insert('N4')
# newBinaryTree.insert('N5')
# newBinaryTree.insert('N6')

newBinaryTree.display()

