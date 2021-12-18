

'''
Activity selection problem
'''
# Given N number of activities with their start and end times. We need to select the maximum
# number of activities that can be performed by a single person, assuming that a person can
# only work on a single activity at a time.

'''
Activity A1  A2  A3  A4  A5  A6
START    0   3   1   5   5   8
END      6   4   2   8   7   9

To find order of activities we will sort them based on finish time

Activity A3  A2  A1  A5  A4  A6
START    1   3   0   5   5   8
END      2   4   6   7   8   9
'''

# ACTIVITY SELECTION PROBLEM:
#   - Sort activities based on finished time
#   - Select first activity from sorted array and print it
#   - For all remaining activities:
#       -If the start time of this activity is greater or equal to the finish time of previously selected
#        activity then select this activity and print it

activities = [["A1", 0, 6],
              ["A2", 3, 4],
              ["A3", 1, 2],
              ["A4", 5, 8],
              ["A5", 5, 7],
              ["A6", 8, 9]
                ]

def printMaxActivities(activities): # time complexity => O(NlogN), space complexity => O(1)
    # sort activities based on finish time
    activities.sort(key=lambda i: i[2]) # time complexity => O(NlogN)

    i = 0
    # select activities
    firstActivity = activities[i][0]
    print(firstActivity)
    for activity in range(len(activities)): # time complexity => O(N)
        if activities[activity][1] > activities[i][2]:
            print(activities[activity][0])
            i = activity
            
printMaxActivities(activities)
















