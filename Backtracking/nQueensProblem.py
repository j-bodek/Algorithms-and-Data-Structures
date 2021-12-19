

'''
N Queens Problem
'''
# Place N queens on an NxN chess board, in such a manner that no two queens can attack each other

# simplified problem - Place 4 queens on an 4x4 chess board, in such a manner that no two queens can attack each other
# cannot place same queen on the same column
# cannot place same queen on the same row
# cannot place same queen on diagonal

# 1. start in the leftmost column
# 2. if all queens are placed return True
# 3. try all rows in the current column
#   - a) if the queen can be placed safely in this row then mark this [row, column] as part of the solution and recursively chack if placing queen here leads to a solution
#   - b) If placing the queen in [row,column] leads to a solution then return true
#   - c) If placing queen does't lead to a solution then unmark this [row, column] and go to step (a) to try other rows
# 4. If all rows have been tried and nothing worked, return false to trigger backtracking.


class NQueens:
    def __init__(self, N):
        self.n = N
        self.board = [[0 for i in range(N)] for j in range(N)]
        
    def __str__(self):
        return '\n'.join([str(row) for row in self.board])
    
    def printQueens(self):
        return '\n'.join(' '.join(['👑' if el == 1 else '⬛' if (indexCol+indexRow)%2!=0 else '⬜'  for indexCol,el in enumerate(row)]) for indexRow,row in enumerate(self.board))

    def checkSafePlace(self, rowIndex, colIndex):
        for index, row in enumerate(self.board):
            if row[colIndex] == 1 or (index == rowIndex and sum(row) > 0):
                return False
        
        # check diagonals
        # check only for queens that are upper
        # right diagonal
        col = colIndex
        for row in range(rowIndex,-1,-1):
            if row < 0: break
            if self.board[row][col] == 1:
                return False
            col -= 1
        # left diagonal
        col = colIndex
        for row in range(rowIndex,self.n):
            if row < 0: break
            if self.board[row][col] == 1:
                return False
            col -= 1
        
        return True
    
    def solve(self, colIndex):
        print(colIndex)
        if colIndex == self.n:
            return True
        # print(self.printQueens())
        # print(self.checkSafePlace(0,1))
        
        for rowIndex in range(self.n):
            if self.checkSafePlace(rowIndex, colIndex):
                print('safe')
                self.board[rowIndex][colIndex] = 1
                
                if self.solve(colIndex+1):
                    return True
                self.board[rowIndex][colIndex] = 0
        return False
    
    def solveNQueens(self):
        if self.solve(0):
            print(self.printQueens())
            # pass
        else:
            print('There is no solution')


nQueens = NQueens(4)
nQueens.solveNQueens()







