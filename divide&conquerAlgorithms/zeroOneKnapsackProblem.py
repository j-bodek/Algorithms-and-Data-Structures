

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

class Item:
    def __init__(self,profit, weight):
        self.profit = profit
        self.weight = weight

def zeroOneKnapsack(items,capacity, currentIndex):
    if capacity <= 0 or currentIndex < 0 or len(items) <= currentIndex:
        return 0
    elif items[currentIndex].weight <= capacity:
        # take first element
        profitOne = items[currentIndex].profit + zeroOneKnapsack(items, capacity-items[currentIndex].weight, currentIndex+1)
        # skip first element and countinue to next one
        profitSecond = zeroOneKnapsack(items, capacity, currentIndex+1)
        return max(profitOne, profitSecond)
    else:
        return 0
    
mango = Item(31,3)
apple = Item(26,1)
orange = Item(17,2)
banana = Item(72,5)
items = [mango,apple,orange,banana]
print(zeroOneKnapsack(items, 7, 0))














