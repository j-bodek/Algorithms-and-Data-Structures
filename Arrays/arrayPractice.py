from array import *

# 1. Create an array and traverse

my_array = array('i', [1,3,6,7,9]) 

for i in my_array:
    print(i) 
    
# 2. Access individual elements through indexes 
print('-------------------- Step 2 --------------------')
print(my_array[0])

# 3. Append any value to the array using append() method
my_array.append(4)
print('-------------------- Step 3 --------------------')
print(my_array)
    
# 4. Insert value in an array using insert() method
my_array.insert(3,12)
print('-------------------- Step 4 --------------------')
print(my_array)
    
# 5. Extend python array using extend() method
my_array_to_extend = array('i', [15,12,13])  
my_array.extend(my_array_to_extend)
print('-------------------- Step 5 --------------------')
print(my_array)

# 6. Add items from list inot array using fromList() method
tempList = [12,124,123]
my_array.fromlist(tempList)
print('-------------------- Step 6 --------------------')
print(my_array)

# 7. Remove any array elemtn using remove() method
my_array.remove(7)
print('-------------------- Step 7 --------------------')
print(my_array)
    
# 8. Remove last array element using pop() method
my_array.pop()
print('-------------------- Step 8 --------------------')
print(my_array)

# 9. Fatch any element through its index using index() method
print('-------------------- Step 9 --------------------')
print(my_array.index(12))

# 10. Reverse a python array using reverse() method
print('-------------------- Step 10 --------------------')
my_array.reverse()
print(my_array)

# 11. Get array buffer information through buffer_info() method
print('-------------------- Step 11 --------------------')
print(my_array.buffer_info()) #first element is array starting point in memeory, the second is amount of elements 

# 12. Check for number of occurrences of any element using count() method 
print('-------------------- Step 12 --------------------')
print(my_array.count(12))

# 13. Convert array to bytes using tobytes() method
print('-------------------- Step 13 --------------------')
strTemp = my_array.tobytes()
print(strTemp)

# 14. Convert array to a python list with same elements using tolist() method
print('-------------------- Step 14 --------------------')
print(my_array.tolist())

# 15. Append a bytes to char array using frombytes() method
print('-------------------- Step 15 --------------------')
ints = array('i')
ints.frombytes(strTemp)
print(ints)

# 16. Slice elements from an array 
print('-------------------- Step 16 --------------------')
print(my_array[1:4])
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    