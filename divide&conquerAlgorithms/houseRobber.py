

'''
House Robber
'''

# Problem Statement:
#   - Given N number of houses along the street with some amount of money
#   - Adjacent houses cannot be stolen
#   - Find the maximum amount that can be stolen

# Example 
# [6]  [7]  [1]  [30]  [8]  [2]  [4]  
# Answer amount = 41
# Houses that are stolen: 7+41+4 = 41

'''
                         _______________________maxValueHouse(0)________________________
                        /                                                               \
         _______maxValueHouse(2)________                                 _______maxValueHouse(1)________
        /                               \                               /                               \
maxValueHouse(4)                maxValueHouse(3)                maxValueHouse(3)                maxValueHouse(2)
'''


def houseRobber(houses, currentIndex):
    if currentIndex >= len(houses): return 0
    stealFirstHouse = houses[currentIndex] + houseRobber(houses, currentIndex+2) #skipping neighbour house
    skipFirstHouse = houseRobber(houses, currentIndex+1) #skip current house and steal from next one
    return max(stealFirstHouse, skipFirstHouse)

houses = [6,7,1,30,8,2,4]
print(houseRobber(houses, 0))

















