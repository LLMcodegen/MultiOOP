
class OQT:
    def __init__(self, img1):
        self.img1 = img1
class SN_OQT(OQT):
    def __init__(self, img1, img2):
        super().__init__(img1)
        self.img2 = img2
    def Overlap_quantity(self):
        n = len(self.img1)
        def shift_and_count_overlap(dx, dy):
            overlap = 0
            for i in range(n):
                for j in range(n):
                    if 0 <= i + dx < n and 0 <= j + dy < n:
                        overlap += self.img1[i][j] & self.img2[i + dx][j + dy]
            return overlap
        max_overlap = 0
        for dx in range(-n + 1, n):
            for dy in range(-n + 1, n):
                max_overlap = max(max_overlap, shift_and_count_overlap(dx, dy))
        return max_overlap

#--------------:
print(SN_OQT([[1, 0], [0, 1]], [[1, 0], [0, 1]]).Overlap_quantity() == 2)
print(SN_OQT([[1, 0], [0, 1]], [[0, 1], [1, 0]]).Overlap_quantity() == 1)
print(SN_OQT([[1, 1, 1], [1, 0, 0], [1, 0, 0]], [[0, 0, 1], [0, 0, 1], [1, 1, 1]]).Overlap_quantity() == 3)
