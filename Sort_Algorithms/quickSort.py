


'''
Quick Sort
'''
# - Quick sort is a divide and conquer algorithm 
# - Find pivot number and make sure smaller numbers located at the left of pivot and bigger numbers are located at the right of the pivot
# - Unlike merge sort extra space is not required


# Example
# 70, 10, 80, 30, 90, 40, 60, 20, 50 <= take most right number as pivot and place all greater elements then it to the right and less to to left
# 10, 30, 40, 20, 50, 80, 60, 70, 90 <= then take as pivot right element from left subtree (20)
# 10, 20, 40, 30, 50, 80, 60, 70, 90 <= then take next right element from left subtree (30)
# 10, 20, 30, 40, 50, 80, 60, 70, 90 <= leftSubtree is complete now take right element from right subtree (90)
# 10, 20, 30, 40, 50, 80, 60, 70, 90 <= 90 is considered as sorted so take next element (70)
# 10, 20, 30, 40, 50, 60, 70, 80, 90 <= then check 60 and 80 to ensure they are fully sorted



# Helper function: place pivot in right position in array (all greater elements in right and smaller in left)
def partition(customList, firstIndex, lastIndex): # Time Complexity => O(n) , Space Complexity => O(n)
    pivot = customList[lastIndex]
    leftMarker = firstIndex - 1
    for rightMarker in range(firstIndex, lastIndex):
        if customList[rightMarker] <= pivot:
            # increase place where is last element less then pivot
            leftMarker += 1
            customList[leftMarker], customList[rightMarker] = customList[rightMarker], customList[leftMarker]
            
    # And at the end swap place with the element at index of the most right smaller element then pivot plus 1 and pivot
    customList[leftMarker+1], customList[lastIndex] = customList[lastIndex], customList[leftMarker+1]
    #return place where pivot currently is
    return leftMarker+1


def quickSort(unsortedList, firstIndex, lastIndex): # Time Complexity => O(nlogn), Space Complexity => O(n)
    if firstIndex < lastIndex:
        # get index of pivot after placeing it in good position
        pivotIndex = partition(unsortedList, firstIndex, lastIndex) # ==> O(n)
        # Then do quicksort on right and left sublist
        quickSort(unsortedList, firstIndex, pivotIndex-1) #we dont want to sort pivot index 
        quickSort(unsortedList, pivotIndex+1, lastIndex)
        
    return unsortedList

sortList = [3,1,4,5,2]
print(quickSort(sortList, 0, 4))



'''
When to use Quick sort
'''
# - When average expected time is O(nlogn)
'''
When to avoid Insertion Sort
'''
# - When space is a concern
# - When you need stable sort

























