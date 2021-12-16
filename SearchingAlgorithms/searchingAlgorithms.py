


'''
Linear Search
'''
# Linear Search check element one by one and return true if element is what we are looking for
# Linear Search is good for unsorted Data but if data is sorted it perform poorly

def linearSearch(lookingElement, array):
    for element in array:
        if element is lookingElement: return True
    return False

data = [1,43,5,6,8,2,3,4]
print(linearSearch(6,data))



'''
Binary Search
'''
# - Binary Search is faster than linear search
# - half of the remaining elements can be eliminated at a time, instead of eliminating them one by one
# !!!IMPORTANT!!! - Binary search work only on sorted data

import math

def binarySearch(lookingElement, array):
    startPointer = 0
    endPointer = len(array)-1
    middlePointer = math.floor(endPointer/2)
    i = 0
    
    while array[middlePointer] is not lookingElement and startPointer <= endPointer:
        if lookingElement < array[middlePointer]:
            endPointer = middlePointer - 1
        if lookingElement > array[middlePointer]:
            startPointer = middlePointer + 1   
        middlePointer = math.floor((startPointer+endPointer)/2)
        if array[middlePointer] is lookingElement: return True

    return False
        
    
array = [1,2,3,4,5,6,7,8,9]
print(binarySearch(6,array))




'''
Binary Search Time complexity 

Worst And Average Cost:     
O(logn)
'''



































