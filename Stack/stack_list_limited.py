

# stack with limit

class Stack:
    def __init__(self, maxSize):
        self.maxSize = maxSize
        self.list = []
        
    def __str__(self): # function to print stack verticaly
        if self.isEmpty(): return 'Stack is empty'
        values = [str(x) for x in reversed(self.list)]
        return '\n'.join(values)
    
    # isEmpty method 
    def isEmpty(self):
        if not self.list: 
            return True 
        else:
            False
            
    # isFull
    def isFull(self):
        if len(self.list) == self.maxSize:
            return True 
        else:
            return False
    
    # Push method 
    def push(self, value):
        if self.isFull(): return print('Stack is full') 
        self.list.append(value)
        print('Element appended to stack')
        
    # Pop method
    def pop(self):
        if not self.list: return print('Stack is empty')
        return self.list.pop()
    
    # Peek method
    def peek(self):
        if not self.list: return print('Stack is empty')
        return self.list[-1]
    
    # delete method
    def delete(self):
        self.list = None
        
        
stack = Stack(3)
print(stack.isEmpty())
stack.push(2)
stack.push(7)
stack.push(1)
print(stack)
print(stack.isFull())