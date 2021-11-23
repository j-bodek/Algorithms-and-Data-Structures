
mylist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100]

# Question 1 - missing number in iteger of 1 to 100

def find_missing(ls):
    return [x for x in list(range(1,101)) if x not in mylist]

# Question 2 - write a program to find all pairs of integers whose sum is equal to a given number
find_pairs = lambda ls,items_sum: [output[0] for output in [[(x,y) for y in ls if y != x and x+y == items_sum] for x in ls] if output != []]

# Question 3 = How to check if an array contains a number in Python 
# linear search
findNumber = lambda array,number: True if [x for x in array if x == number] else False

# Question 4 = find maximum product of two int in list
biggestProduct = lambda ls: sorted(ls,reverse=True)[0] * sorted(ls,reverse=True)[1]

# Question 5 - Check if all elements in list are isUnique
checkUnique = lambda ls: True if len(set(ls)) == len(ls) else False

# Question 6 - check if two lists are permutation
checkPermutation = lambda ls1,ls2: True if sorted(ls1) == sorted(ls2) else False

# Question 7 - rotate matrix by 90 degrees
reverseMatrix = lambda matrix: [[matrix[x][col] for x in range(len(matrix)-1,-1,-1)] for col in range(len(matrix[0]))]

