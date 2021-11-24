

# SINGLY LINKED LIST

class Node:
    def __init__(self,value=None):
        self.value = value
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        
    # function to make linked list printable
    # __iter__ function makes SinglyLinkedList iterable !!!!!!
    def __iter__(self):
        node = self.head #start from first node
        while node:
            yield node #return node
            node = node.next #asign node to next node
            
    def insert(self, value, location):
        newNode = Node(value)
        if not self.head:
            self.head = newNode
            self.tail = newNode
        else:
            
            if location == 0: #inserting to begining
                newNode.next = self.head #asign next node to head (later it will be second node)
                self.head = newNode # then asign newNode to head
                
            elif location == -1: #inserting element to the end of list
                newNode.next = None
                self.tail.next = newNode # asing new node as next for previous
                self.tail = newNode # asign to last position
                
            else:
                # traverse through list to get node before location that we want to insert newNode
                previousNode = self.head
                for i in range(location-1):
                    previousNode = previousNode.next
                    
                nextNode = previousNode.next
                newNode.next = nextNode # asign nextNode as newNode next
                previousNode.next = newNode # asign newNode as previousNode next
                
                if previousNode == self.tail:
                    self.tail = newNode
                             
                    
    # TRAVERSE SINGLY LINKED LIST 
    def traverseSinglyLinkedList(self):
        if not self.head:
            print('Single linked list does not exist')
        else:
            node = self.head
            while node:
                print(node.value)
                node = node.next
                
    # SEARCHING ELEMENT IN SINGLY LINKED LIST
    def searchElement(self, element):
        if not self.head:
            print(f'{element} does not exist in list')
        else:
            node = self.head
            while node:
                if node.value == element: 
                    print(f'{node.value} exist in list!')
                    break
                else:
                    node = node.next
            print(f'{element} does not exist in list')
            
    # DELETE NODE IN SINGLY LINKED LIST
    def delete(self, element_location):
        if not self.head:
            print('Single linked list is empty')
        else:
            if element_location == 0: # deleting first element
                if self.head == self.tail: #only one node in list
                    self.head,self.tail = None,None
                else:
                    self.head = self.head.next
            elif element_location == -1: # deleting last element
                if self.head == self.tail: #only one node in list
                    self.head,self.tail = None,None
                else:
                    node = self.head
                    while node:
                        if node.next == self.tail: break
                        node = node.next
                    node.next = None
                    self.tail = node
            else: # deleting any index element
                previousNode = self.head
                for i in range(element_location-1):
                    previousNode = previousNode.next
                
                deleteNode = previousNode.next
                previousNode.next = deleteNode.next
                
    # CLEAR LINKED LIST
    def clear(self):
        if not self.head:
            print('Single linked list is empty!')
        else:
            self.head,self.tail = None,None
            
        
        
# create new empty linked list and nodes
singlyLinkedList = SinglyLinkedList()

# insert 1 to first position in linked list
singlyLinkedList.insert(1, 0) 

# insert 5 to last position in linked list
singlyLinkedList.insert(5, -1) 

# insert 8 to second position in linked list
singlyLinkedList.insert(8, 1) 

# print linked list elements 
print([node.value for node in singlyLinkedList])

# Traverse through list
singlyLinkedList.traverseSinglyLinkedList()

# Search for element in list
singlyLinkedList.searchElement(9)

# Delete element in list
singlyLinkedList.delete(0)
print([node.value for node in singlyLinkedList])

# Delete entire singly list (clear list)
singlyLinkedList.clear()
print([node.value for node in singlyLinkedList])


