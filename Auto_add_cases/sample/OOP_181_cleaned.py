
from collections import deque

class MS:
    def __init__(self, mat):
        self.mat = mat
    def __private_Matrices_size(self):
        rows, cols = len(self.mat), len(self.mat[0])
        distances = [[float('inf')] * cols for _ in range(rows)]
        queue = deque()
        for i in range(rows):
            for j in range(cols):
                if self.mat[i][j] == 0:
                    distances[i][j] = 0
                    queue.append((i, j))
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        while queue:
            x, y = queue.popleft()
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < rows and 0 <= ny < cols:
                    if distances[nx][ny] > distances[x][y] + 1:
                        distances[nx][ny] = distances[x][y] + 1
                        queue.append((nx, ny))
        return distances
    def public_Matrices_size(self):
        return self.__private_Matrices_size()

#--------------:
print(MS([[1, 1, 1], [0, 0, 0], [1, 1, 1]]).public_Matrices_size() == [[1, 1, 1], [0, 0, 0], [1, 1, 1]])
print(MS([[1, 0, 0], [1, 1, 1], [1, 0, 1]]).public_Matrices_size() == [[1, 0, 0], [2, 1, 1], [1, 0, 1]])
print(MS([[0, 1], [1, 0], [1, 1]]).public_Matrices_size() == [[0, 1], [1, 0], [2, 1]])
