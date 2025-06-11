
class WSP:
    def __init__(self, A):
        self.A = A
class SN_WSP(WSP):
    def Width_slope(self):
        max_width = 0
        n = len(self.A)
        for i in range(n):
            for j in range(n - 1, i, -1):
                if self.A[i] <= self.A[j]:
                    max_width = max(max_width, j - i)
                    break
        return max_width

#--------------:
print(SN_WSP([1, 1, 1, 1, 1]).Width_slope() == 4)
print(SN_WSP([5, 4, 3, 2, 1]).Width_slope() == 0)
print(SN_WSP([1, 3, 2, 4, 5]).Width_slope() == 4)
