
# calculate factorial of n using recurion
# to set larger recursion limit use sys library (sys.setrecurionlimit)

# step 1. - recurive case - the flow 
# step 2. - base case - the stopping criterion 
# step 3. - unintantional case - the constraint (take in account cases like factorial(-2), factorial(7.3) )

def factorial(n):
    # if conditions are not satisfied return error
    assert n == int(n) and n >= 0, 'The number can be positive integer only!'
    
    if 0 <= n <= 1:
        return 1
    else:
        return n * factorial(n-1)
    
    
#----------------------------------------------------------------

# fibonaci numbers using recurion

# step 1: recursive case: (fn = f(n-1) + f(n-2))
# step 2. - base case - the stopping criterion 


def fibonaci(n):
    assert n == int(n) and n >= 0, 'the number con be positive integer only!'
    
    if 0 <= n <= 1:
        return n
    else:
        return fibonaci(n-1) + fibonaci(n-2) 

