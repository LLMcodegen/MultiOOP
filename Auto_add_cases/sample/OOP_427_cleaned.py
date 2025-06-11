
class CKB:
    def __init__(self, queens):
        self.queens = queens
class SN_CKB(CKB):
    def __init__(self, queens, king):
        super().__init__(queens)
        self.king = king
    def checkerboard(self):
        queen_positions = set(map(tuple, self.queens))
        result = []
        directions = [ (0,1), (1,1), (1,0), (1,-1), (0,-1), (-1,-1), (-1,0), (-1,1) ]
        for dx, dy in directions:
            x, y = self.king
            while True:
                x += dx
                y += dy
                if not (0 <= x < 8 and 0 <= y < 8):
                    break
                if (x, y) in queen_positions:
                    result.append([x, y])
                    break
        return result

#--------------:
print(SN_CKB([[0,0],[1,1],[2,2],[3,4],[3,5],[4,4],[4,5]], [7,0]).checkerboard() == [[0, 0], [3, 4]])
print(SN_CKB([[0,0],[1,1],[2,2],[3,4],[3,5],[4,4],[4,5]], [7,7]).checkerboard() == [[4, 4]])
print(SN_CKB([[0,0],[1,1],[2,2],[3,4],[3,5],[4,4],[4,5]], [0,0]).checkerboard() == [[1, 1]])
