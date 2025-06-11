
class RDB:
    def __init__(self, grid):
        self.grid = grid
class SN_RDB(RDB):
    def __init__(self, grid):
        super().__init__(grid)
    def resource_distribution(self):
        def dfs(x, y):
            if x < 0 or x >= len(self.grid) or y < 0 or y >= len(self.grid[0]) or self.grid[x][y] == 0:
                return 0
            gold = self.grid[x][y]
            self.grid[x][y] = 0
            max_gold = gold + max(dfs(x + 1, y), dfs(x - 1, y), dfs(x, y + 1), dfs(x, y - 1))
            self.grid[x][y] = gold
            return max_gold
        max_gold_collected = 0
        for i in range(len(self.grid)):
            for j in range(len(self.grid[0])):
                if self.grid[i][j] != 0:
                    max_gold_collected = max(max_gold_collected, dfs(i, j))
        return max_gold_collected

#--------------:
print(SN_RDB([[1, 0, 1], [0, 1, 0], [1, 0, 1]]).resource_distribution() == 1)
print(SN_RDB([[1, 2, 3], [0, 0, 0], [7, 8, 9]]).resource_distribution() == 24)
print(SN_RDB([[1, 2, 3], [4, 0, 0], [7, 8, 9]]).resource_distribution() == 34)
