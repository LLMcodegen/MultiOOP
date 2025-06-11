
from collections import deque

class MME:
    def __init__(self, grid):
        self.grid = grid
class SN_MME(MME):
    def Min_Minutes(self):
        if not self.grid:
            return -1
        rows, cols = len(self.grid), len(self.grid[0])
        queue = deque()
        fresh_count = 0
        for r in range(rows):
            for c in range(cols):
                if self.grid[r][c] == 1:
                    fresh_count += 1
                elif self.grid[r][c] == 2:
                    queue.append((r, c))
        if fresh_count == 0:
            return 0
        minutes = 0
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        while queue:
            for _ in range(len(queue)):
                r, c = queue.popleft()
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < rows and 0 <= nc < cols and self.grid[nr][nc] == 1:
                        self.grid[nr][nc] = 2
                        fresh_count -= 1
                        queue.append((nr, nc))
            minutes += 1
        return minutes - 1 if fresh_count == 0 else -1

#--------------:
print(SN_MME([[2, 2],[2, 2]]).Min_Minutes() == 0)
print(SN_MME([[2, 1, 1],[1, 1, 0],[0, 1, 1]]).Min_Minutes() == 4)
print(SN_MME([[2, 1, 1],[0, 1, 1],[1, 0, 1]]).Min_Minutes() ==-1)
