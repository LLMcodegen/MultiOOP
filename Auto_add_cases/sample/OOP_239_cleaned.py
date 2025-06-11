
class PS:
    def __init__(self, n, mines):
        self.n = n
        self.mines = mines
    def __private_Plus_sign(self):
        grid = [[1] * self.n for _ in range(self.n)]
        for mine in self.mines:
            x, y = mine
            grid[x][y] = 0
        left = [[0] * self.n for _ in range(self.n)]
        right = [[0] * self.n for _ in range(self.n)]
        up = [[0] * self.n for _ in range(self.n)]
        down = [[0] * self.n for _ in range(self.n)]
        for i in range(self.n):
            for j in range(self.n):
                if grid[i][j] == 1:
                    left[i][j] = (left[i][j - 1] + 1) if j > 0 else 1
                    up[i][j] = (up[i - 1][j] + 1) if i > 0 else 1
        for i in range(self.n - 1, -1, -1):
            for j in range(self.n - 1, -1, -1):
                if grid[i][j] == 1:
                    right[i][j] = (right[i][j + 1] + 1) if j < self.n - 1 else 1
                    down[i][j] = (down[i + 1][j] + 1) if i < self.n - 1 else 1
        largest_order = 0
        for i in range(self.n):
            for j in range(self.n):
                if grid[i][j] == 1:
                    order = min(left[i][j], right[i][j], up[i][j], down[i][j])
                    largest_order = max(largest_order, order)
        return largest_order
    def public_Plus_sign(self):
        return self.__private_Plus_sign()

#--------------:
print(PS(3, [[0, 0], [0, 2], [2, 0], [2, 2]]).public_Plus_sign() == 2)
print(PS(4, [[1, 1], [2, 2]]).public_Plus_sign() == 1)
print(PS(4, [[0, 0], [0, 3], [3, 0], [3, 3]]).public_Plus_sign() == 2)
