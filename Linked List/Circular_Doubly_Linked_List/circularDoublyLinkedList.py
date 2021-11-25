

class Node:
    def __init__(self, value=None):
        self.previous = None
        self.value = value
        self.next = None
        
class CircularDobulyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        
    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next
            if node == self.tail.next: break
    
    # CREATION OF CIRCULAR DOUBLY LINKED LIST
    def create(self, nodeValue):
        node = Node(nodeValue)
        node.next, node.previous = node, node
        self.head, self.tail = node, node
        
    # INSERT NEW NODE TO DOUBLY LINKED LIST
    def insert(self, nodeValue, nodeLocation):
        if not self.head: return print('List does not exist!')
        newNode = Node(nodeValue)
        if nodeLocation == 0:
            newNode.next, newNode.previous = self.head, self.tail
            self.head.previous, self.tail.next = newNode, newNode
            self.head = newNode
        elif nodeLocation == -1:
            newNode.next, newNode.previous = self.head, self.tail
            self.tail.next, self.head.previous = newNode, newNode
            self.tail = newNode
        else:
            previousNode = self.head
            for i in range(nodeLocation-1):
                previousNode = previousNode.next
            
            newNode.previous, newNode.next = previousNode, previousNode.next
            previousNode.next.previous, previousNode.next = newNode, newNode
            
    # TRAVERSE THROUGH CIRCULAR DOUBLY LINKED LIST
    def traverse(self, reverse=False):
        if not self.head: return print('List is empty!')
        node = self.head if not reverse else self.tail
        while True: 
            print(node.value)
            node = node.next if not reverse else node.previous
            if (node == self.head and not reverse) or (node == self.tail and reverse):break
            
    # SEARCHING NODE
    def search(self, nodeValue):
        if not self.head: return print('List is empty!')
        node = self.head
        while True:
            if node.value == nodeValue: return print(f'{nodeValue} exist in list')
            if node == self.tail: break
            node = node.next
        print(f'{nodeValue} does not exist in list')
        
    # DELETEING NODE FROM CIRCULAR DOUBLY LINKED LIST
    def delete(self, nodeLocation):
        if not self.head: return print('List is empty!')
        if nodeLocation == 0:
            if self.head == self.tail: 
                self.head, self.tail, self.head.next, self.head.previous = None, None, None, None
            else:
                self.head, self.tail.next = self.head.next, self.head.next
                self.head.previous = self.tail
        if nodeLocation == -1:
            if self.head == self.tail:
                self.head, self.tail, self.head.next, self.head.previous = None, None, None, None
            else:
                self.tail,self.head.previous = self.tail.previous, self.tail.previous
                self.tail.next = self.head
        else:
            previousNode = self.head
            for i in range(nodeLocation-1):
                previousNode = previousNode.next
            previousNode.next, previousNode.next.previous = previousNode.next.next, previousNode
                
    # CLEAR ENTIRE LIST
    def clear(self):
        if not self.head: return print('List is empty!')
        node = self.head
        while node:
            node.next, node = None, node.next
            if node == self.head:break
        self.head.previous = None
        self.head, self.tail = None, None
            
        
        
        
        
# Create new linked list
circularDobulyLinkedList = CircularDobulyLinkedList()
circularDobulyLinkedList.create(5)
print([[node.previous.value,node.value,node.next.value] for node in circularDobulyLinkedList])

# insert element to linked list
circularDobulyLinkedList.insert(2,0)
circularDobulyLinkedList.insert(3,-1)
circularDobulyLinkedList.insert(9,1)
print([[node.previous.value,node.value,node.next.value] for node in circularDobulyLinkedList])

# Traverse the circular doubly linked list 
circularDobulyLinkedList.traverse()
circularDobulyLinkedList.traverse(reverse=True)

# Searching node in circular doubly linked list
circularDobulyLinkedList.search(10)

# Delete node from circular doubly linked list
circularDobulyLinkedList.delete(-1)
print([[node.previous.value,node.value,node.next.value] for node in circularDobulyLinkedList])

# Clear list 
circularDobulyLinkedList.clear()
print([[None if not node.previous.value else node.previous.value,node.value,None if not node.next.value else node.next.value] for node in circularDobulyLinkedList])




