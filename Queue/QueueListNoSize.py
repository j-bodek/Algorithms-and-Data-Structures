 
# Queue created with list without size limit
# Problem with this queue is shifting element in list after dequeueing
# It takes O(n) times complexity to enqueue element and dequeue element

class Queue:
    def __init__(self):
        self.items = []
        
    def __str__(self):
        if not self.items: return 'Queue does not exist'
        values = [str(item) for item in self.items]
        return '-'.join(values)
    
    # isEmtpy method 
    def isEmpty(self):
        if not self.items: 
            return True
        else:
            return False
        
    # Enqueue method 
    def enqueue(self, value):
        self.items.append(value) # append element at the end of the queue
        return 'Element added to queue!'
    
    # Dequeue method
    def dequeue(self): # this method take O(n) time complexity
        if self.isEmpty(): return print('Queue is empty')
        return self.items.pop(0)
    
    # Peek method
    def peek(self):
        if self.isEmpty(): return print('Queue is empty')
        return self.items[0]
    
    # Delete method
    def delete(self):
        self.items = None
        
        
# Create queue
queue = Queue()
# check if queue is empty
print(queue.isEmpty())
# enqueue elements
queue.enqueue(4)
queue.enqueue(52)
queue.enqueue(41)
# check if queue is empty
print(queue.isEmpty())
print(queue)
# Dequeue element
print(f'Dequeued value => {queue.dequeue()}')
print(queue)
# Print peek of queue
print(f'Peek value => {queue.peek()}')
#Delete queue
queue.delete()
print(queue)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
        