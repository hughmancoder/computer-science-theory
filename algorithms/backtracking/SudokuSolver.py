class Solution:
    def solveSudoku(self, board):
        return self.backtrack(board)
        
    def backtrack(self, board):
        for r in range(len(board)):
            for c in range(len(board[0])):
                if board[r][c] == ".":
                    # try numbers from 1 to 10
                    for num in range(1,10):
                        if self.isValidMove(board, r, c, str(num)):
                            board[r][c] = str(num)
                            if self.backtrack(board):
                                return board
                            # otherwise backtrack
                            else:
                                board[r][c] = "."
                    return False
        return True
                                
    def isValidMove(self, board, row, col, cand):
        for i in range(9):
            if board[i][col] != "." and board[i][col] == cand: 
                return False
            if board[row][i] != "." and board[row][i] == cand: 
                return False
            # square row and col positions
            srp = 3 * (row // 3)  + i // 3 
            scp = 3 * (col // 3) + i % 3

            if board[srp][scp] != "." and board[srp][scp] == cand: 
                return False
            
        return True