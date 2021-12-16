


'''
Selection Sort
'''
# - In case of selection sort we repeatedly find the minimum element and move it to the sorted part of array to make usorted part sorted

# example
#  sorted   | unsorted
#           | 5,7,4,3
#  sorted   | unsorted  
#  3        | 5,7,4    (3 is minimum element)
#  sorted   | unsorted  
#  3,4      | 5,7      (4 is minimum element)
#  sorted   | unsorted  
#  3,4,5    | 7        (5 is minimum element)
#  sorted   | unsorted  
#  3,4,5,7  |          (7 is minimum element)



# SELECTION SORT FUNCTION
def selectionSort(unsortedList, reverse=False): # time complexity is O(n^2), space complexity is O(1)
    for index in range(len(unsortedList)):
        min_or_max_index = index
        for sortIndex in range(index+1, len(unsortedList)):
            if not reverse and unsortedList[min_or_max_index] > unsortedList[sortIndex]:
                min_or_max_index = sortIndex
            if reverse and unsortedList[min_or_max_index] < unsortedList[sortIndex]:
                min_or_max_index = sortIndex
                
        #Swap min_or_max element 
        unsortedList[index],unsortedList[min_or_max_index] = unsortedList[min_or_max_index], unsortedList[index]

    print(unsortedList)
        
sortList = [3,1,4,5,2]
selectionSort(sortList, reverse=True)
selectionSort(sortList)



'''
When to use Selection sort
'''
# - When we have insufficient memory
# - Easy to implement
'''
When to avoid Selection Sort
'''
# - When time is a concern










































