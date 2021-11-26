

# QUESTION 1. WRITE CODE TO REMOVE DUPLICATES FROM AN USORTED LINKED LIST
from customeLinkedList import LinkedList

def removeDuplicates(linkedList):
    removedDuplicates = []
    for node in linkedList:
        if node.value not in removedDuplicates:removedDuplicates.append(node.value)
    linkedList.head, linkedList.tail = None, None
    for node in removedDuplicates:
        linkedList.add(node)
        
def removeDuplicates2(linkedList):
    if not linkedList.head: return print('linked list is empty')
    
    node = linkedList.head
    while node:
        curentNode = node                                  #|  
        while curentNode.next:                             #|      
            if curentNode.value == curentNode.next.value:  #|  => time complexity = O(n^2)
                curentNode.next == curentNode.next.next    #|     it removes every singly duplicates of one node every iteration     
            else:                                          #|          
                curentNode = curentNode.next               #|          
        node = curentNode.next
        
linkedList = LinkedList()
linkedList.generate(10,1,5)
print(linkedList)

removeDuplicates(linkedList)
print(linkedList)
