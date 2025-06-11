
class TPD:
    def __init__(self, grid):
        self.grid = grid
class SN_TPD(TPD):
    def __init__(self, grid):
        super().__init__(grid)
    def Total_projected(self):
        n = len(self.grid)
        xy_projection = 0
        yz_projection = 0
        zx_projection = 0
        for i in range(n):
            for j in range(n):
                if self.grid[i][j] > 0:
                    xy_projection += 1
        for i in range(n):
            max_row = 0
            for j in range(n):
                max_row = max(max_row, self.grid[i][j])
            yz_projection += max_row
        for j in range(n):
            max_col = 0
            for i in range(n):
                max_col = max(max_col, self.grid[i][j])
            zx_projection += max_col
        total_projected_area = xy_projection + yz_projection + zx_projection
        return total_projected_area

#--------------:
print(SN_TPD([[3, 0, 3], [0, 3, 0], [3, 0, 3]]).Total_projected() == 23)
print(SN_TPD([[1, 2, 1], [2, 1, 2], [1, 2, 1]]).Total_projected() == 21)
print(SN_TPD([[4, 0, 4], [0, 4, 0], [4, 0, 4]]).Total_projected() == 29)
