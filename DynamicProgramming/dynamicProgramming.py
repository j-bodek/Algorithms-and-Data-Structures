

'''
What is Dynamic Programming
'''
# Dynamic programming is an algorithmic technique for solving an optimization problem by
# breaking it down into simpler subproblems and utilizing the fact that the optimal solution to the overall
# problem depends upon the optimal solution to its subproblems


# Example:
# 1 + 1 + 1 + 1 + 1 + 1 + 1  = 7

# ___________7_____________
# 1 + 1 + 1 + 1 + 1 + 1 + 1 + 2  =  7 + 2 = 9  Remember solution from previous problem and use this answer


'''
Dynamic Programming Properties
'''
# OPTIMAL SUBSTRUCTURE:
#   - If any problem's overall optimal solution can be constructed from the optimal solutions of its subproblem then this porblem has optimal substructure

# OVERLAPPING SUBPROBLEM
#   - Subproblems are smaller versions of the original problem. Any provlem has overlapping sub-problems if finding its solution involves solving the same subproblem multiple times


'''
Top Down with Memorization
'''
# Solve the bigger problem by recursively finding the solutino to smaller subproblems. Whenever we solve a 
# sub-prbolem, we cache its result so that we don't end up solving it repeatedly if it's called multiple 
# times. This technique of storing the results of already solved subproblems is called Memoization.

# Example: 
# During calculating fibonacci series with recursive function we calculate fibonacci for same 
# numbers multiple time so time complexity takes O(c^n)
# to solve this problem using dymanic programming we will save value for fibbonaci sequence 

def fibonacciMamoization(n, memo):
    if 0 < n <=2:
        return [0,1][n-1]
    if n not in memo:
        memo[n] = fibonacciMamoization(n-1, memo) + fibonacciMamoization(n-2, memo)
    return memo[n]

myDict = {}
print(f'Fibonacci for 6 (with Top Down approach) => {fibonacciMamoization(6,myDict)}')



'''
Bottom Up with Tabulation
'''
# Tabulation is the opposite of the top-down approach and avoids recursion. In this approach, we solve the
# problem 'bottom-up' (by solving all the related subproblems first). This is done by filling up a table. 
# Based on the results in the table, the solution to the top/original problm is then computed.

# It start from smaller problem then countinue to bigger one
def fibonacciTabulation(n):
    table = [0,1]
    for i in range(2,n):
        table.append(table[i-1]+table[i-2])
    return table[-1]

print(f'Fibonnaci for 6 (with Botton Up with tabulation) => {fibonacciTabulation(6)}')


'''
Top Down vs Bottom Up 


Problem             Divide and Conquer    |   Top Down    |  Bottom Up   
Fibonacci numbers        O(c^n)           |     O(n)      |    O(n)


Top Down:
    - Easyness - Easy to come up with solution as it is extension of divide and conquer
    - Runtime - Slow (couse we use recursion)
    - Space Efficientcy - Unnecessary use of stack space
    - When to use - Need a quick solution
    
Bottom Up:
    - Dificult to come up with solution 
    - Runtime - Fast
    - Space Efficiency - Stack is not used
    - When to use = Need an efficient solution
'''

'''
Is Merge Sort is Dynamic Programming?
'''
# We devide harder problem into multiple smaller and then combine them with each other - Optimal substructure property
# But merge sort does not have overlapping subproblems property - each subproblem is independent and none of them does not repeat
# So merge sort can be solved using divide and conquer algorithm but not DYNAMIC PROGRAMMING


'''
Dynamic Programming - Number Factor problem
'''
# PROBLEM STATEMENT 
# Given N, find the number of ways to express N as a sum of 1,3,4

# Example 
# N = 4
# number of ways = 4
# 4, [1,3] [3,1] [1,1,1,1]

# After examining probem we can see that:
# numberFactor(n) = numberFactor(n-1) + numberFactor(n-3) + numberFactor(n-4)
# So in bigger n subproblems will repeat 

def numberFactorTopDown(N, memo):
    if N in (0,1,2):
        return 1
    elif N == 3:
        return 2
    elif N not in memo:
        memo[N] = numberFactorTopDown(N-1, memo) + numberFactorTopDown(N-3, memo) + numberFactorTopDown(N-4, memo)
    return memo[N]

myDict = {}
print(f'Number of Factor for 5 (with top down approach) => {numberFactorTopDown(5,myDict)}')


def numberFactorBottomUp(N):
    factors = [1,1,1,2]
    if N < 4:
        return factors[N]
    
    for i in range(4,N+1):
        factors[0], factors[1], factors[2], factors[3] = factors[1], factors[2], factors[3], factors[3] + factors[1] + factors[0]
    return factors[3]

print(f'Number of Factor for 5 (with Bottm Up) => {numberFactorBottomUp(5)}')



'''
House Robber with Dynamic programming
'''
# Problem Statement:
#   - Given N number of houses along the street with some amount of money
#   - Adjacent houses cannot be stolen
#   - Find the maximum amount that can be stolen

# Example 
# [6]  [7]  [1]  [30]  [8]  [2]  [4]  
# Answer amount = 41
# Houses that are stolen: 7+41+4 = 41

def houseRobberTopDown(houses, currentHouse, memo):
    if currentHouse >= len(houses):
        return 0
    elif currentHouse not in memo:
        stealFirstHouse = houses[currentHouse] + houseRobberTopDown(houses, currentHouse+2, memo)
        skipFirstHouse = houseRobberTopDown(houses, currentHouse+1, memo)
        memo[currentHouse] = max(stealFirstHouse, skipFirstHouse)
    return memo[currentHouse]

myDict = {}
houses = [6,7,1,30,8,2,4]
print(f'House Robber with Top Down => {houseRobberTopDown(houses, 0, myDict)}')


# HOUSE ROBBER PROBLEM WITH DOWN UP 
def houseRobberDownUp(houses, currentHouse):
    stolenAmount = [0]*(len(houses)+2)
    for i in range(len(houses)-1,currentHouse-1,-1):
        stolenAmount[i] = max(stolenAmount[i+1], houses[i] + stolenAmount[i+2])
        pass
    return max(stolenAmount)

print(f'House Robber with Down Up => {houseRobberDownUp(houses, 0)}')



'''
Convert String to another one using Dynamic Programming
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

def convertStringTopDown(string1, string2, indexFirstString, indexSecondString, memo):
    if indexFirstString == len(string1): #we reach end of string1 so we need to delete rest characters from string2
        return len(string2)-indexSecondString
    if indexSecondString == len(string2): #we reach end of string2 so we need to insert rest of characters from string1
        return len(string1)-indexFirstString
    if string1[indexFirstString] == string2[indexSecondString]: # if characters are same skip
        return convertStringTopDown(string1, string2, indexFirstString+1, indexSecondString+1, memo)
    elif (indexFirstString, indexSecondString) not in memo:
        # during deletion we take index from first string and go to second string
        deleteOperation = 1 + convertStringTopDown(string1, string2, indexFirstString, indexSecondString+1, memo) 
        insertOperation = 1 + convertStringTopDown(string1, string2, indexFirstString+1, indexSecondString, memo) 
        replaceOperation = 1 + convertStringTopDown(string1, string2, indexFirstString+1, indexSecondString+1, memo)
    
        memo[(indexFirstString, indexSecondString)] = min(deleteOperation, replaceOperation, insertOperation)
    return memo[(indexFirstString, indexSecondString)]

myDict = {}
print(f'Convert tbrltt -> table with Top Down => {convertStringTopDown("table","tbrltt",0,0, myDict)}')



# CONVERT STRING WITH DOWN UP
def convertStringDownUp(string1, string2, tempDict):
    tempDict.update(dict(zip([str(x)+'0' for x in range(len(string1)+1)],list(range(len(string1)+1)))))
    tempDict.update(dict(zip(['0'+str(x) for x in range(len(string2)+1)],list(range(len(string2)+1)))))
    
    for index1 in range(1, len(string1)+1):
        for index2 in range(1, len(string2)+1):
            if string1[index1-1] == string2[index2-1]:
                dictKey = str(index1)+str(index2)
                dictKey1 = str(index1-1)+str(index2-1)
                tempDict[dictKey] = tempDict[dictKey1]
            else:
                dictKey = str(index1)+str(index2)
                dictKeyD = str(index1-1)+str(index2)
                dictKeyI = str(index1)+str(index2-1)
                dictKeyR = str(index1-1)+str(index2-1)
                
                tempDict[dictKey] = 1 + min(tempDict[dictKeyI], tempDict[dictKeyR], tempDict[dictKeyD])

    dictKey = str(len(string1))+str(len(string2))
    return tempDict[dictKey]


print(f'Convert tbrltt -> table with Down Up => {convertStringDownUp("table","tbrltt",{})}')



'''
Zero One Knapsack Problem
'''
# Problem Statement:
#   - Given the weights and profits of N items
#   - Find the maximum profit within given capacity of C
#   - Items cannot be broken

# Example:
# ITEMS:
#   - mango: weight-3, profit-31
#   - apple: weight-1, profit-26
#   - orange: weight-2, profit-17
#   - banana: weight-5, profit-72

# KNAPSACK CAPACITY: 7

# Subproblems:
#   - Option1: take first item and continue to next items
#   - Option2: skip first and take next ones

# Zero one knapsack problem does not have overlapping subproblems so dynamic programming 
# wouldn't perform better then divide and conquer algorithms











