

class Node:
    def __init__(self, value=None):
        self.previous = None
        self.value = value
        self.next = None
        
class DobulyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        
    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next
    
    # CREATION OF DOUBLY LINKED LIST
    def create(self, nodeValue):
        node = Node(nodeValue)
        self.head,self.tail = node,node
        print('Double Linked List created!')
        
    # Insert new Node 
    def insert(self, nodeValue,nodeLocation):
        if not self.head: return print('Double Linked List does not exist!')
        newNode = Node(nodeValue)
        if nodeLocation == 0:
            newNode.next = self.head
            self.head.previous = newNode
            self.head = newNode
        elif nodeLocation == -1:
            newNode.previous = self.tail
            self.tail.next = newNode
            self.tail = newNode
        else:
            previousNode = self.head
            for i in range(nodeLocation-1):
                previousNode = previousNode.next
            
            newNode.previous,newNode.next = previousNode,previousNode.next
            previousNode.next,newNode.next.previous = newNode, newNode
            
    # Traverse through doubly linked list
    def traverse(self, reverse=False):
        if not self.head: return print('List is empty!')
        node = self.head if not reverse else self.tail
        while node:
            print(node.value)
            node = node.next if not reverse else node.previous
            
    # Searching node inside doubly linked list
    def search(self, nodeValue):
        if not self.head: return print('List is empty!')
        node = self.head
        while node:
            if node.value == nodeValue: return print(f'{nodeValue} is inside list')
            node = node.next
        print(f'{nodeValue} is not inside list')
        
    # DELETING NODE FROM DOUBLY LINKED LIST
    def delete(self, nodeLocation):
        if not self.head: return print('List is empty!')
        if nodeLocation == 0:
            if self.head == self.tail:
                self.head,self.tail = None, None
            else:
                self.head = self.head.next
                self.head.previous = None
        elif nodeLocation == -1:
            if self.head == self.tail:
                self.head,self.tail = None, None
            else:
                self.tail = self.tail.previous
                self.tail.next = None
        else:
            node = self.head
            for i in range(nodeLocation - 1):
                node = node.next
            node.next = node.next.next
            node.next.previous = node
        
        
    # Clear entire list 
    def clear(self):
        if not self.head: return print('List is empty!')
        node = self.head
        while node:
            node.previous,node.next,node = None,None,node.next
        self.head,self.tail = None,None


# Create doubly linked list 
doublyLinkedList = DobulyLinkedList()
doublyLinkedList.create(4)

print([node.value for node in doublyLinkedList])

# Insert new element into doublyLinkedList
doublyLinkedList.insert(2,0)
doublyLinkedList.insert(3,-1)
doublyLinkedList.insert(7,1)
print([[None if not node.previous else node.previous.value ,node.value, None if not node.next else node.next.value] for node in doublyLinkedList])

# Traverse through list
doublyLinkedList.traverse()
doublyLinkedList.traverse(reverse=True)

# Search if node is inside list
doublyLinkedList.search(1)

# Delete node from list
# doublyLinkedList.delete(-1)
# print([[None if not node.previous else node.previous.value ,node.value, None if not node.next else node.next.value] for node in doublyLinkedList])

# Clear list
doublyLinkedList.clear()
print([node.value for node in doublyLinkedList])

