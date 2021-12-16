

'''
Bucket Sort
'''
# - Create buckets and distribute elements of array into buckets 
# - Sort buckets individually
# - Merge buckets after sorting

# Example:
# 5, 3, 4, 7
# Number of buckets = round(Sqrt(number of elements))
# round(Sqrt(4)) = 2
# [ ]  [ ]
# Appropriate bucket = ceil(Value * number of buckets / maxValue)
# For first element (5) => ceil(5*2/7) = ceil(10/7) = 2
# [ ] [5 ]
# For next element (3) => ceil(3*2/7) = ceil(6/7) = 1
# [3 ] [5 ]
# For next element (4) => ceil(4*2/7) = ceil(8/7) = 2
# [3 ] [5,4 ]
# For next element (7) => ceil(7*2/7) = ceil(14/7) = 2
# [3 ] [5,4,7] #Then use any algorithm to sort this buckets
# [3] [4,5,7]
# [3,4,5,7] # and merge them


import math

def bucketSort(unsortedList): #if we use quick sort with bucket sort time complexity => O(NlogN), space complexity => O(n)
    numberOfBuckets = round(math.sqrt(len(unsortedList)))
    maxValue = max(unsortedList)
    buckets = [[] for i in range(numberOfBuckets)]
    
    for element in unsortedList:
        bucketIndex = math.ceil(element*numberOfBuckets/maxValue)
        buckets[bucketIndex-1].append(element)
        
    # Then sort them with any sort function 
    buckets = [sorted(bucket) for bucket in buckets]
    buckets = [element for bucket in buckets for element in bucket]
    print(buckets)

sortList = [3,1,4,5,2]
bucketSort(sortList)



'''
When to use Insertion sort
'''
# - When input uniformly distributed over range (if differences between numbers are not too big)
# uniformly distributed => [1,2,4,5,3,7]
# not uniformly distributed => [1,2,4,46,83,12]
'''
When to avoid Insertion Sort
'''
# - When time is a concern



















