

# QUESTION 4. YOU HAVE TWO NUMBERS REPRESENTED BY A LINKED LIST, WHERE EACHNODE CONTAINS A SINGLE DIDGIT.
# THE DIITS ARE STORED IN REVERSE ORDER, SUCH THAT 1'S DIGIT IS AT THE HEAD OF THE LSIT. WRITE A FUNCTION 
# THAT ADDS THE TWO NUMBERS AND RETURNS THE SUM AS A LINKED LIST.

from customeLinkedList import LinkedList

def sumList(listA, listB):
    nodeA, nodeB = listA.head, listB.head
    new_list_values = LinkedList()
    division = 0
    while nodeA:
        new_list_values.add((nodeA.value + nodeB.value + division) % 10)
        division = (nodeA.value + nodeB.value + division)//10
        nodeA,nodeB = nodeA.next, nodeB.next
    print(new_list_values)
    
    
def sumList2(listA, listB):
    sumValue = int(''.join([str(node.value) for node in listA][::-1])) + int(''.join([str(node.value) for node in listB][::-1]))
    new_list_values = LinkedList()
    for node in str(sumValue):
        new_list_values.add(node)
    print(new_list_values)

    
listA = LinkedList()
listA.generate(3,5,9)
listB = LinkedList()
listB.generate(3,5,9)
print(listB)
print(listA)
sumList(listA,listB)
sumList2(listB,listA)
