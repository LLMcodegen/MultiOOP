
class SMT:
    def __init__(self, a):
        self.a = a
class SN_SMT(SMT):
    def __init__(self, a, b, c):
        super().__init__(a)
        self.b = b
        self.c = c
    def Stone_movement(self):
        positions = sorted([self.a, self.b, self.c])
        x, y, z = positions
        min_moves = 0
        if z - y == 1 and y - x == 1:
            min_moves = 0
        elif z - y == 1 or y - x == 1:
            min_moves = 1
        else:
            min_moves = 2
        max_moves = (z - y - 1) + (y - x - 1)
        return [min_moves, max_moves]

#--------------:
print(SN_SMT(1, 2, 3).Stone_movement() == [0, 0])
print(SN_SMT(1, 2, 4).Stone_movement() == [1, 1])
print(SN_SMT(1, 3, 4).Stone_movement() == [1, 1])
