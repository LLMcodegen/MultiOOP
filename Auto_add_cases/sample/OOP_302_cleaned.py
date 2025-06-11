
class CLT:
    def __init__(self, rows):
        self.rows = rows
class SN_CLT(CLT):
    def __init__(self, rows, cols, rStart, cStart):
        super().__init__(rows)
        self.cols = cols
        self.rStart = rStart
        self.cStart = cStart
    def Coordinate_List(self):
        R, C = self.rows, self.cols
        x, y = self.rStart, self.cStart
        ans = []
        total = R * C
        if 0 <= x < R and 0 <= y < C:
            ans.append([x, y])
        dx, dy = 0, 1
        steps = 1
        while len(ans) < total:
            for _ in range(2):
                for _ in range(steps):
                    x += dx
                    y += dy
                    if 0 <= x < R and 0 <= y < C:
                        ans.append([x, y])
                dx, dy = dy, -dx
            steps += 1
        return ans

#--------------:
print(SN_CLT(4, 5, 3, 2).Coordinate_List() == [[3, 2], [3, 3], [3, 1], [2, 1], [2, 2], [2, 3], [2, 4], [3, 4], [3, 0], [2, 0], [1, 0], [1, 1], [1, 2], [1, 3], [1, 4], [0, 0], [0, 1], [0, 2], [0, 3], [0, 4]])
print(SN_CLT(3, 3, 0, 1).Coordinate_List() == [[0, 1], [0, 2], [1, 2], [1, 1], [1, 0], [0, 0], [2, 2], [2, 1], [2, 0]])
print(SN_CLT(5, 5, 2, 2).Coordinate_List() == [[2, 2], [2, 3], [3, 3], [3, 2], [3, 1], [2, 1], [1, 1], [1, 2], [1, 3], [1, 4], [2, 4], [3, 4], [4, 4], [4, 3], [4, 2], [4, 1], [4, 0], [3, 0], [2, 0], [1, 0], [0, 0], [0, 1], [0, 2], [0, 3], [0, 4]])
