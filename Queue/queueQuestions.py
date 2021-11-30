

# QUESTION 1. QUEUE VIA STACKS
# IMPORTANT QUEUE CLASS WHICH IMPLEMENTS A QUEUE USING TWO STACKS


class Stack:
    def __init__(self):
        self.list = []
    def __iter__(self):
        for i in self.list:
            yield i
    def __len__(self):
        return len(self.list)
    def push(self,value):
        self.list.append(value)
    def pop(self):
       if not self.list: return None
       return self.list.pop()  


class QueueViaStacks:
    def __init__(self):
        self.inStack = Stack()
        self.outStack = Stack()
    def __str__(self):
        return '-'.join([str(item) for item in self.inStack])
    def enqueue(self,value):
        self.inStack.push(value)
    def dequeue(self):
        if not self.inStack: return None
        while len(self.inStack) > 1:
            self.outStack.push(self.inStack.pop())
        dqueuedElement = self.inStack.pop()
        while len(self.outStack):
            self.inStack.push(self.outStack.pop())
        return dqueuedElement

queue = QueueViaStacks()
queue.enqueue(3)
queue.enqueue(5)
queue.enqueue(9)
print(queue)
print(f'Dequeue method => {queue.dequeue()}')
print(queue)



print('-----------------------------------QUESTION_2-----------------------------')


# QUESTION 2. ANIMAL SHELTER - AN ANIMAL SHELTER, WHICH HOLDS ONLY DOGS AND CATS, OPERATES ON A STRICTLY 
# 'FIRST IN, FIRST OUT' BASIS. PEOPLE MUST ADOPT EITHER THE 'OLDEST' (BASED ON ARIVAL TIME) OF ALL ANIMALS AT 
# SHELTER, OR THEY CAN SELECT WHETER THEY WOULD PREFER A DOG OR A CAT (AND WILL RECEIVE THE OLDEST OF THAT TYPE)
# THEY CANNOT SELECT WHICH SPECIFIC ANIMAL THEY WOULD LIKE. CREATE THE DATA STRUCTURES TO MAINTAIN THIS SYSTEM 
# AND IMPLEMENT OPERATIONS SUCH AS ENQUEUE, DEQUEUEANY, DEQUEUEDOG, AND DEQUEUECAT

import random

class AnimalShelter():
    def __init__(self):
        self.cats = []
        self.dogs = []
        
    def __str__(self):
        return 'Dogs => ' + '-'.join(self.dogs) + '\n' + 'Cats => ' + '-'.join(self.cats)
        
    def enqueue(self, animal, type):
        if type == 'Cat': self.cats.append(animal)
        if type == 'Dog': self.dogs.append(animal)

    def dequeueCat(self):
        if not self.cats: return None
        return self.cats.pop(0)
    def dequeueDog(self):
        if not self.dogs: return None
        return self.dogs.pop(0)
    def dequeueAny(self):
        choices = [choice for choice in [self.dogs,self.cats] if choice]
        if len(choices) == 1:
            animalType = choices[0]
            return animalType.pop(0)
        elif len(choices) > 1:
            animalType = choices[random.randint(0,1)]
            return animalType.pop(0)
        else:
            return None
            

shelter = AnimalShelter()
shelter.enqueue('C1','Cat')
shelter.enqueue('D1','Dog')
shelter.enqueue('C2','Cat')
shelter.enqueue('D2','Dog')
shelter.enqueue('D3','Dog')
shelter.enqueue('C3','Cat')
print(shelter)  

print(f'Dequeue Cat => {shelter.dequeueCat()}')
print(f'Dequeue Dog => {shelter.dequeueDog()}')
print(f'Dequeue Any => {shelter.dequeueAny()}')

print(shelter)
 






































































