

# QUESTION 2. IMPLEMENT AN ALGORITHM TO FIND THE NTH TO LST ELEMENT OF A SINGLY LIKED LIST 
# RETURN ELEMENT THAT IS LOCATED NTH STEPS FROM THE LAST ELEMENT

from customeLinkedList import LinkedList

def nthLast(linkedList, n):
    # lets solve this problem using two pointer one starting from head and second nth steps from head
    # we move them simultaneously until second one reach tail and then first will be nth steps from last elements
    
    pointer1,pointer2 = linkedList.head, linkedList.head 
    
    #Move pointer2
    for i in range(n):
        pointer2 = pointer2.next
    
    # Move both pointers till second one reach tail 
    while pointer2:
        pointer2, pointer1 = pointer2.next, pointer1.next
    
    return pointer1
    
def nthLast2(linkedList, n):
    pointer = linkedList.head
    for i in range(len(linkedList)-n):
        pointer = pointer.next
    return pointer

linkedList = LinkedList()
linkedList.generate(10,0,5)
print(linkedList)
print(nthLast(linkedList,3))
print(nthLast2(linkedList,3))











