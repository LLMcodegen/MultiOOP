
class DMS:
    def __init__(self, tops):
        self.tops = tops
class SN_DMS(DMS):
    def __init__(self, tops, bottoms):
        super().__init__(tops)
        self.bottoms = bottoms
    def min_rotations(self, target):
        top_rotations = bottom_rotations = 0
        for i in range(len(self.tops)):
            if self.tops[i] != target and self.bottoms[i] != target:
                return float('inf')
            elif self.tops[i] != target:
                top_rotations += 1
            elif self.bottoms[i] != target:
                bottom_rotations += 1
        return min(top_rotations, bottom_rotations)
    def Dominoes(self):
        candidates = {self.tops[0], self.bottoms[0]}
        min_rotations = float('inf')
        for candidate in candidates:
            min_rotations = min(min_rotations, self.min_rotations(candidate))
        return min_rotations if min_rotations != float('inf') else -1

#--------------:
print(SN_DMS([1, 2, 3, 4, 5], [5, 4, 3, 2, 1]).Dominoes() == -1)
print(SN_DMS([1, 2, 3, 4, 5], [1, 2, 3, 4, 5]).Dominoes() == -1)
print(SN_DMS([1, 2, 3, 4, 5], [5, 4, 3, 2, 1]).Dominoes() == -1)
