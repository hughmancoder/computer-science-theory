class EightQueens:
    def __init__(self, size=8):
        self.size = size
        self.board = [[''] * size for _ in range(size)]
        self.res = []

    def is_safe(self, row, col):
        for i in range(col):
            if self.board[row][i] == 'Q':
                return False
            for i, j in zip(range(row, -1, -1), range(col, -1, -1)):  # check upper diagonal
                if self.board[i][j] == 'Q':
                    return False
            for i, j in zip(range(row, self.size, 1), range(col, -1, -1)):  # check lower diagonal
                if self.board[i][j] == 'Q':
                    return False
        return True

    def solve_queens(self, col=0):
        if col == self.size:
            self.res.append([row[:] for row in self.board])
            return
        for i in range(self.size):
            if self.is_safe(i, col):
                self.board[i][col] = 'Q'
                self.solve_queens(col + 1)
                self.board[i][col] = ''

    def print_solution(self):
        for i, board in enumerate(self.res):
            print(f"\n\nSolution {i + 1}:")
            for row in board:
                print('.'.join(row))

def test_eight_queens():
    queens = EightQueens()
    queens.solve_queens()
    queens.print_solution()

if __name__ == "__main__":
    test_eight_queens()