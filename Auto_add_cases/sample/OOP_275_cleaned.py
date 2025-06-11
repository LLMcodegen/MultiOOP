
class ROP:
    def __init__(self, rec1):
        self.rec1 = rec1
class SN_ROP(ROP):
    def __init__(self, rec1, rec2):
        super().__init__(rec1)
        self.rec2 = rec2
    def Rectangle_overlap(self):
        x1_min, y1_min, x1_max, y1_max = self.rec1
        x2_min, y2_min, x2_max, y2_max = self.rec2
        if x1_max <= x2_min or x2_max <= x1_min:
            return False
        if y1_max <= y2_min or y2_max <= y1_min:
            return False
        return True

#--------------:
print(SN_ROP([0, 0, 2, 2], [0, 0, 1, 1]).Rectangle_overlap() == True)
print(SN_ROP([0, 0, 2, 2], [1, 0, 3, 2]).Rectangle_overlap() == True)
print(SN_ROP([0, 0, 2, 2], [0, 1, 2, 3]).Rectangle_overlap() == True)
