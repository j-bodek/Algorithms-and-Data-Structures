


'''
Coin Change Problem
'''
# you are given coins of different denominations and total amount of money. Find the minimum number of coins
# that you need to make up the given amount 
# infinite supply of denominations:{1,2,5,10,20,50,100,1000}


# Example: 
# total amount: 70
# Answer 2 -> 50+20=70

'''
Coin Change Problem STEP BY STEP
'''
# total amount: 2035
# 2035 - 1000 = 1035    resultList = [1000]
# 1035 - 1000 = 35      resultList = [1000,1000]
# 35 - 20 = 15      resultList = [1000,1000,15]
# 15 - 10 = 5      resultList = [1000,1000,15,10]
# 5 - 5 = 0      resultList = [1000,1000,15,10,5]
# in each step take best local solution (biggest number that is less or equal then amount)

# 1. Find the biggest coin that is less or equal than given total number
# 2. Add coint to the result and subtract coin from total number
# 3. if amount will come to 0 print results

def coinChange(amount, coinsSet): # time complexity => O(N), space complexity => O(1)
    coinsSet.sort()
    lastIndex = len(coinsSet)-1
    while True:
        coinValue = coinsSet[lastIndex]
        if amount >= coinValue:
            print(coinValue)
            amount -= coinValue
        # we can be sure that index would not goes under 0 because amount is always greater or equal to 1 (min coin)
        if amount < coinValue:
            lastIndex -= 1
        if amount <= 0: 
            break

coins = [1,2,5,20,50,1000,10000]
coinChange(1929237, coins)
















