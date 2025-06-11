
class HSE:
    def __init__(self, grid):
        self.grid = grid
class SN_HSE(HSE):
    def Highest_Score(self):
        m, n = len(self.grid), len(self.grid[0])
        max_score = 0
        for i in range(m):
            if self.grid[i][0] == 0:
                self.grid[i] = [1 - x for x in self.grid[i]]
        for j in range(n):
            count_ones = sum(self.grid[i][j] for i in range(m))
            if count_ones < m / 2:
                count_ones = m - count_ones
            max_score += count_ones * (1 << (n - j - 1))
        return max_score

#--------------:
print(SN_HSE([[0, 0], [0, 0]]).Highest_Score() == 6)
print(SN_HSE([[1, 0, 0], [0, 1, 0], [0, 0, 1]]).Highest_Score() == 18)
print(SN_HSE([[1, 1, 1], [1, 1, 1], [1, 1, 1]]).Highest_Score() == 21)
