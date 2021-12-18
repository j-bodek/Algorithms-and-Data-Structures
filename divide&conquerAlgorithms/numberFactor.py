

'''
Number Factor Problem
'''
# Given number N, find the number of ways to express N as a sum of 1, 3, 4

# Example 
# N = 4
# number of ways = 4
# 4, [1,3] [3,1] [1,1,1,1]

# to find NumberFactor(6) we can divide it to subproblems

# NumberFactor(6) = NumberFactor(6-1) + NumberFactor(6-3) + NumberFactor(6-4)

def numberFactor(n):
    if n in [0,1,2]:
        return 1
    elif n == 3:
        return 2
    else:
        subProblem1 = numberFactor(n-1)
        subProblem2 = numberFactor(n-3)
        subProblem3 = numberFactor(n-4)
        return subProblem1 + subProblem2 + subProblem3

print(numberFactor(5))















