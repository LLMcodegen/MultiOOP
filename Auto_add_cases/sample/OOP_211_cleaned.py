
from collections import deque

class CDT:
    def __init__(self, forest):
        self.forest = forest
    def __private_Chop_down_trees(self):
        m, n = len(self.forest), len(self.forest[0])
        trees = []
        for i in range(m):
            for j in range(n):
                if self.forest[i][j] > 1:
                    trees.append((self.forest[i][j], i, j))
        trees.sort()
        def bfs(start_row, start_col, target_row, target_col):
            if start_row == target_row and start_col == target_col:
                return 0
            directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
            visited = [[False] * n for _ in range(m)]
            queue = deque([(start_row, start_col, 0)])
            visited[start_row][start_col] = True
            while queue:
                row, col, steps = queue.popleft()
                for dr, dc in directions:
                    new_row, new_col = row + dr, col + dc
                    if 0 <= new_row < m and 0 <= new_col < n and not visited[new_row][new_col]:
                        if self.forest[new_row][new_col] != 0:
                            if new_row == target_row and new_col == target_col:
                                return steps + 1
                            visited[new_row][new_col] = True
                            queue.append((new_row, new_col, steps + 1))
            return -1
        total_steps = 0
        start_row, start_col = 0, 0
        for height, target_row, target_col in trees:
            steps = bfs(start_row, start_col, target_row, target_col)
            if steps == -1:
                return -1
            total_steps += steps
            start_row, start_col = target_row, target_col
            self.forest[start_row][start_col] = 1
        return total_steps
    def public_Chop_down_trees(self):
        return self.__private_Chop_down_trees()

#--------------:
print(CDT([[1, 2, 3], [0, 0, 0], [1, 1, 1]]).public_Chop_down_trees() == 2)
print(CDT([[1, 2, 3], [4, 0, 5], [6, 7, 8]]).public_Chop_down_trees() == 14)
print(CDT([[1, 2, 3], [4, 5, 6], [7, 0, 8]]).public_Chop_down_trees() == 14)
