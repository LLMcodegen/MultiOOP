
class NBS:
    def __init__(self, grid):
        self.grid = grid
        self.m = len(grid)
        self.n = len(grid[0])
class SN_NBS(NBS):
    def __init__(self, grid, hits):
        super().__init__(grid)
        self.hits = hits
    def find(self, parent, x):
        if parent[x] != x:
            parent[x] = self.find(parent, parent[x])
        return parent[x]
    def union(self, parent, size, x, y):
        rootX = self.find(parent, x)
        rootY = self.find(parent, y)
        if rootX != rootY:
            if size[rootX] >= size[rootY]:
                parent[rootY] = rootX
                size[rootX] += size[rootY]
            else:
                parent[rootX] = rootY
                size[rootY] += size[rootX]
    def is_connected_to_top(self, row, col):
        return row == 0
    def index(self, row, col):
        return row * self.n + col
    def Number_bricks(self):
        for r, c in self.hits:
            if self.grid[r][c] == 1:
                self.grid[r][c] = 2
        parent = [i for i in range(self.m * self.n + 1)]
        size = [1] * (self.m * self.n + 1)
        top = self.m * self.n
        for r in range(self.m):
            for c in range(self.n):
                if self.grid[r][c] == 1:
                    if self.is_connected_to_top(r, c):
                        self.union(parent, size, self.index(r, c), top)
                    for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                        nr, nc = r + dr, c + dc
                        if 0 <= nr < self.m and 0 <= nc < self.n and self.grid[nr][nc] == 1:
                            self.union(parent, size, self.index(r, c), self.index(nr, nc))
        result = []
        for r, c in reversed(self.hits):
            before_hit_stable_count = size[self.find(parent, top)]
            if self.grid[r][c] == 2:
                self.grid[r][c] = 1
                if self.is_connected_to_top(r, c):
                    self.union(parent, size, self.index(r, c), top)
                for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < self.m and 0 <= nc < self.n and self.grid[nr][nc] == 1:
                        self.union(parent, size, self.index(r, c), self.index(nr, nc))
                after_hit_stable_count = size[self.find(parent, top)]
                result.append(max(0, after_hit_stable_count - before_hit_stable_count - 1))
            else:
                result.append(0)
        return result[::-1]

#--------------:
print(SN_NBS([[1, 0, 0, 0], [1, 1, 1, 0]], [[0, 0], [1, 0]]).Number_bricks() == [3, 0])
print(SN_NBS([[1, 0, 0, 0], [1, 1, 1, 0]], [[0, 0], [1, 1]]).Number_bricks() == [3, 0])
print(SN_NBS([[1, 0, 0, 0], [1, 1, 1, 0]], [[0, 0], [1, 2]]).Number_bricks() == [3, 0])
