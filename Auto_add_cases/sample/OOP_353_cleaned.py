
class DPS:
    def __init__(self, grid):
        self.grid = grid
class SN_DPS(DPS):
    def Different_paths(self):
        def backtrack(x, y, remain):
            if x < 0 or x >= rows or y < 0 or y >= cols or self.grid[x][y] == -1:
                return 0
            if self.grid[x][y] == 2:
                return 1 if remain == 1 else 0
            temp = self.grid[x][y]
            self.grid[x][y] = -1
            remain -= 1
            paths = (backtrack(x + 1, y, remain) +
                     backtrack(x - 1, y, remain) +
                     backtrack(x, y + 1, remain) +
                     backtrack(x, y - 1, remain))
            self.grid[x][y] = temp
            remain += 1
            return paths
        rows, cols = len(self.grid), len(self.grid[0])
        start_x = start_y = 0
        empty_count = 0
        for i in range(rows):
            for j in range(cols):
                if self.grid[i][j] == 1:
                    start_x, start_y = i, j
                if self.grid[i][j] != -1:
                    empty_count += 1
        return backtrack(start_x, start_y, empty_count)

#--------------:
print(SN_DPS([[1,0,0,-1],[0,-1,0,2],[0,0,0,0]]).Different_paths() == 0)
print(SN_DPS([[1,0,0,0],[0,-1,-1,0],[0,0,0,2]]).Different_paths() == 0)
print(SN_DPS([[1,0,-1,0],[0,0,-1,0],[0,0,2,0]]).Different_paths() == 0)
