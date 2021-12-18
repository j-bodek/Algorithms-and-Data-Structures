

# PROBLEM STATEMENT: 
#   - S1 and S@ are given strings
#   - Find the length of the longest subsequence which is common to both strings
#   - Subsequese: a sequence that can be driven from another sequence by deleting some elements without changeing the order of them

# example:
# ABCDE => subsequece of length 3 is for example ACD

# subproblems:
#   - Option1 1+f(2,8 : 2,7) - characters are matching
#   - Option2 0 + f(3,8:2,7) - characters not matching move to next one
#   - Option3 0 + f(2,8:3,7) - characters not matching delete this character


def findLongestCommonSubsequence(string1, string2, indexFirstString, indexSecondString):
    if indexFirstString == len(string1) or indexSecondString == len(string2):
        return 0
    if string1[indexFirstString] == string2[indexSecondString]:
        return 1 + findLongestCommonSubsequence(string1, string2, indexFirstString+1, indexSecondString+1)
    else:
        option2 = findLongestCommonSubsequence(string1, string2, indexFirstString+1, indexSecondString)
        option3 = findLongestCommonSubsequence(string2, string1, indexFirstString, indexSecondString+1)
        return max(option2, option3)
    
    
print(findLongestCommonSubsequence('elephant','eretpat',0,0))