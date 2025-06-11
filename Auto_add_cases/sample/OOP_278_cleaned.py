
class SAX:
    def __init__(self, grid):
        self.grid = grid
class SN_SAX(SAX):
    def submatrix(self):
        def is_magic_square(x, y):
            values = [self.grid[x][y], self.grid[x][y+1], self.grid[x][y+2], self.grid[x+1][y], self.grid[x+1][y+1], self.grid[x+1][y+2], self.grid[x+2][y], self.grid[x+2][y+1], self.grid[x+2][y+2]]
            if sorted(values) != list(range(1, 10)):
                return False
            row1 = self.grid[x][y] + self.grid[x][y+1] + self.grid[x][y+2]
            row2 = self.grid[x+1][y] + self.grid[x+1][y+1] + self.grid[x+1][y+2]
            row3 = self.grid[x+2][y] + self.grid[x+2][y+1] + self.grid[x+2][y+2]
            col1 = self.grid[x][y] + self.grid[x+1][y] + self.grid[x+2][y]
            col2 = self.grid[x][y+1] + self.grid[x+1][y+1] + self.grid[x+2][y+1]
            col3 = self.grid[x][y+2] + self.grid[x+1][y+2] + self.grid[x+2][y+2]
            diag1 = self.grid[x][y] + self.grid[x+1][y+1] + self.grid[x+2][y+2]
            diag2 = self.grid[x][y+2] + self.grid[x+1][y+1] + self.grid[x+2][y]
            return (row1 == row2 == row3 == col1 == col2 == col3 == diag1 == diag2)
        rows = len(self.grid)
        cols = len(self.grid[0])
        count = 0
        for i in range(rows - 2):
            for j in range(cols - 2):
                if is_magic_square(i, j):
                    count += 1
        return count

#--------------:
print(SN_SAX([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]).submatrix() == 0)
print(SN_SAX([[1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1]]).submatrix() == 0)