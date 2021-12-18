


# PROBLEM STATEMENT:
#   - 2D matrix is given
#   - Each cell has a cost associated with it for accessing
#   - We need to start from (0,0) cel and go till (n-1,n-1) cell
#   - We can go only to right or down cell from current cell
#   - Find the way in which the cost is minimum


# Example:

matrix = [
    [4, 7, 8, 6, 4],
    [6, 7, 3, 9, 2],
    [3, 8, 1, 2, 4],
    [7, 1, 7, 3, 7],
    [2, 9, 8, 9, 3],
]

# We want to go from cell (0,0) to (n-1,n-1)
# min cost is 36

# to solve it you have to take to options into account:
#   - option1 go right
#   - option2 go down

def findMinCost(matrix,currentX, currentY):
    if currentX > len(matrix)-1 or currentY > len(matrix)-1:
        return float('inf')
    if currentY == len(matrix)-1 and currentX == len(matrix)-1:
        return matrix[currentY][currentX]
    else:
        moveRight = findMinCost(matrix,currentX+1,currentY)
        moveDown = findMinCost(matrix,currentX,currentY+1)
        return matrix[currentY][currentX] + min(moveRight,moveDown)
    
print(findMinCost(matrix,0,0))




















