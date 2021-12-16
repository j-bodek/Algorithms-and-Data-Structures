



'''
Bubble Sort
'''
# - Bubble sort is also referred as Singking sort
# - We repeatedly compare each pair of adjecent items and swap them if they are in the wrond order

# Bubble sort example (increasing order)
# [6, 4, 1, 7, 3, 5]
# [4, 6, 1, 7, 3, 5]
# [4, 1, 6, 7, 3, 5] <= 7 is greater than 6
# [4, 1, 6, 3, 7, 5]
# [4, 1, 6, 3, 5, 7] <= 7 is fully sorted
# [1, 4, 6, 3, 5, 7]
# [1, 4, 6, 3, 5, 7] <= 6 is greater than 4
# [1, 4, 3, 6, 5, 7]
# [1, 4, 3, 5, 6, 7] <= 6 is fully sorted
# [1, 4, 3, 5, 6, 7] <= 4 is greater than 1
# [1, 3, 4, 5, 6, 7] <= 5 is greater than 4 (list fully sorted because all successive elements are greater then previous ones)


# BUBBLE SORT FUNCTION
def bubbleSort(sortList, reverse=False): # time complexity is O(n^2), space complexity is O(1)
    for element in range(len(sortList)-1):
        for copareElement in range(len(sortList)-element-1):
            if not reverse and sortList[copareElement] > sortList[copareElement+1]:
                sortList[copareElement], sortList[copareElement+1] = sortList[copareElement+1],sortList[copareElement]
            if reverse and sortList[copareElement] < sortList[copareElement+1]:
                sortList[copareElement], sortList[copareElement+1] = sortList[copareElement+1],sortList[copareElement]
    
    print(sortList)


sortList = [3,1,4,5,2]
bubbleSort(sortList, reverse=True)


'''
When to use Bubble sort
'''
# - Whe n the input is already sorted
# - space is a concern
# - Easy to implement
'''
When to avoid Bubble Sort
'''
# - Average time complexity is poor






























