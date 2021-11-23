

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