

# QUESTION 1. THREE IN ONE - Describe how you could use a single Python list to implement three stacks

class MultiStack:
    def __init__(self, stacksize):
        self.numberOfStacks = 3
        self.items = [None] * (stacksize*self.numberOfStacks)
        self.sizes = [0] * self.numberOfStacks
        self.stacksize = stacksize
        
    def __str__(self):
        values = [str(item) for item in self.items]
        values = '| ' + '-'.join(values[:self.stacksize]) + ' | ' + '-'.join(values[self.stacksize:2*self.stacksize]) + ' | ' + '-'.join(values[2*self.stacksize:]) + ' |'
        return values
        
    # isFull method 
    def isFull(self, stackNumber):
        if self.sizes[stackNumber] == self.stacksize:
             return True
        else:
            return False
        
    # isEmpty method 
    def isEmpty(self, stackNumber):
        if self.sizes[stackNumber] == 0:
            return True
        else:
            return False
    
    # indexTop method - return the index of the top element from the given stack
    def indexTop(self, stackNumber):
        offset = stackNumber * self.stacksize
        return self.sizes[stackNumber] - 1 + offset

    # Push method
    def push(self, stackNumber, value):
        if self.isFull(stackNumber): return 'Stack is full'
        self.sizes[stackNumber] += 1
        self.items[self.indexTop(stackNumber)] = value
        
    # Pop method
    def pop(self, stackNumber):
        if self.isEmpty(stackNumber): return 'Stack is empty'
        value = self.items[self.indexTop(stackNumber)]
        self.items[self.indexTop(stackNumber)] = None
        self.sizes[stackNumber] -= 1
        return value

    # Peek method
    def peek(self,stackNumber):
        if self.isEmpty(stackNumber): return 'Stack is empty'
        return self.items[self.indexTop(stackNumber)]


# Create method
stack = MultiStack(4)
# isFull method
print(stack.isFull(0))
# isEmpty method
print(stack.isEmpty(2))
stack.push(0,27)
stack.push(1,31)
stack.push(2,51)
print(stack)
# Peek method
print(f'Peek of first stack => {stack.peek(0)}')
# Pop metod
print(f'Pop of third stack => {stack.pop(2)}')
print(stack)






# QUESTION 2. STACK MIN - How would you design a stack which, in addition to push and pop, has a function
# min which return the minimum element? Push, pop and min should all operate in O(1)

print('-----------------------------------QUESTION_2-----------------------------')

# This task can be solved with linked list. To do this each node will have asigned minimum value that is under itself

class Node:
    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next
        
    def __str__(self):
        string = str(self.value)
        if self.next: string += ',' + str(self.next)
        return string


class Stack:
    def __init__(self):
        self.top = None
        self.minNode = None
    
    def min(self):
        if not self.minNode: return None
        return self.minNode.value

    # push method 
    def push(self, value):
        if self.minNode and value > self.minNode.value:
            self.minNode = Node(value = self.minNode.value, next = self.minNode)
        else:
            self.minNode = Node(value = value, next = self.minNode)
        self.top = Node(value = value, next = self.top)
    
    # Pop method
    def pop(self):
        if not self.top: return 'Stack is empty'
        popedValue,self.top,self.minNode = self.top.value,self.top.next,self.minNode.next
        return popedValue
    
stack = Stack()
# Push method
stack.push(5)
stack.push(1)
print(f'Minimum Value => {stack.min()}')
stack.push(78)
stack.push(0)
print(f'Minimum Value => {stack.min()}')
stack.push(9)


# QUESTION 3. STACK OF PLATES - IMAGEIN A (LITERAL) STACK OF PLATES. IF THE STACK GETS TOO HIGH, IT MIGHT TOPPLE.
# THERFORE, IN REAL LIFE, WE WOULD LIKELY START A NEW STACK WHEN THE PREVIOUS STACK EXCEEDS SOME THRESHOLD.
# IMPLEMENT A DATA STRUCTURE SETOFSTACKS THAT MIMICS THIS. SETOFSTACKS SHOULD BE COMPOSED OF SEVERAL
# STACKS AND SHOULD CREATE A NEW STACK ONCE THE PREVOUS ONE EXCEEDS CAPACITY, SETOFSTACKS.PUSH() 
# AND SETOFSTACKS.POP() SHOULD BEHAVE INDENTICALLY TO A SINGLE STACK (THAT IS, POP() SHOULD RETURN THE SAME VALUES
# AS IT WOULD IF THERE WERE JUST A SINGLE STACK).

# FOLLOW UP:
# IMPLEMENT A FUNCTION POPAT(INT INDEX) WHICH PERFORMS A POP OPERATION ON A SPECIFIC SUB - STACK.

print('-----------------------------------QUESTION_3-----------------------------')

class PlateStack:
    def __init__(self, capacity):
        self.capacity = capacity
        self.stacks = []
        
    def __str__(self):
        stacks = [str(stack) for stack in self.stacks]
        return '-'.join(stacks)
    
    def push(self,item):
        if len(self.stacks) > 0 and len(self.stacks[-1]) < self.capacity:
            self.stacks[-1].append(item)
        else:
            self.stacks.append([item])

    def pop(self):
        while len(self.stacks) and len(self.stacks[-1]) == 0:
            self.stacks.pop()
        if len(self.stacks) == 0:
            return None
        else:
            if len(self.stacks[-1]) == 1: return (self.stacks.pop()).pop()
            return self.stacks[-1].pop()


    def pop_at(self, stackNumber):
        while len(self.stacks) and len(self.stacks[-1]) == 0:
            self.stacks.pop()
        if len(self.stacks) > stackNumber:
            return self.stacks[stackNumber].pop()
        else:
            return None
        
        
plateStack = PlateStack(2)
plateStack.push(4)
plateStack.push(1)
plateStack.push(6)
print(plateStack)
print(f'Pop method => {plateStack.pop()}')
print(plateStack)
print(f'Pop at method => {plateStack.pop_at(0)}')
print(plateStack)



























