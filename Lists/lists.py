# PYTHON LISTS
# List - data structure that holds an ordered collection of items 

# Accessing/Traversing the list (logic behind list and arrays when it comes to memory is the same)
shoppingList = [0,1,2] 
print(shoppingList[2])

# update/insert list 
shoppingList[2] = 123
shoppingList.insert(1, 'inserted_item')
shoppingList.append('appended_item')
shoppingList.extend(['1','2'])
print(shoppingList)

# Searching list 
if 1 in shoppingList: # this takes O(n) time complexity
    print(shoppingList.index(1))
    
# List operations

a = [1,2,3]
b = [4,5,6]

# concatenate lists
print(a+b)
# repeat elements in list
print(b*3)


# ARRAYS VS LISTS 
#            SIMILARITIES                       |            DIFFERENCES                                                       |    
#   Both dats structures are mutable            |   arrays are for arithmetic operations (arrays are better for computations)  |    
#   Both can be indexed and iterated through    |   data types must be the same in arrays                                      |    
#   They can be both sliced                     |           



def f(i, values = []): # appended elements are staying in values list
    values.append(i)
    print (values)
    return values
f(1)
f(2)
f(3)
