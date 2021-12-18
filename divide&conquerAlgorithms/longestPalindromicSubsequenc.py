


# PROBLEM STATEMENT:
#   - S is a given string
#   - Find the longest palindromic subsequence 
#   - Subsequence: a sequence that can be driven from another sequence by deleting some elements without changeing the order of them
#   - Palindrome is a string that reads the same backward as well as forward

# Example:
# ELRMENMET => output = 5 because longest polindrome subseqence is 'EMEME'

# SUBPROBLEMS:
#   - both elements are same (first and last)
#   - elements not matching (move one to left from last element)
#   - elements not matching (move one to right from first element)

def findLongestPalindromeSequence(string, startIndex, endIndex):
    if startIndex > endIndex:
        return 0
    elif startIndex == endIndex: #if both indexes reach to middle of string
        return 1
    if string[startIndex] == string[endIndex]: #both characters same
        return 2 + findLongestPalindromeSequence(string, startIndex+1, endIndex-1)
    else:
        #move endIndex
        option1 = findLongestPalindromeSequence(string, startIndex, endIndex-1)
        # move startIndex
        option2 = findLongestPalindromeSequence(string, startIndex+1, endIndex)
        
        return max(option1, option2)


print(findLongestPalindromeSequence('ELRMENMET',0,8))










