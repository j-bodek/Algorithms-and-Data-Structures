

# Python Collections Module
# methods:  
# - deque()
# - append()
# - popleft()
# - clear()

from collections import deque

print('---------------------QUEUE_WITH_COLLECTIONS_MODULE---------------------')


# Deque method (create queue)
queue = deque(maxlen = 4) # after reaching max length it's overwrite elements
print(queue)

# Append method
queue.append(43)
queue.append(21)
queue.append(61)
print(queue)

# Popleft method
print(f'Popleft method => {queue.popleft()}')
print(queue)

# Clear method
queue.clear()
print(queue)



# Python Queue Module
# methods:  
# - qsize()
# - empty()
# - full()
# - put()
# - get() - return first element of the queue (like pop)
# - task_done() - Indicate that a formerly enqueued task is complete
# - join() - Block until all items in the queue have been received and processed

import queue as q


print('---------------------QUEUE_WITH_QUEUE_MODULE---------------------')

# Create a queue
queue = q.Queue(maxsize = 3) #after reaching max size of elements it would append new ones
# empty method
print(f'Is queue empty => {queue.empty()}')
# qsize method
print(f'qsize method => {queue.qsize()}')
# Put method
queue.put(31)
queue.put(73)
queue.put(47)
# full method
print(f'Is queue full => {queue.full()}')
# get method
print(f'Get method => {queue.get()}')




# Python Multiprocessing Module
# methods:  
# - qsize()
# - empty()
# - full()
# - put()
# - get() - return first element of the queue (like pop)

from multiprocessing import Queue

print('---------------------QUEUE_WITH_MULTIPROCESSING_MODULE---------------------')

#Create queue
queue = Queue(maxsize = 3) #after reaching max size of elements it would append new ones
# empty method
print(f'Is queue empty => {queue.empty()}')
# Put method 
queue.put(32)
# full method
print(f'Is queue full => {queue.full()}')
# get method
print(f'Get method => {queue.get()}')











