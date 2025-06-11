
class LIM:
    def __init__(self, matrix):
        self.matrix = matrix
    def _private_Longest_Incremental(self):
        if not self.matrix or not self.matrix[0]:
            return 0
        m, n = len(self.matrix), len(self.matrix[0])
        memo = [[0] * n for _ in range(m)]
        def dfs(i, j):
            if memo[i][j] != 0:
                return memo[i][j]
            longest_path = 1
            for x, y in [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]:
                if 0 <= x < m and 0 <= y < n and self.matrix[x][y] > self.matrix[i][j]:
                    longest_path = max(longest_path, 1 + dfs(x, y))
            memo[i][j] = longest_path
            return longest_path
        max_length = 0
        for i in range(m):
            for j in range(n):
                max_length = max(max_length, dfs(i, j))
        return max_length
    def public_Longest_Incremental(self):
        return self._private_Longest_Incremental()

#--------------:
print(LIM([[9, 8, 7], [6, 5, 4], [3, 2, 1]]).public_Longest_Incremental() == 5)
print(LIM([[3, 2, 1], [6, 5, 4], [7, 8, 9]]).public_Longest_Incremental() == 7)
print(LIM([[10, 9, 8], [7, 6, 5], [4, 3, 2]]).public_Longest_Incremental() == 5)
