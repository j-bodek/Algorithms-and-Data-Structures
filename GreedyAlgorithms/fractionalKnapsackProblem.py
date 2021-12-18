

'''
Fractional Knapsack Problem
'''
# Given a set of items, each with a weight and a value, determine the number of each item to 
# include in a collection so that the total weight is less than or equal to a given limit and the
# total value is as large as possible.

# This problem often araises in resource allocation 

'''
Example 
Fill box that can weight max 50kg with items to get max value and don't cross weight limit
- item 1 [20kg, 100]
- item 2 [30kg, 120]
- item 3 [10kg, 60]

# 1. find which item has max density 
# - item 1 100/20 = 5
# - item 1 120/30 = 4
# - item 1 60/10 = 6

# 2. sort items by highest density

# 3. then take first items with max density

# 4. add the next item as much as we can
'''

class Item:
    def __init__(self, weight, value):
        self.weight = weight
        self.value = value
        self.ratio = value/weight
        
def knapsackMethod(items, capacity): # time complexity => O(NlogN), space complexity => O(1)
    # sort items based on highest density
    items.sort(key = lambda i: i.ratio, reverse=True)
    usedCapacity = 0
    totalValue = 0
    for item in items:
        if item.weight + usedCapacity <= capacity:
            usedCapacity += item.weight
            totalValue += item.value
        else:
            unusedWeight = capacity - usedCapacity
            value = item.ratio * unusedWeight
            usedCapacity += unusedWeight
            totalValue += value

        if usedCapacity == capacity:
            break
    print(f'Total value: {totalValue}')

item1 = Item(20,100)
item2 = Item(30,120)
item3 = Item(10,60)
cList = [item1, item2, item3]

knapsackMethod(cList, 50)





















