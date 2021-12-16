

'''
Merge Sort
'''
# - merge sort is a divide and conquer algorithm 
# - divide the input array in two halves and we keep halving recursively until they become too small that sannot be broken furhter
# - merge halves by sortign them

# Example:
# [6,4,3,7,5]
# [6,4,3] [7,5] #divide array
# [6,4] [3] [7] [5] #divide arrays
# [6] [4] [3] [7] [5] #divide arrays
# then merge them in order they were divided
# [4,6] [3] [7] [5]
# [3,4,6] [5,7]
# [3,4,5,6,7]

# helper function
def merge(unsortedList, firstIndex, middleIndex, lastIndex):
    numberLeft = middleIndex - firstIndex + 1 #number of elements in left half
    numberRight = lastIndex - middleIndex #number of elements in right half
    Left = [unsortedList[firstIndex+indexLeft] for indexLeft in range(0, numberLeft)]
    Right = [unsortedList[indexRight+middleIndex+1] for indexRight in range(0, numberRight)]
    
    
    indexLeft,indexRight,indexMarge = 0,0,firstIndex
    while indexLeft < numberLeft and indexRight < numberRight:
        if Left[indexLeft] <= Right[indexRight]:
            unsortedList[indexMarge] = Left[indexLeft]
            indexLeft += 1
        else:
            unsortedList[indexMarge] = Right[indexRight]
            indexRight += 1
            
        indexMarge += 1
        
    # if one of them is less then number of elements in corresponding list
    while indexLeft < numberLeft:
        unsortedList[indexMarge] = Left[indexLeft]
        indexLeft += 1
        indexMarge += 1
    while indexRight < numberRight:
        unsortedList[indexMarge] = Right[indexRight]
        indexRight += 1
        indexMarge += 1
    

def mergeSort(unsortedList, firstIndex, lastIndex): #Time complexity O(nLogN), space complexity O(n)
    if firstIndex < lastIndex:
        middle = (firstIndex+(lastIndex-1))//2
        mergeSort(unsortedList, firstIndex, middle)
        mergeSort(unsortedList, middle+1, lastIndex)
        #Then we need to merge divided lists
        merge(unsortedList, firstIndex, middle, lastIndex)
    return unsortedList



sortList = [3,1,4,5,2]
print(mergeSort(sortList, 0, 4))


'''
When to use Merge sort
'''
# - When you need stable sort
# - When average expected time is O(nlogn)
'''
When to avoid Insertion Sort
'''
# - When space is a concern
















