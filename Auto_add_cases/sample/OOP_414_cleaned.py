
from collections import deque

class OCL:
    def __init__(self, grid):
        self.grid = grid
        self.n = len(grid)
class SN_OCL(OCL):
    def Ocean_Cell(self):
        if not self.grid or not any(1 in row for row in self.grid):
            return -1
        queue = deque()
        for i in range(self.n):
            for j in range(self.n):
                if self.grid[i][j] == 1:
                    queue.append((i, j))
        if len(queue) == self.n * self.n:
            return -1
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        distance = -1
        while queue:
            distance += 1
            for _ in range(len(queue)):
                x, y = queue.popleft()
                for dx, dy in directions:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < self.n and 0 <= ny < self.n and self.grid[nx][ny] == 0:
                        self.grid[nx][ny] = distance + 1
                        queue.append((nx, ny))
        max_distance = distance
        return max_distance
#--------------:
print(SN_OCL([[1, 0, 1],[0, 0, 0],[1, 0, 1]]).Ocean_Cell() == 2)
print(SN_OCL([[1, 1],[1, 1]]).Ocean_Cell() == -1)
print(SN_OCL([[0, 0],[0, 0]]).Ocean_Cell() == -1)
