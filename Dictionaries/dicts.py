
# DICTIONARY METHODS

myDict = {'name':'Edy', 'age':31, 'address':'london', 'education':'master'}

# copy() copy original dictionary and return copy of dict
copiedDict = myDict.copy()
print(copiedDict)

# clear() clear dictionary
myDict.clear()
print(myDict)

# fromkeys() - create new dictionary from keys and values provided
newDict = {}.fromkeys(['new1','new2'], 'value')
print(newDict)

# get() return value for specified key if key is in dictionary
print(copiedDict.get('name', 'Unknown')) # if name is not in dictionary it will print 'Unknown'

# items() = return dict items

# keys() - return list of keys 

# values() - return list of values 

# popitem() - return and remove last item from dictionary
print(copiedDict.popitem())
print(copiedDict)

# setdefault() - return value of key if key is in dictionary, if not it insert key to dictionary
copiedDict.setdefault('education', 'master') #if key is not specified it will insert key to dictionary and value 'master'

# pop() - return and remove element by specified key
copiedDict.pop('age','age not in dictionary') 

# update() - append elements from another dictionary if key are in dictionary it will update them
updateDict = {'age':'41', 'updated':'True'}
copiedDict.update(updateDict)
print(copiedDict)




##############################################################################################
#############              DICTIONARY OPERATIONS/BUILD IN FUNCTIONS              #############
##############################################################################################

# in operator
print('name' in copiedDict)

# for loop

# all() - return true if all values are True 
print(all(copiedDict))

# any() - return true if any element is true else it return false
print(any(copiedDict))

# sorted() - return dictionary by keys
# syntax:  sorted(iterable, reverse, key)
print(sorted(copiedDict, reverse=True, key = lambda key: copiedDict[key])) # copiedDict sorted by values and reversed






































