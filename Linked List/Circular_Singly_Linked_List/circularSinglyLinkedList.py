
# CIRCULAR SINGLY LINKED LIST

class Node:
    def __init__(self,value=None):
        self.value = value
        self.next = None

class CircularSinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        
    # function to make linked list printable
    # __iter__ function makes SinglyLinkedList iterable !!!!!!
    def __iter__(self):
        node = self.head #start from first node
        while node:
            yield node #return node
            if node.next == self.head: break # break after interate through entire list
            node = node.next #asign node to next node
    
    # CREATION OF CIRCULAR SINGLY LINKED LIST
    def create(self, nodeValue):
        node = Node(nodeValue)
        node.next = node
        self.head,self.tail = node,node
        
    # INSERT ELEMENT TO SINGLY LINKED LIST
    def insert(self, nodeValue, nodeLoction):
        if not self.head: 
            print('List is empty!')
        elif nodeLoction == 0: # insert new node to first position
            newNode = Node(nodeValue)
            newNode.next = self.head
            self.head,self.tail.next = newNode,newNode
        elif nodeLoction == -1: # insert new node to last position
            newNode = Node(nodeValue)
            previousNode = self.tail
            newNode.next = previousNode.next
            previousNode.next = newNode
            self.tail = newNode
        else:
            newNode = Node(nodeValue)
            previousNode = self.head
            for i in range(nodeLoction-1):
                previousNode = previousNode.next
            newNode.next = previousNode.next
            previousNode.next = newNode
            
            
    # TRAVERSE CIRCULAR SINGLY LINKED LIST 
    def traverse(self):
        if not self.head: return print('List is empty!')
        node = self.head
        while node:
            print(node.value)
            if node.next == self.head: break
            node = node.next

    # SEARCHING ELEMENT IN CIRCULAR SINGLY LINKED LIST
    def search(self,searchNode):
        if not self.head: return print('List is empty!')
        node = self.head
        while node:
            if node.value == searchNode: return print(f'{searchNode} exist in list!')
            if node.next == self.head: return print(f'{searchNode} does not exist in list!')
            node = node.next
        
    # DELETE SINGLE NODE FROM CIRCULAR SINGLY LINKED LIST
    def delete(self, nodeLoction):
        if not self.head: return print('List is empty!')
        if nodeLoction == 0:
            if self.head == self.tail: 
                self.head.next,self.head,self.tail = None,None,None
            elif self.head != self.tail: 
                self.head = self.head.next
                self.tail.next = self.head
        elif nodeLoction == -1:
            if self.head == self.tail: 
                self.head.next,self.head,self.tail = None,None,None
            elif self.head != self.tail: 
                previousNode = self.head
                while previousNode.next != self.tail:
                    previousNode = previousNode.next
                previousNode.next = self.head
                self.tail = previousNode
        else:
            previousNode = self.head
            for i in range(nodeLoction-1):
                previousNode = previousNode.next
            previousNode.next = previousNode.next.next

    # CLEAR ENTIRE CIRCULAR SINGLY LINKED LIST
    def clear(self):
        self.head,self.tail.next,self.tail = None,None,None







circularSinglyLinkedList = CircularSinglyLinkedList()
circularSinglyLinkedList.create(2)

print([node.value for node in circularSinglyLinkedList])

#Insert new Node
circularSinglyLinkedList.insert(6,0) #insert to first position
circularSinglyLinkedList.insert(9,-1) #insert to last position
circularSinglyLinkedList.insert(3,2) #insert to second position
print([node.value for node in circularSinglyLinkedList])

# Traverse circular singly linked list
circularSinglyLinkedList.traverse()

# Search element in circular singly linked list
circularSinglyLinkedList.search(7)

# Delete node from circular singly linked list
circularSinglyLinkedList.delete(1)
print([node.value for node in circularSinglyLinkedList])

# Clear list
circularSinglyLinkedList.clear()
print([node.value for node in circularSinglyLinkedList])


