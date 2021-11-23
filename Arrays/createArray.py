from array import * 

arr1 = array('i', [1,2,3,4]) # array type integer (and only integer can be inside of it) 

arr1.insert(0,7)

# array traversion

def traverseArray(array):
    for i in array:  
        print(i)
        
def accessElement(array, index):
    return 'There is not any element in this index' if index > len(array)-1 else array[index]


# search if element exists inside array
def searchInArray(array, value):
    for i in array: 
        if i == value:
            return array.index(value) 
    return 'The element does not exists in this array'

# delete element from the array 
arr1.remove(7) 
 
 
# time and space complexity in one dimsnsional arrays 

#    Operation                      |    Time complexity    |    Space complexity   |
#------------------------------------------------------------------------------------
#    Creating an empty array        |     O(1)              |         O(N)          |
#------------------------------------------------------------------------------------
#    Inserting a value in an array  |     O(1)/O(n)         |         O(1)          |
#------------------------------------------------------------------------------------
#    Taversing a given array        |     O(n)              |         O(1)          |
#------------------------------------------------------------------------------------
#    Accessing a given cell         |     O(1)              |         O(1)          |
#------------------------------------------------------------------------------------
#    Searching a given value        |     O(n)              |         O(1)          |
#------------------------------------------------------------------------------------
#    Deleting a given value         |     O(1)/O(n)         |         O(1)          |
#------------------------------------------------------------------------------------


