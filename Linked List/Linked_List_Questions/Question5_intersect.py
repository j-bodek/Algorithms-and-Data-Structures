

# QUESTION 5. GIVEN TWO (SINGLY) LINKED LISTS, DETERMINE IF THE TWO LISTS INTERSECT. RETURN THE INTERSECTING NODE. 
# NOTE THAT THE INTERSECTION IS DEFINED BASED ON REFERENCE, NOT VALUE. THAT IS, IF THE KTH NODE OF THE FIRST 
# LINKED LIST IS THE EXCACT SAME NODE (BY REFERENCE) AS THE JTH NODE OF THE SECOND LINKED LIST, 
# THEN THAY ARE INTERSECTING.

from customeLinkedList import LinkedList

def checkIntersection(listA, listB):
    nodeA, nodeB = listA.head, listB.head
    if len(listA) != len(listB):
        steps = abs(len(listA) - len(listB))
        for i in range(steps):
            nodeA = nodeA.next if len(listA) > len(listB) else nodeA
            nodeB = nodeB.next if len(listB) > len(listA) else nodeB
    
    nodeA = nodeA if nodeA else listA.head
    nodeB = nodeB if nodeB else listB.head
    while nodeA or nodeB:
        if nodeA.value == nodeB.value: return print(f'{nodeA.value} is intersection')
        nodeA, nodeB = nodeA.next, nodeB.next

listA = LinkedList()
listA.generate(6,5,9)
listB = LinkedList()
listB.generate(3,5,9)
print(listA)
print(listB)
checkIntersection(listA,listB)