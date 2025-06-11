
class IA:
    def __init__(self, grid):
        self.grid = grid
    def __private_Island_area(self):
        if not self.grid or not self.grid[0]:
            return 0
        m, n = len(self.grid), len(self.grid[0])
        max_area = 0
        def dfs(i, j):
            if i < 0 or i >= m or j < 0 or j >= n or self.grid[i][j] == 0:
                return 0
            self.grid[i][j] = 0
            area = 1
            area += dfs(i + 1, j)
            area += dfs(i - 1, j)
            area += dfs(i, j + 1)
            area += dfs(i, j - 1)
            return area
        for i in range(m):
            for j in range(n):
                if self.grid[i][j] == 1:
                    max_area = max(max_area, dfs(i, j))
        return max_area
    def public_Island_area(self):
        return self.__private_Island_area()

#--------------:
print(IA([[1, 0, 1, 0, 1], [0, 1, 0, 1, 0], [1, 0, 1, 0, 1], [0, 1, 0, 1, 0], [1, 0, 1, 0, 1]]).public_Island_area() == 1)
print(IA([[1, 1, 1, 0, 0], [0, 0, 1, 0, 0], [1, 1, 1, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]).public_Island_area() == 7)
print(IA([[1, 0, 0, 1, 0], [0, 1, 0, 1, 0], [0, 0, 1, 0, 0], [1, 1, 0, 1, 1], [0, 0, 0, 0, 0]]).public_Island_area() == 2)
