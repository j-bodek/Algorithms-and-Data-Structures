

'''
A Recipe for Problem Solving
'''
# Algorithm: is a set of steps for accomplish a certain task


'''
5 STEPS FOR PROBLEM SOLVING
'''
#   - UNSERSTAND THE PROBLEMS
# 1. Can we restate the problem in our own words?
# 2. What are the inputs that go into the problem?
# 3. What are the outputs that come from the problem?
# 4. Can the outputs be determined from the inputs? In other words do we have enough information to solve this problem?
# 5. What should I label that important piece of data that are the part of a problem?


#   - EXPLORE EXAMPLES
# 1. Start with simple examples
# 2. Progress to more complex examples
# 3. Explore examples with empty 
# 4. Explore examples with invalid examples


#   - BREAK IT DOWN
# Write out the steps that you need to take 
# Example: write function that takes string and return counts of every character
# step.1   Declare an object to return at the end
# step.2   loop over the string
#   - if character is not in our object add that character to our object with the value of one
#   - if character is in our object add one to the value
# step.3   return an object


#   - SOLVE / SIMPLIFY
# if you can't solve entire problem simplify it 
# * Find the core difficulty
# * Temporarily ignore that difficulty 
# *  Write a simplified solution
# *  Then incorporate that difficulty




def charCount(string):
    # lowercase character and eliminate spaces
    string = string.lower().replace(' ', '')
    # Create list of characters
    characters = list(set([character for character in string]))
    # create dictionary 
    return dict(zip(characters, [string.count(character) for character in characters]))

print(charCount('Hello World'))


def orderedCharCount(string):
    # lowercase character and eliminate spaces
    string = string.lower().replace(' ', '')
    # Create list of characters and check if they are letters
    characters = list(set([character for character in string if isinstance(character, str)]))
    # sort characters
    characters.sort(key=lambda character: string.index(character))
    # create dictionary 
    return dict(zip(characters, [string.count(character) for character in characters]))

print(orderedCharCount('Hello World'))



#   - LOOK BACK REFACTOR
# Can we check the result?
# Can we drive the result differently?
# Can we understand it at a glance?
# Can we use the result or method for some other problem?
# Can you improve the performance of your solution? (time and space complexity)
# How other people solve this problem?
























