


'''
Convert String
'''
# PROBLEM STATEMENT
#   - S1 and S2 are given strings
#   - Convert S2 to S1 using delete, insert or replace operations
#   - Find the minimum count of edit operations

# Example 1
# S1 = catche
# S2 = carch
# output = 1
# replace r with t


# We can easily split problem into subproblems by calling each three (delet, insert, replace) operations on S2 letters that different from S1 

def findMinimumOperation(string1, string2, indexFirstString, indexSecondString):
    if indexFirstString == len(string1): #we reach end of string1 so we need to delete rest characters from string2
        return len(string2)-indexSecondString
    if indexSecondString == len(string2): #we reach end of string2 so we need to insert rest of characters from string1
        return len(string1)-indexFirstString
    if string1[indexFirstString] == string2[indexSecondString]: # if characters are same skip
        return findMinimumOperation(string1, string2, indexFirstString+1, indexSecondString+1)

    else:
        # during deletion we take index from first string and go to second string
        deleteOperation = 1 + findMinimumOperation(string1, string2, indexFirstString, indexSecondString+1) 
        
        insertOperation = 1 + findMinimumOperation(string1, string2, indexFirstString+1, indexSecondString) 

        replaceOperation = 1 + findMinimumOperation(string1, string2, indexFirstString+1, indexSecondString+1)
        
        return min(deleteOperation, replaceOperation, insertOperation)
    
    
print(findMinimumOperation("table","tbrltt",0,0))






