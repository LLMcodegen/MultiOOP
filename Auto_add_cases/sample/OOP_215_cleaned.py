
class KC:
    def __init__(self, n, k, row, column):
        self.n = n
        self.k = k
        self.row = row
        self.column = column
    def __private_Knight_Chessboard(self):
        moves = [(-2, -1), (-2, 1), (2, -1), (2, 1), (-1, -2), (-1, 2), (1, -2), (1, 2)]
        dp = [[[0] * self.n for _ in range(self.n)] for _ in range(self.k + 1)]
        dp[0][self.row][self.column] = 1
        for step in range(1, self.k + 1):
            for r in range(self.n):
                for c in range(self.n):
                    if dp[step - 1][r][c] > 0:
                        for dr, dc in moves:
                            new_r, new_c = r + dr, c + dc
                            if 0 <= new_r < self.n and 0 <= new_c < self.n:
                                dp[step][new_r][new_c] += dp[step - 1][r][c] / 8.0
        total_probability = sum(dp[self.k][r][c] for r in range(self.n) for c in range(self.n))
        return total_probability
    def public_Knight_Chessboard(self):
        return self.__private_Knight_Chessboard()

#--------------:
print(KC(4, 3, 0, 0).public_Knight_Chessboard() == 0.0390625)
print(KC(4, 4, 0, 0).public_Knight_Chessboard() == 0.017578125)
print(KC(5, 2, 0, 0).public_Knight_Chessboard() == 0.1875)
