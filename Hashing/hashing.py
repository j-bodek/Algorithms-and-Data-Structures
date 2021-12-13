
# WHAT IS HASHING?
# Hashiing is a method of sorting and indexing data. The idea behind hashing is to allow large
# amounts of data to be indexed using keys commonly created by formulas

# WHY HASHING?
# It is time efficient in case of SEARCH Operations

# Data Structure      |  Time complexity for SEARCH
#--------------------------------------------------
# Array/Python List   |  O(LogN)
# Linked List         |  O(N)
# Tree                |  O(logN)
# Hashing             |  O(1) / O(N)



# HASHING TERMINOLOGY
# - Hash Function: it is a function that can be used to map of arbitrary size to data of fixed size
# - Key: Input data given by a user
# - Hash value: A value that is returned by Hash Function
# - Hash Table: data structure which implements n associative array abstarct data type, a structure that can map keys to values
# - Collision: A collision occures when two different keys to a hash function produce the same output


# HASH FUNCTIONS
# - Mod function
def mod(number, cellNumber):
    return number % cellNumber
# mod(400, 24) => insert 400 to index of 16 (400%24=16)
# mod(700, 24) => insert 700 to index of 4 (700%24=4)
 
# - ASCII function (we use ascii values to convert it to number)
def modASCII(string, cellNumber):
    # ord -> Return the Unicode code point for a one-character string
    return sum([ord(i) for i in string]) % cellNumber
# modASCII("ABC", 24) => insert 'ABC' to index of 6
print(modASCII("ABC", 24))


# PROPERTIES OF GOOD HASH FUNCTIONS
# - It distributes hash values uniformly across hash tables
# - It has to use all the input data



# What is collision in hash function?
# collision - situation where hash function assing same index to different inputs

# COLLISTION RESOLUTION TECHNIQUES
# - Direct Chainign: Implements the buckets as linked list. Colliding elements are stored in this lists
# - Open Addressing: Colliding elements are stored in other vacent buckets. During storage and lookup these are found through so called probing.
#   - Linear probing: It places new key into closest following empty cell
#   - Quadratic probing: Adding arbitrary quadratic polynomial to the index until an empty cell is found
#   - Double hashing: Intervl between probs is computed by another hash function



# PROS AND CONS OF COLLISION RESOLUTION TECHNIQUES
# - Direct chaining: 
#   PROS:
#   - Hash table never gets full
#   CONS:
#   - Hge linked list causes performance leaks (time complexit for search operation becomes O(n))
#-------------------------------------------------------------------------------------------------
# - Open addressing:
#   PROS:
#   - Easy Implementation
#   CONS:
#   - When Hash Talbe is full ,creation of new Hash table affects performance (time complexity for search operation becones O(n))

# If the input size is known we always use 'Open Addressing"
# If we perform deletion operation frequently we use 'Direct chaining'


# PRACTICAL USE OF HASHING
# - password verification (password gets converted to hash value)
# - file systems (file path is mepped to physical location on disk)


# PROS AND CONS OF HASHING
# PROS:
#     - On an average insertion / deletion / search operations take O(1) time
# CONS:
#     - When Hash function is not good enough insertion / deletion / search operations take O(n) time complexity







































