

# WHAT IS BINARY HEAP
# Binary heap is tree with following properties:
# - a binary heap is either max heap or min heap. In min binary heap, the key at the end of the
# root must be minimum among all keys present in Binary Heap. The same property 
# must be recursibely true for all nodes in Ba\inary Tree. 
# - It's a complete tree (all levels are completly filled except possibly the last level and
# the last level has all keys as left as possible). This property of Binary Heap makes them suitable to be stored in an array.


# TYPES OF BINARY HEAP:
# - Min heap - the value of each node is less than or equal the value of both its children
# - Max heap - it is excatly the oposite of min heap that is the value of each node is more than or equal to the value of both its children


# MIN BINARY HEAP EXAMPLE:
#          |5|  
#        /    \
#     |10|    |20|
#    /   \
# |30|   |40|

# MAX BINARY HEAP EXAMPLE:
#          |40|  
#        /    \
#     |30|    |20|
#    /   \
# |20|   |10|


# WHY WE NEED A BINARY HEAP?
# Find the minimum or maximum number among a set of numbers in logN time. And also we want to make sure that inserting additional
# number does not take more than O(logN) time

# Possible solutions:
# - Store the numbers in sorted array (finding smallest number will take O(1) but inserting O(n))
# - Store the numbers in lined list in sorted manner (finding smallest number will take O(1) but inserting O(n))
# - Binary heap (finding smalles number O(1) inserting O(logN))

# Pratical Use of Binary Heap:
# - Prim's Algorithm
# - Heap Sort
# - Priority Queue


# COMMON OPERATIONS ON BINARY HEAP
# - Creation of Binary Heap
# - Peak top of Binary Heap
# - Extract Min / Extract Max
# - Traversal of binary heap
# - Size of binary Heap
# - Insert value in Binary Heap
# - Delete the entire Binary Heap


# TIME AND SPACE COMPLEXITY OF BINARY HEAP
#-------------------------------------------------------------------------------------------------------
# Create Binary Heap     Time Complexity => O(1)    Space Complexity => O(n)
#-------------------------------------------------------------------------------------------------------
# Peek of Binary Heap     Time Complexity => O(1)    Space Complexity => O(1)
#-------------------------------------------------------------------------------------------------------
# Size of Binary Heap     Time Complexity => O(1)    Space Complexity => O(1)
#-------------------------------------------------------------------------------------------------------
# Traversal of Binary Heap     Time Complexity => O(n)    Space Complexity => O(1)
#-------------------------------------------------------------------------------------------------------
# Insert a node to Binary Heap     Time Complexity => O(logN)    Space Complexity => O(LogN)
#-------------------------------------------------------------------------------------------------------
# Extract a node from Binary Heap     Time Complexity => O(logN)    Space Complexity => O(LogN)
#-------------------------------------------------------------------------------------------------------
# Delete entire Binary Heap     Time Complexity => O(1)    Space Complexity => O(1)




# IMPLEMENTATIONS OPERATIONS
# - Array Implementation
# - Referance / pointer implementation

class Heap:
    def __init__(self, size):
        self.list = size * [None]
        self.heapSize = 0
        self.maxSize = size + 1 
        
        
    
def peek(rootNode):
    if not rootNode: return 
    return rootNode.list[1] # return first element of list (0 index is none)

def size(rootNode):
    if not rootNode: return 0
    return rootNode.heapSize

# binary heap has 3 types of traversals (same as binary tree)
def levelOrderTraversal(rootNode):
    if not rootNode.list: return print('Binary Heap does not exist!')
    for node in rootNode.list[1: rootNode.heapSize+1]:
        print(node)
        

# helper method for insertion which swap insertNode with parent nodes
def heapifyTreeInsert(rootNode, index, heapType):
    # find parent node of inserted node (by index)
    parentIndex = index//2
    if index <= 1: return
    if heapType == 'Min':
        if rootNode.list[parentIndex] > rootNode.list[index]:
            # swap nodes
            rootNode.list[parentIndex],rootNode.list[index] = rootNode.list[index],rootNode.list[parentIndex]
        # call heapifyTreeInsert method recursively
        heapifyTreeInsert(rootNode, parentIndex, heapType)
    elif heapType == 'Max':
        if rootNode.list[parentIndex] < rootNode.list[index]:
            # swap nodes
            rootNode.list[parentIndex],rootNode.list[index] = rootNode.list[index],rootNode.list[parentIndex]
        # call heapifyTreeInsert method recursively
        heapifyTreeInsert(rootNode, parentIndex, heapType)
    else:
        print('Wrong heapType')
        

def insert( rootNode, value, heapType):
    if rootNode.heapSize + 1 == rootNode.maxSize: return print('Binary heap is full')
    rootNode.list[rootNode.heapSize + 1] = value
    rootNode.heapSize += 1
    heapifyTreeInsert( rootNode, rootNode.heapSize, heapType)
    

# function that swap nodes after node extraction
def heapifyTreeExtract(rootNode, index, heapType):
    leftChildIndex = 2*index
    rightChildIndex = 2*index + 1
    if rootNode.heapSize < leftChildIndex: 
        return #if rootnode does not have childrens
    elif rootNode.heapSize == leftChildIndex:
        if heapType == 'Min':
            if rootNode.list[index] > rootNode.list[leftChildIndex]:
                rootNode.list[index],rootNode.list[leftChildIndex] = rootNode.list[leftChildIndex],rootNode.list[index]
        else:
            if rootNode.list[index] < rootNode.list[leftChildIndex]:
                rootNode.list[index],rootNode.list[leftChildIndex] = rootNode.list[leftChildIndex],rootNode.list[index]
    
    else: # both children
        if heapType == 'Min':
            minChildNode = rootNode.list.index(min(rootNode.list[leftChildIndex], rootNode.list[rightChildIndex]))
            if rootNode.list[index] > rootNode.list[minChildNode]:
                rootNode.list[index],rootNode.list[minChildNode] = rootNode.list[minChildNode],rootNode.list[index]
        else:
            maxChildNode = rootNode.list.index(max(rootNode.list[leftChildIndex], rootNode.list[rightChildIndex]))
            if rootNode.list[index] < rootNode.list[maxChildNode]:
                rootNode.list[index],rootNode.list[maxChildNode] = rootNode.list[maxChildNode],rootNode.list[index]
    
def extract(rootNode, heapType):
    if rootNode.heapSize == 0: return
    extractNode, rootNode.list[1], rootNode.list[rootNode.heapSize] = rootNode.list[1], rootNode.list[rootNode.heapSize], None
    rootNode.heapSize -= 1
    heapifyTreeExtract(rootNode, 1, heapType)
    return extractNode

def deleteHeap(rootNode):
    rootNode.list = None

# Creation of new binary heap
newBinaryHeap = Heap(5)
insert(newBinaryHeap, 4, 'Max')
insert(newBinaryHeap, 7, 'Max')
insert(newBinaryHeap, 5, 'Max')
insert(newBinaryHeap, 2, 'Max')
# HOW OUR BINARY HEAP LOOKS LIKE :
#          |7|  
#        /    \
#     |4|     |5|
#    /  
# |2| 
levelOrderTraversal(newBinaryHeap)

# Extract Node
print('------------------Node_Extraction-------------------')
print(f"Extracted node => {extract(newBinaryHeap, 'Max')}")
levelOrderTraversal(newBinaryHeap)

# Delete Binary Heap
print('------------------Delete_Binary_Heap------------------')
deleteHeap(newBinaryHeap)
levelOrderTraversal(newBinaryHeap)











































