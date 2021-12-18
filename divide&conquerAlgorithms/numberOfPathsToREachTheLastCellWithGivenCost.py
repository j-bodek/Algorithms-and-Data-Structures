

# PROBLEM STATEMENT:
#   - 2D matrix is given 
#   - Each cell has a cost associated with it for accessing
#   - We need to start from (0,0) cel and go till (n-1,n-1) cell
#   - We can go only to right or down cell from current cell
#   - We are given total cost to reach the last cell
#   - Find the number of ways to reach end of matrix with given 'total cost'


matrix = [
    [4, 7, 1, 6],
    [5, 7, 3, 9],
    [3, 2, 1, 2],
    [7, 1, 6, 3],
]


def findWays(matrix, currentX, currentY):
    if currentX > len(matrix)-1 or currentY > len(matrix)-1:
        return []
    if currentY == len(matrix)-1 and currentX == len(matrix)-1:
        return [matrix[currentY][currentX]]
    else:
        moveRight = findWays(matrix,currentX+1,currentY)
        moveDown = findWays(matrix,currentX,currentY+1)
        
        return [*[matrix[currentY][currentX] + element for element in moveRight],*[matrix[currentY][currentX] + element for element in moveDown]]

print(findWays(matrix,0,0).count(25))



def numberOfPaths(matrix, row, column, cost):
    if cost < 0: return 0
    elif row == 0 and column == 0:
        if matrix[0][0] - cost == 0:
            return 1
        else:
            return 0
    elif row == 0:
        return numberOfPaths(matrix, 0, column-1, cost - matrix[row][column])
    elif column == 0:
        return numberOfPaths(matrix, row-1, 0, cost - matrix[row][column])
    else:
        option1 = numberOfPaths(matrix, row-1, column, cost - matrix[row][column])
        option2 = numberOfPaths(matrix, row, column-1, cost - matrix[row][column])
        return option1 + option2
    
print(numberOfPaths(matrix,3,3,25))












