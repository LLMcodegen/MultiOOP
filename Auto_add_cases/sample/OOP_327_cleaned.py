
class FNE:
    def __init__(self, grid):
        self.grid = grid
class SN_FNE(FNE):
    def __init__(self, grid):
        super().__init__(grid)
    def Flip_Number(self):
        from collections import deque
        n = len(self.grid)
        visited = [[False] * n for _ in range(n)]
        islands = []
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        def bfs(start):
            queue = deque([start])
            island_cells = []
            visited[start[0]][start[1]] = True
            while queue:
                x, y = queue.popleft()
                island_cells.append((x, y))
                for dx, dy in directions:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny] and self.grid[nx][ny] == 1:
                        visited[nx][ny] = True
                        queue.append((nx, ny))
            return island_cells
        for i in range(n):
            for j in range(n):
                if self.grid[i][j] == 1 and not visited[i][j]:
                    islands.append(bfs((i, j)))
        def min_distance(island1, island2):
            min_dist = float('inf')
            for x1, y1 in island1:
                for x2, y2 in island2:
                    dist = abs(x1 - x2) + abs(y1 - y2) - 1
                    min_dist = min(min_dist, dist)
            return min_dist
        return min_distance(islands[0], islands[1]) if len(islands) == 2 else 0

#--------------:
print(SN_FNE([[0,1,0],[0,0,0],[0,0,1]]).Flip_Number() == 2)
print(SN_FNE([[1,1],[1,1]]).Flip_Number() == 0)
