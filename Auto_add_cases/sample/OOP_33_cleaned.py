class STP:
    def shortest_path(self, grid):
        if not grid or not grid[0]:
            return 0
        m, n = len(grid), len(grid[0])
        dp = [[0] * n for _ in range(m)]
        dp[0][0] = grid[0][0]
        for j in range(1, n):
            dp[0][j] = dp[0][j - 1] + grid[0][j]
        for i in range(1, m):
            dp[i][0] = dp[i - 1][0] + grid[i][0]
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = min(dp[i - 1][j], dp[i][j - 1]) + grid[i][j]
        return dp[-1][-1]
#--------------:
print(STP().shortest_path([[5]]) == 5)
print(STP().shortest_path([[2, 3], [4, 1]]) == 6)
print(STP().shortest_path([[1, 2, 3, 4], [4, 3, 2, 1]]) == 9)
