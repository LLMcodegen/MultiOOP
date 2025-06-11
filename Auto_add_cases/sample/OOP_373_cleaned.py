
class LCL:
    def __init__(self, grid):
        self.grid = grid
class SN_LCL(LCL):
    def Land_Cell(self):
        if not self.grid:
            return 0
        m, n = len(self.grid), len(self.grid[0])
        visited = [[False] * n for _ in range(m)]
        def dfs(x, y):
            if x < 0 or x >= m or y < 0 or y >= n:
                return
            if self.grid[x][y] == 0 or visited[x][y]:
                return
            visited[x][y] = True
            dfs(x + 1, y)
            dfs(x - 1, y)
            dfs(x, y + 1)
            dfs(x, y - 1)
        for i in range(m):
            for j in range(n):
                if (i == 0 or i == m - 1 or j == 0 or j == n - 1) and self.grid[i][j] == 1:
                    dfs(i, j)
        count = 0
        for i in range(m):
            for j in range(n):
                if self.grid[i][j] == 1 and not visited[i][j]:
                    count += 1
        return count

#--------------:
print(SN_LCL([[2,1,1,1],[1,0,0,1],[1,0,0,1],[1,1,1,1]]).Land_Cell() == 0)
print(SN_LCL([[2,0,0,0],[0,1,1,0],[0,1,1,0],[0,0,0,0]]).Land_Cell() == 4)
print(SN_LCL([[2,0,1,0],[0,1,0,1],[1,0,1,0],[0,1,0,1]]).Land_Cell() == 2)
