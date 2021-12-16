


'''
Heap Sort
'''
# - Step 1: insert data to binary heap tree
# - Step 2: Extract data from binary heap
# - It is best suited with array, it does not work with linked list


# helper function
def heapify(customList, numberElements, index):
    smallestNumber = index
    leftChild = 2*index +1
    rightChild = 2*index 

    if leftChild < numberElements and customList[leftChild] < customList[smallestNumber]:
        smallestNumber = leftChild
    if rightChild < numberElements and customList[rightChild] < customList[smallestNumber]:
        smallestNumber = rightChild

    if smallestNumber != index:
        #swap smallest number
        customList[smallestNumber],customList[index] = customList[index], customList[smallestNumber]
        #call heapify recursively
        heapify(customList,numberElements,smallestNumber)
        
def heapSort(customList, reverse=False):
    numberElements = len(customList)
    # create heap for first elements
    for index in range((numberElements//2) -1, -1, -1): #start from the last index
        heapify(customList,numberElements,index)
    
    
    for index in range(numberElements-1, 0, -1):
        # swap firt element (smallest) with last element
        customList[index], customList[0] = customList[0], customList[index]
        # and call heapify method but without taking last swaped element into account
        heapify(customList, index, 0)
        
    if not reverse: 
        customList.reverse()
        
        
sortList = [3,1,4,5,2]
heapSort(sortList)
print(sortList)



































