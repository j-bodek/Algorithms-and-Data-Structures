

# Stack created using liked lists 
class Node:
    def __init__(self,value = None):
        self.next = None
        self.value = value
    
    
class LinkedList:
    def __init__(self):
        self.head = None
        
    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next
        
        
class Stack:
    def __init__(self):
        self.LinkedList = LinkedList() # Create stack using linked list
        
    def __str__(self):
        values = ['['+str(node.value)+']' for node in self.LinkedList]
        return '\n'.join(values)
        
    # isEmpty method 
    def isEmpty(self):
        if not self.LinkedList.head: 
            return True 
        else: 
            return False

    # Push method 
    def push(self, value):
        node = Node(value)
        node.next = self.LinkedList.head
        self.LinkedList.head = node # insert node at the begining of the linked list
        
    # Pop method 
    def pop(self):
        if self.isEmpty(): return print('Stack is empty')
        popedValue,self.LinkedList.head = self.LinkedList.head.value,self.LinkedList.head.next
        return popedValue
    
    # Peek method
    def peek(self):
        if self.isEmpty(): return print('Stack is empty')
        return self.LinkedList.head.value
    
    # Delete method
    def delete(self):
        self.LinkedList.head = None
        


stack = Stack() 
stack.push(83)
stack.push(14)
stack.push(51)
print(stack)
print(f'Poped value => {stack.pop()}')
print(stack)
print(f'Peek Value => {stack.peek()}')






