

# QUESTION 3. WRITE CODE TO PARTITION A LINKED LIST AROUND A VALUE X, SUCH THAT ALL NODES LESS THAN X 
# COME BEFORE ALL NODES GREATER THAN OR EQUAL TO X

from customeLinkedList import LinkedList

def partition(linkedList, x):
    node = linkedList.head
    linkedList.tail = linkedList.head
    while node:
        nextNode = node.next
        if node.value < x:
            node.next = linkedList.head 
            linkedList.head = node
        else:
            linkedList.tail.next = node
            linkedList.tail = node
        node = nextNode

linkedList = LinkedList()
linkedList.generate(6,0,6)
print(linkedList)
partition(linkedList, 3)
print(linkedList)


