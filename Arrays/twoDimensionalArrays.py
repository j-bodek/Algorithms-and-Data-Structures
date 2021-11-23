import numpy as np 

# CREATING TWO DIMENSIONAL ARRAYS

#Day 1 - 11, 15, 10, 6
#Day 2 - 15, 12, 15, 19
#Day 3 - 1, 6, 21, 2
#Day 4 - 6, 8, 12, 5

twoDArray = np.array([[11, 15, 10, 6],
                    [15, 12, 15, 19],
                    [1, 6, 21, 2],
                    [6, 8, 12, 5]])

newTwoDArray = np.insert(twoDArray, 1, [[1,2,3,4]], axis=1) # add new column to second position
newTwoDArray = np.insert(newTwoDArray, 0, [[5,6,7,8,9]], axis=0) # add new row to first position
newTwoDArray = np.append(newTwoDArray, [[3,1,6,1,2]], axis=0) # add new row to first position
print(newTwoDArray)


# ACCESSING ELEMENTS OF TWO DIMENSIONAL ARRAYS

def accessElements(array, rowIndex, colIndex):
    if rowIndex >= len(array) or colIndex >= len(array[0]):
        return 'Index out of range' 
    else:
        return array[rowIndex][colIndex]
    
print(accessElements(twoDArray,2,3))


# TRAVERSAL TWO DIMENSIONAL ARRAYS

returnAllIndexes = lambda array,element: [(row,col) for row in range(len(array)) for col in range(len(array[0])) if array[row][col] == element]
print(returnAllIndexes(newTwoDArray,1))

# DELETION - TWO DIMENSIONAL ARRAYS
newTwoDArray = np.delete(newTwoDArray, 0, axis=0) # delete first row in newTwoDArray
newTwoDArray = np.delete(newTwoDArray, 2, axis=1) # delete third column in newTwoDArray
print(newTwoDArray)


# time and space complexity in two dimsnsional arrays 

#    Operation                      |    Time complexity    |    Space complexity   |
#------------------------------------------------------------------------------------
#    Creating an empty array        |     O(1)              |         O(mn)          |
#------------------------------------------------------------------------------------
#    Inserting a value in an array  |     O(1)/O(mn)         |         O(1)          |
#------------------------------------------------------------------------------------
#    Taversing a given array        |     O(mn)              |         O(1)          |
#------------------------------------------------------------------------------------
#    Accessing a given cell         |     O(1)              |         O(1)          |
#------------------------------------------------------------------------------------
#    Searching a given value        |     O(mn)              |         O(1)          |
#------------------------------------------------------------------------------------
#    Deleting a given value         |     O(1)/O(mn)         |         O(1)          |
#------------------------------------------------------------------------------------


#   WHEN TO USE / AVOID ARRAYS

# USE:
# - To store multiple varialbes of same data type
# - Random access 
# AVOID: 
# - Same data type elements 
# - Reserve memory 







