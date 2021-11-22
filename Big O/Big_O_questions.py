
# First question 
# Find runtime of the below code 

def foo(array):
    sum = 0  # constandt O(1)
    product = 1  # constandt O(1)
    for i in array:  # linear O(n)
        sum += i   # constandt O(1)
    for i in array:  # linear O(n)
        product *= i   # constandt O(1)
    print("Sum = "+str(sum)+", Product = "+str(product))   # constandt O(1)
    
# time complexity after removing constants is O(n)

#----------------------------------------------------------------

# Second question
# Find runtime of the below code 

def printPairs(array):
    for i in array: # linear O(n)
        for j in array: # linear O(n) but inside for loop 
            print(str(i)+","+str(j)) # constandt O(1)

# time complexity is O(n)*O(n) = O(n^2)

#----------------------------------------------------------------

# 3rd question
# What is runtime of the below code 

def printUnorderedPairs(array):
    for i in range(0,len(array)):  # linear O(n)
        for j in range(i+1,len(array)): # from O(n-1) to O(1)
            print(array[i] + "," + array[j])

#first iteration n-1
#second iteration n-2 
#...
# last iteration 1
#after sumation (n-1 + 1)*n/2 so runtime will be O(n^2)

#----------------------------------------------------------------

# 4th question
# What is the runtime of the below code?

def printUnorderedPairs(arrayA, arrayB):
    for i in range(len(arrayA)): # linear O(n)
        for j in range(len(arrayB)): # linear O(m)
            if arrayA[i] < arrayB[j]: # constant 
                print(str(arrayA[i]) + "," + str(arrayB[j])) # constant
                
# runtime will be O(n)*O(m) = O(n*m)

#----------------------------------------------------------------

# 5th question
# What is the runtime of the below code?

def printUnorderedPairs(arrayA, arrayB):
    for i in range(len(arrayA)): # linear O(n)
        for j in range(len(arrayB)): # linear O(n)
            for k in range(0,100000): # linear O(100000)
                print(str(arrayA[i]) + "," + str(arrayB[j]))

# runtime will be O(n)*O(m) = O(n*m) because we ignore constant O(100000)

#----------------------------------------------------------------

# 6th question
# What is the runtime of the below code?

def reverse(array):
    for i in range(0,int(len(array)/2)): # logaritmic O(n/2) 
        other = len(array)-i-1 # constant 
        temp = array[i] # constant 
        array[i] = array[other] # constant 
        array[other] = temp # constant 
    print(array) # constant 

# runtime will be O(n)

#----------------------------------------------------------------

# 7th question
# Which of the following are equivalent to O(n)

#we need to find which of function inside brackets are dominant

#1. O(n+p) where p<n/2   --   O(n) because n > p and is dominant
#2. O(2n)                --   O(n) because 2 is static
#3. O(n+log n)           --   O(n) because n > log n and n is dominant
#4. O(n + nlog n)        --   O(nlog n) because nlog n > n and is dominant
#5. O(n+m)               --   O(n+m) because be don't know which n or m is dominant


#----------------------------------------------------------------

# 8th question
# What is the runtime of the below code?
















