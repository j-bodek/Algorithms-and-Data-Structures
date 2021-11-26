from random import randint

# General Linked List
class Node:
    def __init__(self, value=None):
        self.previous = None
        self.value = value
        self.next = None

    def __str__(self): # __str__  function returns a string representation (this method will be called when we print the node)
        return str(self.value)


class LinkedList:
    def __init__(self, values=None):
        self.head = None
        self.tail = None
        
    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next
            
    def __str__(self):
        values = [str(node.value) for node in self]
        return ' -> '.join(values)

    def __len__(self):
        return sum([1 for node in self])

    def add(self, value):
        if self.head is None:
            newNode = Node(value)
            self.head, self.tail = newNode, newNode
        else:
            self.tail.next = Node(value)
            self.tail = self.tail.next
        return self.tail

    def generate(self, elementNumber, min_value, max_value):
        self.head, self.tail = None, None
        for i in range(elementNumber):
            self.add(randint(min_value,max_value))
        return self
    
# customeLinkedList = LinkedList()
# customeLinkedList.generate(10,0,19)
# print(customeLinkedList)
# print(len(customeLinkedList))

















