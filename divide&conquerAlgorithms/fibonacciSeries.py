

# FIBONACCI SERIES
# Definition: a series of numbers in which each number is the sum of the two preceding numbers. First two 
# numbers by definition are 0 and 1

# Example: 0,1,1,2,3,5,8,13
# fibonacci(n) = fibonacci(n-1) + fibonacci(n-2)

def fibonacci(n):
    if n <= 2: return ['error',0,1][n]
    return fibonacci(n-1) + fibonacci(n-2)













