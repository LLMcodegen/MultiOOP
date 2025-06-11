
class PBI:
    def __init__(self, board):
        self.board = board
    def __private_Placed_battleships(self):
        if not self.board:
            return 0
        m, n = len(self.board), len(self.board[0])
        count = 0
        for i in range(m):
            for j in range(n):
                if self.board[i][j] == 'X':
                    if (i == 0 or self.board[i-1][j] != 'X') and (j == 0 or self.board[i][j-1] != 'X'):
                        count += 1
        return count
    def public_Placed_battleships(self):
        return self.__private_Placed_battleships()

#--------------:
print(PBI([['X', '.', 'X'], ['.', 'X', '.'], ['X', '.', 'X']]).public_Placed_battleships() == 5)
print(PBI([['X', '.', '.'], ['.', 'X', '.'], ['.', '.', 'X']]).public_Placed_battleships() == 3)