

# Queue created with linked list

class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None
        
    def __str__(self):
        return str(self.value) 

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    def __iter__(self):
        node = self.head 
        while node:
            yield node
            node = node.next
    

class Queue:
    def __init__(self):
        self.items = LinkedList()
    
    def __str__(self):
        values = [str(node) for node in self.items if node]
        if not values: return 'Queue is empty'
        return 'start -> ' + '-'.join(values)
    
    # isEmpty method
    def isEmpty(self): # time complexity is O(1)
        if self.items.head == None:
            return True
        else:
            return False
    
    # Enqueue method
    def enqueue(self, value):  # time complexity is O(1)
        newNode = Node(value)
        if not self.items.head:
            self.items.head, self.items.tail = newNode, newNode
        else:
            self.items.tail.next, self.items.tail = newNode, newNode

    # Dequeue method
    def dequeue(self):  # time complexity is O(1)
        if self.isEmpty(): return 'Queue is empty'
        dequeueNode = self.items.head
        if self.items.head == self.items.tail: 
            self.items.head, self.items.tail = None, None
        else:
            self.items.head = self.items.head.next
        return dequeueNode.value

    # Peek method
    def peek(self): # time complexity is O(1)
        if self.isEmpty(): 'Queue is empty'
        return self.items.head.value

    # Delete method
    def delete(self): # time complexity is O(1)
        self.items.head, self.items.tail = None, None


# # Create new Queue 
# queue = Queue()
# # Check if queue is empty
# print(f'Is queue empty? => {queue.isEmpty()}')
# #Enqueue element to queue
# queue.enqueue(4)
# queue.enqueue(41)
# queue.enqueue(12)
# print(queue)
# # Dequeue element from queue
# print(f'Dequeued element => {queue.dequeue()}')
# print(queue)
# # Peek element from queue
# print(f'Peek element => {queue.peek()}')



