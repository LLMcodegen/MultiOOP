
from collections import deque

class UPT:
    def __init__(self, grid):
        self.grid = grid
class SN_UPT(UPT):
    def Unobstructed_path(self):
        grid = self.grid
        n = len(grid)
        if n == 0 or grid[0][0] != 0 or grid[n - 1][n - 1] != 0:
            return -1
        directions = [(-1, -1), (-1, 0), (-1, 1), ( 0, -1), ( 0, 1), ( 1, -1), ( 1, 0), ( 1, 1)]
        visited = [[False] * n for _ in range(n)]
        queue = deque([(0, 0, 1)])
        visited[0][0] = True
        while queue:
            row, col, length = queue.popleft()
            if row == n - 1 and col == n - 1:
                return length
            for dr, dc in directions:
                r, c = row + dr, col + dc
                if (0 <= r < n) and (0 <= c < n) and not visited[r][c] and grid[r][c] == 0:
                    visited[r][c] = True
                    queue.append((r, c, length + 1))
        return -1

#--------------:
print(SN_UPT([[0,1,0],[0,1,0],[0,1,0]]).Unobstructed_path() == -1)
print(SN_UPT([[0,0,0],[0,1,0],[0,0,2]]).Unobstructed_path() == -1)
print(SN_UPT([[0,1,0],[0,0,0],[0,1,2]]).Unobstructed_path() == -1)
