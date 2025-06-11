
class IAA:
    def __init__(self, grid):
        self.grid = grid
        self.n = len(grid)
class SN_IAA(IAA):
    def __init__(self, grid):
        super().__init__(grid)
    def dfs(self, i, j, visited):
        if i < 0 or i >= self.n or j < 0 or j >= self.n or visited[i][j] or self.grid[i][j] == 0:
            return 0
        visited[i][j] = True
        area = 1
        area += self.dfs(i + 1, j, visited)
        area += self.dfs(i - 1, j, visited)
        area += self.dfs(i, j + 1, visited)
        area += self.dfs(i, j - 1, visited)
        return area
    def Island_area(self):
        visited = [[False for _ in range(self.n)] for _ in range(self.n)]
        max_area = 0
        for i in range(self.n):
            for j in range(self.n):
                if self.grid[i][j] == 1 and not visited[i][j]:
                    max_area = max(max_area, self.dfs(i, j, visited))
        for i in range(self.n):
            for j in range(self.n):
                if self.grid[i][j] == 0:
                    seen_islands = set()
                    new_area = 1
                    for x, y in [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]:
                        if 0 <= x < self.n and 0 <= y < self.n and self.grid[x][y] == 1:
                            seen_islands.add((x, y))
                    visited = [[False for _ in range(self.n)] for _ in range(self.n)]
                    for island in seen_islands:
                        new_area += self.dfs(island[0], island[1], visited)
                    max_area = max(max_area, new_area)
        return max_area

#--------------:
print(SN_IAA([[0, 0, 0, 0], [0, 1, 1, 0], [0, 1, 1, 0], [0, 0, 0, 1]]).Island_area() == 6)
print(SN_IAA([[0, 0, 0, 0], [0, 1, 1, 0], [0, 1, 1, 0], [0, 0, 1, 1]]).Island_area() == 7)
print(SN_IAA([[0, 0, 0, 0], [0, 1, 1, 0], [0, 1, 1, 0], [0, 1, 1, 1]]).Island_area() == 8)