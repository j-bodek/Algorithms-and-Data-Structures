

'''
Insertion Sort
'''
# - Divide the given array into two part (sorted and unsorted)
# - Take first element from usorted array and find its correct position in sorted array
# - Repeat until unsorted array is empty

#Example:

#  sorted   | unsorted
#           | 5,7,4,3
#  sorted   | unsorted
#  5        | 7,4,3    (take first element and compare it with elements in sorted array)
#  sorted   | unsorted
#  3,5      | 7,4      (take first element and compare it with elements in sorted array)
#  sorted   | unsorted
#  3,5,7    | 4        (take first element and compare it with elements in sorted array)
#  sorted   | unsorted
#  3,4,5,7  |          (take first element and compare it with elements in sorted array)

# !!!IMPORTANT!!! During comparing element from unsorted array we compare it with elements from sorted 
# array but starting from the right side


# INSERTION SORT FUNCTION

def insertionSort(unsortedList, reverse=False): # Time complexity => O(n^2), Space complexity => O(1)
    for index in range(len(unsortedList)):
        currentElement = unsortedList[index]
        sortedIndex = index - 1
        while (sortedIndex >= 0 and currentElement < unsortedList[sortedIndex] and not reverse) or (sortedIndex >= 0 and currentElement > unsortedList[sortedIndex] and reverse):
            unsortedList[sortedIndex+1] = unsortedList[sortedIndex]
            # Decrease sortedIndex
            sortedIndex -= 1
        unsortedList[sortedIndex+1] = currentElement
    print(unsortedList)
            

sortList = [3,1,4,5,2]
insertionSort(sortList)
insertionSort(sortList,reverse=True)




'''
When to use Insertion sort
'''
# - When we have insufficient memory
# - Easy to implement
# - When we have continuous inflow of numbers and we want to keep them sorted
'''
When to avoid Insertion Sort
'''
# - When time is a concern


























