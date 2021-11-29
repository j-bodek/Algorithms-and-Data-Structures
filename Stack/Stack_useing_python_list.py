

# Stack made with python list 

class Stack:
    def __init__(self):
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
            return False

    # Push method 
    def push(self, value):
        self.list.append(value)
        
    # Pop method 
    def pop(self):
        if self.isEmpty(): return 'Stack is empty!'
        return self.list.pop()
    
    # Peek method (method that return element on the top of the stack)
    def peek(self):
        if self.isEmpty(): return 'Stack is empty!'
        return self.list[-1]
    
    # Delete entire stack 
    def delete(self):
        self.list = None
        

stack = Stack()
#Check if stack is empty 
print(stack.isEmpty())
# Push element to stack
print('Push')
stack.push(2)
stack.push(7)
stack.push(9)
print(stack)
# Pop element from stack
print('Pop')
print(stack.pop())
print(stack)
# Peek method 
print('Peek')
print(stack.peek())
print(stack)
#Delete stack
stack.delete()
print(stack)



















































