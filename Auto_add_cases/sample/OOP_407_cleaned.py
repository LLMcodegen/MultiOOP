
class SSR:
    def __init__(self, grid):
        self.grid = grid
class SN_GGG(SSR):
    def Square_subgrid(self):
        grid = self.grid
        if not grid or not grid[0]:
            return 0
        n, m = len(grid), len(grid[0])
        max_size = 0
        right = [[0]*m for _ in range(n)]
        down = [[0]*m for _ in range(n)]
        for i in range(n-1, -1, -1):
            for j in range(m-1, -1, -1):
                if grid[i][j] == 1:
                    right[i][j] = 1 + (right[i][j+1] if j+1 < m else 0)
                    down[i][j] = 1 + (down[i+1][j] if i+1 < n else 0)
                else:
                    right[i][j] = 0
                    down[i][j] = 0
        for i in range(n):
            for j in range(m):
                small = min(right[i][j], down[i][j])
                for k in range(small, 0, -1):
                    if right[i+k-1][j] >= k and down[i][j+k-1] >= k:
                        max_size = max(max_size, k)
                        break
        return max_size * max_size

#--------------:
print(SN_GGG([[1,0,1,0],[0,1,0,1],[1,0,1,0]]).Square_subgrid() == 1)
print(SN_GGG([[1,1,1,1],[1,1,1,1],[1,1,1,1],[1,1,1,1]]).Square_subgrid() == 16)
print(SN_GGG([[1,0,1,0],[0,1,0,1],[1,0,1,0],[0,1,0,1]]).Square_subgrid() == 1)
