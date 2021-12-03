


# Circular Queue created with python list 

class Queue:
    def __init__(self,maxSize):
        self.items = maxSize * [None] # list with maxSize * None 
        self.maxSize = maxSize
        self.start = -1
        self.top = -1
        
    def __str__(self):
        values = [str(item) for item in self.items if item]
        if not values: return 'Queue is empty'
        return '-'.join(values)

    # isFull method 
    def isFull(self):
        if self.top + 1 == self.start or self.start == self.top - (self.maxSize - 1): 
            return True
        else:
            return False

    # isEmpty method 
    def isEmpty(self):
        if self.top == self.start and self.top == -1:
            return True
        else:
            return False
        
    # Enqueue method
    def enqueue(self, value):
        if self.isFull(): return 'Queue is full!'
        self.top = self.top + 1 if self.top + 1 < self.maxSize else 0
        self.start = self.start if self.start != -1 else 0
        self.items[self.top] = value
        return f'{value} enqueued to queue' 
    
    # Dequeue method 
    def dequeue(self):
        if self.isEmpty(): return print('Queue is empty')
        dequeuedValue,start = self.items[self.start],self.start
        if self.start == self.top:
            self.items,self.start,self.top = self.maxSize*[None],-1,-1
        else:
            self.start = self.start + 1 if self.start + 1 < self.maxSize else 0
        self.items[start]= None
        
        print(f'{dequeuedValue} dequeued from Queue')
        
        
    # Peek method 
    def peek(self):
        if self.isEmpty(): return print('Queue is empty')
        return self.items[self.start]
    
    # Delete method
    def delete(self):
        self.items,self.start,self.top = self.maxSize * [None],-1,-1
        
        
        
        
        

# Create Queue 
queue = Queue(4)
# Check if queue is empty
print(f'Is queue empty? => {queue.isEmpty()}')
# Enqueue elements 
queue.enqueue(37)
queue.enqueue(12)
queue.enqueue(27)
queue.enqueue(53)
print(queue)
#Check if queue is full
print(f'Is queue full? => {queue.isFull()}')
# Dequeue 
queue.dequeue()
print(queue)
# Peek method 
print(f'Peek method => {queue.peek()}')
#Delete method
queue.delete()
print(queue)










